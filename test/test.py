from data import index
from spider import fetch_trains
from datetime import datetime

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'
FROM_STATION = '北京'
TO_STATION = '厦门'


def test_12306_interface():
    from_station_key = index.get_station_key(FROM_STATION)
    to_station_key = index.get_station_key(TO_STATION)
    date = str(datetime.now()).split(' ')[0]

    fetch_url = URL.format(date=date, from_station_key=from_station_key, to_station_key=to_station_key)
    train_tickets = fetch_trains.TrainTickets(fetch_url)
    tickets_result = train_tickets.fetch_tickets()
    assert tickets_result['status'] in (1, True)
