"""
common functions
"""
from colorama import Fore


def make_colorful_font(text, color=Fore.CYAN, reset_color=Fore.RESET):
    """make text colorful

    :param text: target text
    :param color: font color, default color is Fore.CYAN
    :param reset_color
    :return: colored text
    """
    return color + text + reset_color


def check_month_validation(month):
    """check if month is validate

    :param month: input month
    :return: if month is validate
    """
    return int(month) in range(1, 13)


def check_day_validation(day):
    """check if day is validate

    :param day: input day
    :return: if day is validate
    """
    # TODO different month has different mount days
    return int(day) in range(1, 30)


def convert_validate_date(input_date):
    """

    :param input_date
    :return: validate date
    """
    if len(input_date) == 1:
        input_date = '0{}'.format(input_date)
    return input_date


def error_message(message='date is invalidate, you should use \'718\' or \'0718\' or \'7/18\' or \'7-18\'', result=0):
    return dict([('result', result), ('message', message)])


def success_message(message):
    return error_message(message, 1)
