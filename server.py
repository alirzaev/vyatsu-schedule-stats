from os import getenv, path

import bottle

from stats import stats_api_daily, stats_api_monthly, stats_tg_daily, \
    stats_tg_monthly, stats_v_monthly, stats_v_daily

BASE_URL = getenv('BASE_URL')

app_dir = path.dirname(path.realpath(__file__))
views_dir = path.join(app_dir, 'views')
bottle.TEMPLATE_PATH.insert(0, views_dir)


@bottle.get(f'/{BASE_URL}')
@bottle.view('index')
def index():
    api_daily = stats_api_daily()
    api_monthly = stats_api_monthly()

    schedule_total_daily = ('Всего', sum(t[1] for t in api_daily[1]))
    schedule_total_monthly = ('Всего', sum(t[1] for t in api_monthly[1]))

    department_total_daily = ('Всего', sum(t[1] for t in api_daily[2]))
    department_total_monthly = ('Всего', sum(t[1] for t in api_monthly[2]))

    api_head = ('API endpoints', 'Кол-во')
    api_tables = [
        dict(head=api_head, body=api_daily[0]),
        dict(head=api_head, body=api_daily[1][:5] + [schedule_total_daily]),
        dict(head=api_head, body=api_daily[2][:5] + [department_total_daily]),
        dict(head=api_head, body=api_monthly[0]),
        dict(head=api_head, body=api_monthly[1][:5] + [schedule_total_monthly]),
        dict(head=api_head, body=api_monthly[2][:5] + [department_total_monthly])
    ]

    tg_daily = stats_tg_daily()
    tg_monthly = stats_tg_monthly()
    tg_head = ('Команды', 'Кол-во')
    tg_tables = [
        dict(head=tg_head, body=tg_daily),
        dict(head=tg_head, body=tg_monthly)
    ]

    v_daily = stats_v_daily()
    v_monthly = stats_v_monthly()
    v_head = ('Команды', 'Кол-во')
    v_tables = [
        dict(head=v_head, body=v_daily),
        dict(head=v_head, body=v_monthly)
    ]

    return dict(api_tables=api_tables,
                api_schedules_total=(schedule_total_daily, schedule_total_monthly),
                tg_tables=tg_tables,
                v_tables=v_tables)


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
else:
    app = bottle.default_app()
