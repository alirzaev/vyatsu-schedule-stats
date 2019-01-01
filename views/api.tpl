% rebase('basepage.tpl', title='Статистика API')

<h2 class="pt-1">Статистика за сегодня</h2>

<h3>Вызовы API</h3>

% include('table.tpl', data=tables[0])

<h3 class="pt-1">Часто загружаемые расписания</h3>

% include('table.tpl', data=tables[1])

<h2 class="pt-1">Статистика за месяц</h2>

<h3>Вызовы API</h3>

% include('table.tpl', data=tables[2])

<h3 class="pt-1">Часто загружаемые расписания</h3>

% include('table.tpl', data=tables[3])