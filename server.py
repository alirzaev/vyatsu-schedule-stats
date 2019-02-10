from os import getenv, path

import bottle

from stats import stats_api_daily, stats_api_monthly, stats_tg_daily, \
    stats_tg_monthly, stats_v_monthly, stats_v_daily

BASE_URL = getenv('BASE_URL')

app_dir = path.dirname(path.realpath(__file__))
views_dir = path.join(app_dir, 'views')
bottle.TEMPLATE_PATH.insert(0, views_dir)


@bottle.error(404)
def error(error):
    return bottle.template('404')


@bottle.get(f'/{BASE_URL}')
@bottle.view('api')
def index():
    daily = stats_api_daily()
    monthly = stats_api_monthly()

    head = ('API endpoints', 'Кол-во')

    tables = [
        dict(head=head, body=daily[0]),
        dict(head=head, body=daily[1]),
        dict(head=head, body=monthly[0]),
        dict(head=head, body=monthly[1])
    ]
    return dict(tables=tables, base_url=BASE_URL)


@bottle.get(f'/{BASE_URL}/telegram')
@bottle.view('telegram')
def index():
    daily = stats_tg_daily()
    monthly = stats_tg_monthly()

    head = ('Команды', 'Кол-во')

    tables = [
        dict(head=head, body=daily),
        dict(head=head, body=monthly)
    ]
    return dict(tables=tables, base_url=BASE_URL)


@bottle.get(f'/{BASE_URL}/viber')
@bottle.view('viber')
def index():
    daily = stats_v_daily()
    monthly = stats_v_monthly()

    head = ('Команды', 'Кол-во')

    tables = [
        dict(head=head, body=daily),
        dict(head=head, body=monthly)
    ]
    return dict(tables=tables, base_url=BASE_URL)


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
else:
    app = bottle.default_app()
