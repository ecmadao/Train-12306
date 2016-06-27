"""
use nosetests
"""
from datetime import date
from utils import tickets_util
from spider import fetch_trains

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'
FROM_STATION = '北京'
TO_STATION = '厦门'


def test_12306_interface():
    from_station_key = tickets_util.get_station_key(FROM_STATION)
    to_station_key = tickets_util.get_station_key(TO_STATION)
    start_date = tickets_util.validate_date(None)

    fetch_url = URL.format(date=start_date, from_station_key=from_station_key, to_station_key=to_station_key)
    train_tickets = fetch_trains.TrainTickets(fetch_url)
    tickets_result = train_tickets.fetch_tickets()
    assert tickets_result['status'] in (1, True)


def test_invalidate_date():
    invalidate_date = '2016718'
    date_result = tickets_util.validate_date(invalidate_date)
    print(date_result['message'])
    assert isinstance(date_result, object)

    invalidate_date = '20160718'
    date_result = tickets_util.validate_date(invalidate_date)
    assert date_result == '2016-07-18'

    invalidate_date = None
    date_result = tickets_util.validate_date(invalidate_date)
    assert date_result == str(date.today())
