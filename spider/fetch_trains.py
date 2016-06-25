#!/usr/bin/env python
"""

"""

from urllib import request, error
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class TrainTickets(object):
    """
    Attributes:
        response
        url
        headers
    Methods:
        fetch_tickets
    """
    __slots__ = ["response", "url", "headers"]

    def __init__(self, url):
        self.response = None
        self.url = url
        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
            'GET': url
        }

    def fetch_tickets(self):
        # req = request.Request(self.url, headers=self.headers)
        # response = request.urlopen(req).read().decode('UTF-8')
        # self.response = json.loads(response)
        # return self.output_result()
        return dict([('status', 0), ('data', 'Ops, there are some error...')])

    def output_result(self):
        status = self.response["status"]
        if str(status) == 'true':
            result_trains = dict([('status', 1), ('data', self.response["data"])])
        else:
            result_trains = dict([('status', 0), ('data', 'Ops, there are some error...')])
        return result_trains

