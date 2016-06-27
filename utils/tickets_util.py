"""
train tickets common function
"""
import re
from colorama import Fore
from datetime import date
from data.station_name import station_name
from .common_util import \
    make_colorful_font, \
    check_month_validation, \
    check_day_validation, \
    convert_validate_date, \
    error_message


def get_station_key(station):
    """convert station to key

    :param station: the station user input
    :return: a validate station key
    """
    upper_stations, lower_stations = station_name()
    if re.findall(u'[a-z]+', station.lower()):
        station_chinese = lower_stations[station.lower()]
        station_key = upper_stations[station_chinese]
        print(station_chinese)
    elif re.findall(u'[\u4e00-\u9fa5]+', station):
        station_key = upper_stations[station]
    else:
        station_key = None
    return station_key


def filter_target_train(train_type):
    """to return a filter function

    :param train_type
    :return: A function to filter target train type
    """
    def target_train(train_obj):
        return train_obj["queryLeftNewDTO"]["station_train_code"][0] == train_type
    return target_train


def handle_font_color(text):
    """A fun to checkout if text should be colorful

    :param text: target text
    :return: colored text
    """
    if text != "--" and text != "无" or text == '有':
        text = make_colorful_font(text, Fore.MAGENTA)
    return text


# def validate_date(date):
#     """check if the date is validate
#
#     :param date: train start date
#     :return: a validate date or return a error message obj
#     """
#     if date is None:
#         return str(datetime.now().date())
#     else:
#         check_result = re.findall(r'-', date)
#         if len(check_result) == 2:
#             date_list = date.split('-')
#             new_date_list = []
#             for i, d in enumerate(date_list):
#                 if i > 0 and len(d) < 2:
#                     new_date = '0{}'.format(d)
#                 else:
#                     new_date = d
#                 new_date_list.append(new_date)
#             return '-'.join(new_date_list)
#         else:
#             if len(date) is 8:
#                 new_date_list = [date[0:4], date[4:6], date[6:8]]
#                 return '-'.join(new_date_list)
#             else:
#                 return dict([('result', 0),
#                              ('message', 'date is invalidate, '
#                                          'you should use \'2016-07-18\' or \'20160718\' or \'2016-7-18\'')])


def validate_raw_date(train_date):
    train_date_len = len(train_date)
    if train_date_len > 5:
        return error_message()
    check_result = re.findall(r'[-/&*$#@+=|]', train_date)
    if len(check_result):
        date_list = train_date.split(check_result[0])
        date_month = date_list[0]
        date_day = date_list[1]
        return convert_full_date(date_month, date_day)
    elif train_date_len in (2, 3, 4):
        return validate_date(train_date)
    else:
        return error_message()


def validate_date(train_date):
    """check if the date is validate

    :param train_date: train start date
    :return: a validate date or return a error message obj
    """
    if train_date is None:
        return str(date.today())
    else:
        date_len = len(train_date)
        if date_len not in (2, 3, 4):
            return error_message('date is invalidate, you should use \'718\' or \'0718\'')
        if date_len == 3:
            return get_date_from_input(train_date)
        if date_len == 2:
            date_month = train_date[0]
            date_day = train_date[1]
        else:
            date_month = train_date[0:2]
            date_day = train_date[2:4]
        return convert_full_date(date_month, date_day)


def get_date_from_input(train_date):
    """get date from user input

    :param train_date: user's input date
    :return: user's target date
    """
    print('你想要输入的是哪个时间?')
    print('{}-0{} or 0{}-{}'.format(train_date[0:2], train_date[2], train_date[0], train_date[1:3]))
    result = int(input('请选择 1 或者 2 : '))
    if result not in (1, 2):
        return error_message('input is invalidate, it should be 1 or 2')
    if result == 1:
        date_month = train_date[0:2]
        date_day = '0{}'.format(train_date[2])
    else:
        date_month = '0{}'.format(train_date[0])
        date_day = train_date[1:3]
    if check_month_validation(date_month) and check_day_validation(date_day):
        return convert_full_date(date_month, date_day)
    else:
        print('该时间有误,请重新输入')
        get_date_from_input(train_date)


def convert_full_date(date_month, date_day):
    """final check & get full date string

    :param date_month: validate input month
    :param date_day: validate input day
    :return: validate full date or error message
    """
    date_month = convert_validate_date(date_month)
    date_day = convert_validate_date(date_day)

    today = date.today()
    today_year = today.year
    today_month = today.month
    if int(date_month) < int(today_month):
        if 12 - int(today_month) + int(date_month) > 3:
            return error_message('超出了可以查询的日期')
        else:
            today_year += 1
    elif int(date_month) - int(today_month) > 3:
        return error_message('超出了可以查询的日期')
    try:
        return str(date(int(today_year), int(date_month), int(date_day)))
    except ValueError:
        return error_message('输入日期有误')
