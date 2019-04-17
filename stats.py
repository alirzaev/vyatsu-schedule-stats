import re
from datetime import datetime, timedelta, date
from os import getenv

from pymongo import MongoClient

_API_CLIENT = MongoClient(getenv('MONGODB_URI'))
_TG_CLIENT = MongoClient(getenv('TG_MONGODB_URI'))
_V_CLIENT = MongoClient(getenv('V_MONGODB_URI'))


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
        }
    ])

    return [(item['_id'], item['count']) for item in data]


def _api_departments(begin: date, end: date):
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
        }
    ])

    return [(item['_id'], item['count']) for item in data]


def _tg_commands(begin: date, end: date):
    data = _TG_CLIENT.get_database().get_collection('visits').aggregate([
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

    return [(item['_id'], item['count']) for item in data]


def _v_commands(begin: date, end: date):
    data = _V_CLIENT.get_database().get_collection('visit').aggregate([
        {
            '$match': {
                'date': {
                    '$gte': _iso_date(begin),
                    '$lt': _iso_date(end)
                }
            }
        },
        {
            '$group': {
                '_id': '$action',
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


def stats_api_daily():
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return (_api_endpoints(begin, end),
            _api_schedule(begin, end),
            _api_departments(begin, end))


def stats_api_monthly():
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return (_api_endpoints(begin, end),
            _api_schedule(begin, end),
            _api_departments(begin, end))


def stats_tg_daily():
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return _tg_commands(begin, end)


def stats_tg_monthly():
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return _tg_commands(begin, end)


def stats_v_daily():
    begin = date.today()
    end = date.today() + timedelta(days=1)

    return _v_commands(begin, end)


def stats_v_monthly():
    today = date.today()
    begin = date(today.year, today.month, 1)
    end = date.today() + timedelta(days=1)

    return _v_commands(begin, end)
