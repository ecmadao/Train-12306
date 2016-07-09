"""

Usage:
    train [-g | -d | -t | -k | -z] <from> <to> [<date>]
    train (-h | --help)

Options:
    -h --help  显示帮助菜单
    -g         高铁
    -d         动车
    -t         特快
    -k         快速
    -z         直达
    <from>     出发站
    <to>       目的站
    <date>     出发日期, 默认为当日

Examples:
    train 南京 北京 07-18
    train 南京 北京 7-18
    train 南京 北京 07/18
    train 南京 北京 7/18
    train 南京 北京 0718
    train 南京 北京 718
    train -g 南京 北京 07-18
"""
from docopt import docopt
from .data import trains


TRAIN_TYPE = ('-g', '-d', '-t', '-k', '-z')


def get_args():
    """get input arguments and fetch trains

    :return: None
    """
    arguments = docopt(__doc__, version="beta 0.1")
    train_type = {t.split('-')[-1].upper(): arguments[t] for t in TRAIN_TYPE}
    from_station = arguments['<from>']
    to_station = arguments['<to>']
    date = arguments['<date>']
    trains.fetch_train_tickets(from_station, to_station, train_type, date)

# if __name__ == '__main__':
#     get_args()
