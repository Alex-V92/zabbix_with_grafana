def item_get_data_test1():
    return [{'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '35028123',
             'lastclock': '1658404511',
             'lastvalue': '1',
             'name': 'domain'},
            {'hosts': [{'hostid': '233814', 'name': '0106NBA00UNQ6LR'}],
             'itemid': '45174729',
             'lastclock': '0',
             'lastvalue': '0',
             'name': 'domain'},
            {'hosts': [{'hostid': '233854', 'name': '0402NBA05YCQ6L4'}],
             'itemid': '45191909',
             'lastclock': '0',
             'lastvalue': '0',
             'name': 'domain'}]


def item_get_data_test2():
    return [{'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '35028123',
             'lastclock': '1658405717',
             'lastvalue': '1',
             'name': 'domain'},
            {'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '48194543',
             'lastclock': '1658405717',
             'lastvalue': '0',
             'name': 'mdm'},
            {'hosts': [{'hostid': '193903', 'name': '0000NBA00640794'}],
             'itemid': '45375039',
             'lastclock': '1658405717',
             'lastvalue': 'Service',
             'name': 'battery_condition'},
            {'hosts': [{'hostid': '233814', 'name': '0106NBA00UNQ6LR'}],
             'itemid': '45174729',
             'lastclock': '0',
             'lastvalue': '0',
             'name': 'domain'},
            {'hosts': [{'hostid': '233814', 'name': '0106NBA00UNQ6LR'}],
             'itemid': '48194544',
             'lastclock': '0',
             'lastvalue': '0',
             'name': 'mdm'}]


def data_for_save_to_csv_test1():
    return {'0000NBA00640794': [('domain', '1', '2022-07-21 14:55:11')],
            '0106NBA00UNQ6LR': [('domain', '0', '1970-01-01 03:00:00')],
            '0402NBA05YCQ6L4': [('domain', '0', '1970-01-01 03:00:00')]}


def data_for_save_to_csv_test2():
    return {'0000NBA00640794': [('domain', '1', '2022-07-21 15:15:17'),
                                ('mdm', '0', '2022-07-21 15:15:17'),
                                ('battery_condition',
                                 'Service',
                                 '2022-07-21 15:15:17')],
            '0106NBA00UNQ6LR': [('domain', '0', '1970-01-01 03:00:00'),
                                ('mdm', '0', '1970-01-01 03:00:00')]}


def save_data_to_csv_test_target():
    return '/.../unittest_source'


def save_data_to_csv_test_fieldsnames():
    return ['hostname', 'battery_condition', 'lastclock', 'domain', 'lastclock', 'mdm', 'lastclock']


def save_data_to_csv_test_data():
    return {
        '0000NBB05CUQ6L4': [('domain', '1', '2022-10-09 03:00:00'), ('mdm', '0', '1970-01-01 03:00:00'),
                            ('battery_condition', '', '1970-01-01 03:00:00')],
        '0300NBQ005LLVCF': [('domain', '1', '2020-01-01 03:00:00'), ('mdm', '0', '1970-01-01 03:00:00'),
                            ('battery_condition', '', '1970-01-01 03:00:00')],
        '0000NBA0RG1Q6L4': [('domain', '1', '2022-01-01 03:00:00'), ('mdm', '0', '1970-01-01 03:00:00'),
                            ('battery_condition', '', '1970-01-01 03:00:00')],
        '0300NBB000FMD6M': [('domain', '0', '1970-01-01 03:00:00'), ('mdm', '1', '2022-01-01 03:00:00'),
                            ('battery_condition', '', '1970-01-01 03:00:00')]
    }
