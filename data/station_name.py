# -*- coding: utf-8 -*-
import re


def station_name():
    with open(r'station_name.js', encoding="utf-8") as f:
        result = f.read()
    data = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', result)
    return dict(data)
