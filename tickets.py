# coding uft-8
"""

Usage:
    tickets [-gdtkz] <from> <to> [<date>]

Options:
    -h, --help 显示帮助菜单
    -g 高铁
    -d 动车
    -t 特快
    -k 快速
    -z 直达

Examples:
    tickets 南京 北京 2016-07-01
    tickets -g 南京 北京 2016-07-01
"""

from docopt import docopt
from data import index


def get_args():
    arguments = docopt(__doc__, version="beta 0.1")
    from_station = arguments['<from>']
    to_station = arguments['<to>']
    date = arguments['<date>']
    index.fetch_train_tickets(from_station, to_station, date)

if __name__ == '__main__':
    get_args()
