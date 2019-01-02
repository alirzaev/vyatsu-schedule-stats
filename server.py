from os import getenv

import bottle

from stats import stats_api_daily, stats_api_monthly, stats_tg_daily, \
    stats_tg_monthly

USERNAME = getenv('USERNAME')
PASSWORD = getenv('PASSWORD')


def get_cookie():
    return bottle.request.get_cookie('cookie', None)


@bottle.error(404)
def error(error):
    return bottle.template('404')


@bottle.get('/')
@bottle.view('api')
def index():
    cookie = get_cookie()
    if cookie is None:
        bottle.redirect('/login')
    else:
        daily = stats_api_daily()
        monthly = stats_api_monthly()

        head = ('API endpoints', 'Кол-во')

        tables = [
            dict(head=head, body=daily[0]),
            dict(head=head, body=daily[1]),
            dict(head=head, body=monthly[0]),
            dict(head=head, body=monthly[1])
        ]
        return dict(name=cookie, tables=tables)


@bottle.get('/telegram')
@bottle.view('telegram')
def index():
    cookie = get_cookie()
    if cookie is None:
        bottle.redirect('/login')
    else:
        daily = stats_tg_daily()
        monthly = stats_tg_monthly()

        head = ('Команды', 'Кол-во')

        tables = [
            dict(head=head, body=daily),
            dict(head=head, body=monthly)
        ]
        return dict(name=cookie, tables=tables)


@bottle.get('/login')
@bottle.view('login')
def login():
    return dict(name=get_cookie())


@bottle.post('/login')
def login():
    username = bottle.request.forms['username']
    password = bottle.request.forms['password']

    if username == USERNAME and password == PASSWORD:
        bottle.response.set_cookie('cookie', 'logged_in')
        bottle.redirect('/')
    else:
        bottle.abort(401, 'Неверное имя пользователя или пароль')


@bottle.post('/logout')
def logout():
    bottle.response.delete_cookie('cookie')
    bottle.redirect('/')


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
else:
    app = bottle.default_app()
