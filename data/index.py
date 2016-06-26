from datetime import datetime
import json
from colorama import Fore
from spider import fetch_trains
from prettytable import PrettyTable
from utils import tickets_util, common_util

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'

TICKETS_TABLE_HEADER = ["车次", "站点", "起止时间", "历时", "商务座", "特等座",
                        "一等座", "二等座", "软卧", "硬卧", "软座", "硬座", "无座"]


def fetch_train_tickets(from_station, to_station, train_type, date=None):
    """get input data and print final result

    :param train_type
    :param from_station
    :param to_station
    :param date
    :return: if data is invalidate then return False
    """
    if date is None:
        date = str(datetime.now().date())
    else:
        date = tickets_util.validate_date(date)
        if not isinstance(date, str):
            print(common_util.make_colorful_font(date['message'], Fore.RED))
            return date['result']
    from_station_key = tickets_util.get_station_key(from_station)
    to_station_key = tickets_util.get_station_key(to_station)

    fetch_url = URL.format(date=date, from_station_key=from_station_key, to_station_key=to_station_key)
    train_tickets = fetch_trains.TrainTickets(fetch_url)
    tickets_result = train_tickets.fetch_tickets()

    # with open('./data/tickets_data.json', encoding="utf-8") as f:
    #     tickets_result = json.loads(f.read())

    if tickets_result['status']:
        print_train_tickets(tickets_result, train_type)
    else:
        print(common_util.make_colorful_font(tickets_result['data'], Fore.RED))


def print_train_tickets(tickets_result, train_type):
    """make and print a table

    :param train_type
    :param tickets_result: fetched result
    :return: None
    """
    t_type = None
    for item in train_type.items():
        t_type, t_type_value = item
        if t_type_value:
            break
        else:
            t_type = None

    if t_type is not None:
        target_train = tickets_util.filter_target_train(t_type)
        tickets_result_data = filter(target_train, tickets_result['data'])
    else:
        tickets_result_data = tickets_result['data']

    tickets_table = PrettyTable(TICKETS_TABLE_HEADER)
    for ticket_dict in tickets_result_data:
        ticket_data = ticket_dict["queryLeftNewDTO"]
        tickets_table_row = [
            ticket_data["station_train_code"],
            '{}\n{}'.format(common_util.make_colorful_font(ticket_data["from_station_name"]),
                            common_util.make_colorful_font(ticket_data["end_station_name"])),
            '{}\n{}'.format(ticket_data["start_time"], ticket_data["arrive_time"]),
            ticket_data["lishi"],
            tickets_util.handle_font_color(ticket_data["swz_num"]),
            tickets_util.handle_font_color(ticket_data["tz_num"]),
            tickets_util.handle_font_color(ticket_data["zy_num"]),
            tickets_util.handle_font_color(ticket_data["ze_num"]),
            tickets_util.handle_font_color(ticket_data["rw_num"]),
            tickets_util.handle_font_color(ticket_data["yw_num"]),
            tickets_util.handle_font_color(ticket_data["rz_num"]),
            tickets_util.handle_font_color(ticket_data["yz_num"]),
            tickets_util.handle_font_color(ticket_data["wz_num"])
        ]
        tickets_table.add_row(tickets_table_row)
        del tickets_table_row
    print(tickets_table)

