import re

from datetime import datetime, timedelta, date
from pymongo import MongoClient
from os import getenv

_API_CLIENT = MongoClient(getenv('MONGODB_URI'))


def _iso_date(d):
    return datetime.fromisoformat(d.isoformat())


def _api_endpoints(begin: date, end: date):
    data = _API_CLIENT.get_database().get_collection('logs').aggregate([
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
                    '$regex': re.compile('/api/(v2|v1)/(?!schedule)')
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
        }
    ])

    return [(item['_id'], item['count']) for item in data]


def _api_schedule(begin: date, end: date):
    data = _API_CLIENT.get_database().get_collection('logs').aggregate([
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
            '$limit': 5
        }
    ])

    return [(item['_id'], item['count']) for item in data]


def stats_api_daily():
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return (_api_endpoints(begin, end),
            _api_schedule(begin, end))


def stats_api_monthly():
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return (_api_endpoints(begin, end),
            _api_schedule(begin, end))
