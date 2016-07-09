# -*- coding: utf-8 -*-
import re


def station_name():
    with open(r'./train/data/station_name.js', encoding="utf-8") as f:
        result = f.read()
    data_upper = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', result)
    data_lower = re.findall(u'@([a-z]+)\|([\u4e00-\u9fa5]+)', result)
    return dict(data_upper), dict(data_lower)
