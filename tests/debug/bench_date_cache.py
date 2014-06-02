#!/usr/bin/env python

import datetime
import time
from collections import OrderedDict

date_format = '%d/%b/%Y:%H:%M:%S'

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s\t: %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def nocache():
    file = open("timestamps.log", 'r')
    for lineno, line in enumerate(file):
        date_string, timezone_string = line.split()

        date = datetime.datetime.strptime(date_string, date_format)
        timezone = float(timezone_string)

        date -= datetime.timedelta(hours=timezone/100)

@timing
def cache():
    cache_dates = OrderedDict()
    file = open("timestamps.log", 'r')
    for lineno, line in enumerate(file):
        date_string, timezone_string = line.split()
        key = line

        date = cache_dates.get(key)
        if not date:
            date = datetime.datetime.strptime(date_string, date_format)
            timezone = float(timezone_string)

            date -= datetime.timedelta(hours=timezone/100)
            cache_dates[key] = date

cache()
nocache()