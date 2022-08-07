#!/usr/bin/env python3.6


import base64
import datetime
from pyzabbix import ZabbixAPI
import requests
import csv
from urllib3.exceptions import InsecureRequestWarning
from collections import defaultdict
from operator import itemgetter
from arg_pars_metrics import metrics, target, verbose

GROUP_NAME = "group name in zabbix server"

#
# Entry point
#

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def zapi_connect():
    """Создание экземпляра объекта Zabbix API

    :return:
        Экземпляр объекта соединения с сервером заббикс
    """
    try:
        zapi = ZabbixAPI('https://zabbix_server')
        zapi.session.verify = False
        zapi.timeout = 123

        zapi.login(*
                   (
                       'data for login to zabbix server'
                   )
                   )

    except Exception as e:
        raise ('Zabbix server connection error..', str(e))

    # Поиск id группы, которая соответствует константе GROUP_NAME
    groups = zapi.hostgroup.get(output=['itemid', 'name'])
    gid = None
    for group in groups:
        if (group['name'] == GROUP_NAME):
            gid = group['groupid']
            break

    if gid == None:
        raise f'Zabbix group "{GROUP_NAME}" id not found...'

    return zapi, gid


def items_get_all():
    """Список всех метрик из указанной groupID и добавление элемента в список по шаблону ключ:значение,
    где ключ - это name, а значение - имя хоста

    :return:
        Возвращает список вида [{'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '35028123',
             'lastclock': '1658404511',
             'lastvalue': '1',
             'name': 'domain'},...]

    """
    zapi, gid = zapi_connect()
    items = zapi.item.get(
        groupids=gid,
        filter={'name': metrics()},
        output=['name', 'lastvalue', 'lastclock'],
        selectHosts=['name']
    )
    if not items:
        raise f'Zabbix metrics "{metrics()}" id not found...'

    return items


def data_for_save_csv(result=items_get_all):
    """Возвращает словарь, где ключ - имя хоста, а значение - это список метрик

    :param result:
        По умолчанию cписок из функции item_get_all() вида
        [{'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '35028123',
             'lastclock': '1658404511',
             'lastvalue': '1',
             'name': 'domain'},...]
    :return:
        Словарь вида {'0000NBA00640794': [('domain', '1', '2022-07-21 14:55:11')],...}
    """
    data_to_csv = defaultdict(list)
    for ele in result():
        metric = ele['name']
        value = ele['lastvalue']
        lastclock = datetime.datetime.fromtimestamp(int(ele['lastclock'])).strftime(
            '%Y-%m-%d %H:%M:%S')
        hostname = ele['hosts'][0]['name']
        data_to_csv[hostname].append((metric, value, lastclock))
    return data_to_csv


def create_fieldsname_to_csv(data=data_for_save_csv):
    """Формирует список для заголовков в csv-файле

    :param data:
        По умолчанию cлоаварь из функции data_fro_save_csv.
        Имеет вид {'0000NBA00640794': [('domain', '1', '2022-07-21 14:55:11'), ...], ...}
    :return:
        Возвращает список с именами заголовков для csv-файла
    """
    fields_name_in_csv = []
    for ele in data().values():
        fields_name_in_csv = sorted([i[0] for i in ele])
        # Одна итерация по вложенному циклу для вставки после каждой метрики заголовка lastclock
        for i in range(len(fields_name_in_csv)):
            fields_name_in_csv.insert((i * 2) + 1, 'lastclock')
        break
    fields_name_in_csv.insert(0, 'hostname')
    return fields_name_in_csv


def save_data_to_csv(target=target, fieldsnames=create_fieldsname_to_csv, data=data_for_save_csv):
    """Сохраняет полученные данные в csv файл

    :param target:
        Место сохранения csv-файла. По умолчанию ...
    :param fieldsnames:
        Список из заголовков в создаваемом csv-файле. По умолчанию из функции create_fieldsname_to_csv
    :param data:
        Словарь, состоящий из данных хостов и их метрик. По умолчанию из функции data_for_save_csv
    :return:
        Не возвращает значений. Выполняет запись csv файла
    """
    with open(f'{target()}/all_metrics_mac_os.csv', 'w') as csvfile:
        # Создание экземпляра объекта для записи полученных данных в csv-файл
        writter = csv.writer(csvfile, delimiter=',')
        writter.writerow(fieldsnames())

        for key, value in data().items():
            # Сортировка по имени для корректной записи
            list_to_row_csv = list([i[1:] for i in sorted(value, key=itemgetter(0))])
            # Убирается вложенность списка
            list_to_row_csv = list(sum(list_to_row_csv, ()))
            # Если у хоста не отслеживается ни одной метрики, то запись не производится
            if set(list_to_row_csv) == {'', '0', '1970-01-01 03:00:00'} \
                    or set(list_to_row_csv) == {'1970-01-01 03:00:00', '0'}:
                continue
            list_to_row_csv.insert(0, key)
            writter.writerow(list_to_row_csv)


if __name__ == '__main__':
    if verbose() != 0:
        print(f'Выполнение формирования метрик{metrics()} в каталог {target()}')
        save_data_to_csv()
        print('Выполнено')
    else:
        save_data_to_csv()
