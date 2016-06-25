import re
from datetime import datetime
from .station_name import station_name
from spider import fetch_trains

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'


def fetch_train_tickets(from_station, to_station, date=None):
    if date is None:
        date = str(datetime.now()).split(' ')[0]
    from_station_key = get_station_key(from_station)
    to_station_key = get_station_key(to_station)
    fetch_url = URL.format(date=date, from_station_key=from_station_key, to_station_key=to_station_key)
    train_tickets = fetch_trains.TrainTickets(fetch_url)
    tickets_result = train_tickets.fetch_tickets()
    print(tickets_result)


def get_station_key(station):
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
