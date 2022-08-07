#!/usr/bin/env python3.6

import unittest
import sys
import os.path

sys.path.insert(0, '/...')
import csv
from summary_macos_api_zabbix import data_for_save_csv, create_fieldsname_to_csv, save_data_to_csv
from conf_data_for_test import item_get_data_test1, item_get_data_test2
from conf_data_for_test import data_for_save_to_csv_test1, data_for_save_to_csv_test2
from conf_data_for_test import save_data_to_csv_test_fieldsnames
from conf_data_for_test import save_data_to_csv_test_target
from conf_data_for_test import save_data_to_csv_test_data
from arg_pars_metrics import parse_args


class TestAllTargetMetrics(unittest.TestCase):

    def test_data_for_save_csv(self):
        self.assertEqual(
            data_for_save_csv(item_get_data_test1),
            {'0000NBA00640794': [('domain', '1', '2022-07-21 14:55:11')],
             '0106NBA00UNQ6LR': [('domain', '0', '1970-01-01 03:00:00')],
             '0402NBA05YCQ6L4': [('domain', '0', '1970-01-01 03:00:00')]}
        )

        self.assertEqual(
            data_for_save_csv(item_get_data_test2),
            {'0000NBA00640794': [('domain', '1', '2022-07-21 15:15:17'),
                                 ('mdm', '0', '2022-07-21 15:15:17'),
                                 ('battery_condition',
                                  'Service',
                                  '2022-07-21 15:15:17')],
             '0106NBA00UNQ6LR': [('domain', '0', '1970-01-01 03:00:00'),
                                 ('mdm', '0', '1970-01-01 03:00:00')]}
        )

    def test_create_fieldnames_to_csv(self):
        self.assertEqual(
            create_fieldsname_to_csv(data_for_save_to_csv_test1),
            ['hostname', 'domain', 'lastclock']
        )

        self.assertEqual(
            create_fieldsname_to_csv(data_for_save_to_csv_test2),
            ['hostname', 'battery_condition', 'lastclock',
             'domain', 'lastclock', 'mdm', 'lastclock']
        )

    def test_parse_args(self):
        parser = parse_args(['--metric', 'mdm,domain', '--target', '...', '--verbose'])
        self.assertTrue(parser.metric)

        self.assertEqual(
            parser.metric,
            'mdm,domain'
        )

        self.assertTrue(parser.target)

        self.assertEqual(
            parser.target,
            '...'
        )

        self.assertTrue(parser.verbose)

        self.assertEqual(
            parser.verbose,
            1
        )

    def test_save_data_to_csv(self):
        data = save_data_to_csv_test_data
        target = save_data_to_csv_test_target
        fieldsnames = save_data_to_csv_test_fieldsnames
        save_data_to_csv(target, fieldsnames, data)
        with open('all_metrics_mac_os.csv', 'r') as test_csv:
            reader = csv.reader(test_csv)
            fieldname_one = next(reader)
            fieldname_two = next(reader)

        self.assertTrue(os.path.isfile(
            '/.../unittest_source/all_metrics_mac_os.csv'
        ))

        self.assertEqual(
            fieldname_one,
            ['hostname', 'battery_condition', 'lastclock', 'domain', 'lastclock', 'mdm', 'lastclock']
        )

        self.assertEqual(
            fieldname_two,
            ['0000NBB05CUQ6L4', '', '1970-01-01 03:00:00',
             '1', '2022-10-09 03:00:00',
             '0', '1970-01-01 03:00:00']
        )


if __name__ == '__main__':
    unittest.main()
