import re
from colorama import Fore
from data.station_name import station_name
from .common_util import make_colorful_font


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


def validate_date(date):
    """check if the date is validate

    :param date: train start date
    :return: a validate date or return a error message obj
    """
    check_result = re.findall(r'-', date)
    if len(check_result) == 2:
        date_list = date.split('-')
        new_date_list = []
        for i, d in enumerate(date_list):
            if i > 0 and len(d) < 2:
                new_date = '0{}'.format(d)
            else:
                new_date = d
            new_date_list.append(new_date)
        return '-'.join(new_date_list)
    else:
        if len(date) is 8:
            new_date_list = [date[0:4], date[4:6], date[6:8]]
            return '-'.join(new_date_list)
        else:
            return dict([('result', 0),
                         ('message', 'date is invalidate, '
                                     'you should use \'2016-07-18\' or \'20160718\' or \'2016-7-18\'')])
