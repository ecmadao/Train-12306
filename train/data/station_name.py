# -*- coding: utf-8 -*-
import re
from .const_value import STATION_NAMES


def station_name():
    data_upper = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', STATION_NAMES)
    data_lower = re.findall(u'@([a-z]+)\|([\u4e00-\u9fa5]+)', STATION_NAMES)
    return dict(data_upper), dict(data_lower)
