% rebase('basepage.tpl')

<nav class="nav pt-2 pb-2">
  <a class="nav-link" href="#api">API</a>
  <a class="nav-link" href="#telegram">Telegram-бот</a>
  <a class="nav-link" href="#viber">Viber-бот</a>
</nav>

<h1 id="api">Статистика API</h1>

<h2 class="pt-1">Статистика за сегодня</h2>

<h3>Вызовы API</h3>

% include('table.tpl', data=api_tables[0])

<h3 class="pt-1">Часто загружаемые расписания</h3>

% include('table.tpl', data=api_tables[1])

<h3 class="pt-1">Часто загружаемые кафедры</h3>

% include('table.tpl', data=api_tables[2])

<h2 class="pt-1">Статистика за месяц</h2>

<h3>Вызовы API</h3>

% include('table.tpl', data=api_tables[3])

<h3 class="pt-1">Часто загружаемые расписания</h3>

% include('table.tpl', data=api_tables[4])

<h3 class="pt-1">Часто загружаемые кафедры</h3>

% include('table.tpl', data=api_tables[5])

<hr>


<h1 id="telegram">Telegram-бот</h1>

<h2 class="pt-1">Статистика за сегодня</h2>

% include('table.tpl', data=tg_tables[0])

<h2 class="pt-1">Статистика за месяц</h2>

% include('table.tpl', data=tg_tables[1])

<hr>


<h1 id="viber">Viber-бот</h1>

<h2 class="pt-1">Статистика за сегодня</h2>

% include('table.tpl', data=v_tables[0])

<h2 class="pt-1">Статистика за месяц</h2>

% include('table.tpl', data=v_tables[1])