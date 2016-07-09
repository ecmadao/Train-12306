from datetime import date
from .data import trains


def get_today_date():
    return ''.join(str(date.today()).split('-')[1:3])
