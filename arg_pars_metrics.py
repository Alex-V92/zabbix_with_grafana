import sys
import argparse


def parse_args(args=sys.argv[1:]):
    cli = argparse.ArgumentParser(
        description='Выгрузить сводки метрик в отдельные CSV'
    )
    cli.add_argument(
        '--verbose', default=0, action="count",
        help='Вывод дополнительных сообщений'
    )
    cli.add_argument(
        '--target', metavar='путь, папка ФС',
        default="...",
        help='Место для сохранения CSV'
    )
    cli.add_argument(
        '--metric', metavar='метрики',
        help='Список метрик через запятую'
    )
    cfg = cli.parse_args(args)

    if cfg.metric == None:
        raise ('arguments required..')

    return cfg


def target(argv=sys.argv[1:]):
    return parse_args(argv).target


def metrics(argv=sys.argv[1:]):
    return parse_args(argv).metric.split(',')


def verbose(argv=sys.argv[1:]):
    return parse_args(argv).verbose
