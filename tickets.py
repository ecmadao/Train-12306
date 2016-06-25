# coding uft-8
"""

Usage:
    tickets [-gdtkz] <from> <to> <date>

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

if __name__ == '__main__':
    arguments = docopt(__doc__, version="beta 0.1")
    print(arguments)