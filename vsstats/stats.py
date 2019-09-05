import re
from datetime import datetime, timedelta, date
from os import getenv

from pymongo import MongoClient

_TG_CLIENT = MongoClient(getenv('TG_MONGODB_URI'))


def _iso_date(d):
    return datetime.fromisoformat(d.isoformat())


def _api_endpoints(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('logs').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$match': {
                'path': {
                    '$regex': re.compile('/api/(v2|v1)/(?!schedule|department(?!s))')
                }
            }
        },
        {
            '$group': {
                '_id': {
                    "$substr": ["$path", 0, {"$indexOfBytes": ["$path", "?"]}]
                },
                'count': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                '_id': 1
            }
        }
    ])

    return [{'endpoint': item['_id'], 'count': item['count']} for item in data]


def _api_schedule(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('logs').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$match': {
                'path': {
                    '$regex': re.compile('/api/(v2|v1)/schedule')
                }
            }
        },
        {
            '$group': {
                '_id': {
                    "$substr": ["$path", 0, {"$indexOfBytes": ["$path", "?"]}]
                },
                'count': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ])

    return [{'schedule': item['_id'], 'count': item['count']} for item in data]


def _api_departments(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('logs').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$match': {
                'path': {
                    '$regex': re.compile('/api/(v2|v1)/department(?!s)')
                }
            }
        },
        {
            '$group': {
                '_id': {
                    "$substr": ["$path", 0, {"$indexOfBytes": ["$path", "?"]}]
                },
                'count': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ])

    return [{'department': item['_id'], 'count': item['count']} for item in data]


def _tg_commands(url: str, begin: date, end: date):
    data = MongoClient(url).get_database().get_collection('visits').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$match': {
                'type': 'MESSAGE',
                'data': {
                    '$regex': re.compile(r'^/.*')
                }
            }
        },
        {
            '$group': {
                '_id': '$data',
                'count': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                'count': -1
            }
        }
    ])

    return [{'command': item['_id'], 'count': item['count']} for item in data]


def _tg_users(url, begin, end):
    data = MongoClient(url).get_database().get_collection('visits').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$match': {
                'data': {
                    '$regex': re.compile(r'^/.*')
                }
            }
        },
        {
            '$group': {
                '_id': '$telegram_id'
            }
        },
        {
            '$count': 'users'
        }
    ])

    t = tuple(data)
    if len(t) > 0:
        return t[0]['users']
    else:
        return 0


def stats_api(url, begin, end):
    return {'endpoints': _api_endpoints(url, begin, end),
            'schedules': _api_schedule(url, begin, end),
            'departments': _api_departments(url, begin, end)}


def stats_tg(url, begin, end):
    return {'commands': _tg_commands(url, begin, end),
            'users': _tg_users(url, begin, end)}


def stats_api_daily(url):
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return {'endpoints': _api_endpoints(url, begin, end),
            'schedules': _api_schedule(url, begin, end),
            'departments': _api_departments(url, begin, end)}


def stats_api_monthly(url):
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return {'endpoints': _api_endpoints(url, begin, end),
            'schedules': _api_schedule(url, begin, end),
            'departments': _api_departments(url, begin, end)}


def stats_tg_daily(url):
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return {'commands': _tg_commands(url, begin, end),
            'users': _tg_users(url, begin, end)}


def stats_tg_monthly(url):
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return {'commands': _tg_commands(url, begin, end),
            'users': _tg_users(url, begin, end)}
