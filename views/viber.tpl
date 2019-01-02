% rebase('basepage.tpl', title='Статистика Viber-бота')

<h2 class="pt-1">Статистика за сегодня</h2>

% include('table.tpl', data=tables[0])

<h2 class="pt-1">Статистика за месяц</h2>

% include('table.tpl', data=tables[1])
