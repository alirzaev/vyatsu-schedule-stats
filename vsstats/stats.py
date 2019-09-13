import re
from datetime import datetime, timedelta, date
from os import getenv

from pymongo import MongoClient

_TG_CLIENT = MongoClient(getenv('TG_MONGODB_URI'))


def _iso_date(d):
    return datetime.fromisoformat(d.isoformat())


def _filter_by_date(begin: date, end: date):
    return {
        '$match': {
            'date': {
                '$gte': _iso_date(begin),
                '$lt': _iso_date(end)
            }
        }
    }


def _filter_by_regex(field: str, regex):
    return {
        '$match': {
            f'{field}': {
                '$regex': regex
            }
        }
    }


def _filter_by_str(field: str, substr):
    return {
        '$match': {
            f'{field}': substr
        }
    }


def _sort_by(field: str, direction: int):
    return {
        '$sort': {
            f'{field}': direction
        }
    }


def _group_by_url(field: str):
    return {
            '$group': {
                '_id': {
                    "$substr": [f"${field}", 0, {"$indexOfBytes": [f"${field}", "?"]}]
                },
                'count': {
                    '$sum': 1
                }
            }
        }


def _limit(limit: int):
    return {
        '$limit': limit
    }


def _api_endpoints(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('logs').aggregate([
        _filter_by_date(begin, end),
        _filter_by_regex(
            'path', re.compile('/api/(v2|v1)/(?!schedule|department(?!s))')),
        _group_by_url('path'),
        _sort_by('_id', 1)
    ])

    return [{'endpoint': item['_id'], 'count': item['count']} for item in data]


def _api_schedules(url: str, begin: date, end: date):
    pipeline = [
        _filter_by_date(begin, end),
        _filter_by_regex('path', re.compile('/api/(v2|v1)/schedule')),
        _group_by_url('path'),
        _sort_by('count', -1)
    ]
    logs = MongoClient(url).get_database().get_collection('logs')

    top = [{
        'schedule': item['_id'],
        'count': item['count']
    } for item in logs.aggregate(pipeline + [_limit(10)])]
    total = sum(item['count'] for item in logs.aggregate(pipeline))

    return {
        'top': top,
        'total': total
    }


def _api_departments(url: str, begin: date, end: date):
    pipeline = [
        _filter_by_date(begin, end),
        _filter_by_regex('path', re.compile('/api/(v2|v1)/department(?!s)')),
        _group_by_url('path'),
        _sort_by('count', -1)
    ]
    logs = MongoClient(url).get_database().get_collection('logs')

    top = [{
        'department': item['_id'],
        'count': item['count']
    } for item in logs.aggregate(pipeline + [_limit(10)])]
    total = sum(item['count'] for item in logs.aggregate(pipeline))

    return {
        'top': top,
        'total': total
    }


def _tg_commands(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('visits').aggregate([
        _filter_by_date(begin, end),
        _filter_by_str('type', 'MESSAGE'),
        _filter_by_regex('data', re.compile(r'^/.*')),
        {
            '$group': {
                '_id': '$data',
                'count': {
                    '$sum': 1
                }
            }
        },
        _sort_by('count', -1),
    ])

    return [{'command': item['_id'], 'count': item['count']} for item in data]


def _tg_users(url, begin, end):
    data = MongoClient(url).get_database().get_collection('visits').aggregate([
        _filter_by_date(begin, end),
        _filter_by_regex('data', re.compile(r'^/.*')),
        {
            '$group': {
                '_id': '$telegram_id'
            }
        }
    ])

    return len(tuple(data))


def stats_api(url, begin, end):
    return {'endpoints': _api_endpoints(url, begin, end),
            'schedules': _api_schedules(url, begin, end),
            'departments': _api_departments(url, begin, end)}


def stats_tg(url, begin, end):
    return {'commands': _tg_commands(url, begin, end),
            'users': _tg_users(url, begin, end)}
