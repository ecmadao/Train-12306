import re
from datetime import datetime
import json
from colorama import Fore, Back
from .station_name import station_name
from spider import fetch_trains
from prettytable import PrettyTable

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'

TICKETS_TABLE_HEADER = ["车次", "出发站", "到达站", "出发时间", "到达时间", "历时", "商务座", "特等座",
                        "一等座", "二等座", "软卧", "硬卧", "软座", "硬座", "无座"]


def fetch_train_tickets(from_station, to_station, date=None):
    if date is None:
        date = str(datetime.now()).split(' ')[0]
    from_station_key = get_station_key(from_station)
    to_station_key = get_station_key(to_station)
    fetch_url = URL.format(date=date, from_station_key=from_station_key, to_station_key=to_station_key)
    # train_tickets = fetch_trains.TrainTickets(fetch_url)
    # tickets_result = train_tickets.fetch_tickets()
    with open('./data/tickets_data.json', encoding="utf-8") as f:
        tickets_result = json.loads(f.read())
    print_train_tickets(tickets_result)


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


def print_train_tickets(tickets_result):
    tickets_table = PrettyTable(TICKETS_TABLE_HEADER)
    for ticket_dict in tickets_result['data']:
        ticket_data = ticket_dict["queryLeftNewDTO"]
        tickets_table_row = [
            ticket_data['station_train_code'], print_cyan_font(ticket_data["from_station_name"]),
            print_cyan_font(ticket_data["end_station_name"]),
            ticket_data["start_time"], ticket_data["arrive_time"],
            ticket_data["lishi"], print_cyan_back(ticket_data["swz_num"]),
            ticket_data["tz_num"], ticket_data["zy_num"], ticket_data["ze_num"], ticket_data["rw_num"],
            ticket_data["yw_num"], ticket_data["rz_num"], ticket_data["yz_num"], ticket_data["wz_num"]
        ]
        tickets_table.add_row(tickets_table_row)
        del tickets_table_row
    print(tickets_table)


def print_cyan_font(text):
    return Fore.CYAN + text + Fore.RESET


def print_cyan_back(text):
    if text != "--" and text != "无":
        text = Back.CYAN + Fore.WHITE + text + Back.RESET
    return text
