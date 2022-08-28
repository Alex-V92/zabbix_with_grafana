<p align="center">
   <img src="https://i.ibb.co/0cmZmRf/2022-08-19-10-30-23.png" alt="csv-файл">
   <img src="https://i.ibb.co/TvPsGkr/2022-08-07-20-56-26.png" alt="Grafana">
</p>

## About
<p>Единая сводка статусов выбранных метрик узлов через zabbix_api.</p>
<p>Задачи:</p>
<p>Объединить сводки отдельных метрик в единую таблицу.</p>
<p>Задавать требуемые метрики как CLI опции.</p>
<p>Создать тесты разбора опций CLI, формирования результирующей сводки без обращения к Zabbix_API.</p>
<p>Создать, на основе выгруженного csv-файла, панель объединённых сводок в Grafana.</p>

## Documentation
<p>Аргументы командной строки:</p>
<p>--verbose : Вывод дополнительных сообщений при выполнение скрипта в командной строке.</p>
<p>--target : Место для сохранения csv-файла. Имеет значение поумолчанию.</p>
<p>--metric : Список метрик через запятую.</p>
