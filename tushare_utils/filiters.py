import tushare as ts
from pandas import Series, DataFrame
import pandas as pd
import datetime


class StockInstance:


    def __init__(self, code):
        self._code = code

    def get_current_day_gain(self):
        today = datetime.date.today() - datetime.timedelta(days=1)
        str_today = today.strftime('%Y-%m-%d')
        five_days_ago = today - datetime.timedelta(days=5)
        str_five_days_ago = five_days_ago.strftime('%Y-%m-%d')
        rlt = ts.get_k_data(self._code, start=str_five_days_ago,end=str_today)
        # print(rlt)
        #            date   open  close   high    low    volume    code
        # 159  2017-08-28  23.45  23.50  23.70  23.05  119146.0  600848
        # 160  2017-08-29  23.45  23.06  23.85  23.04   90952.0  600848
        # 161  2017-08-30  23.25  24.15  24.60  23.21  196509.0  600848
        # 162  2017-08-31  24.16  25.62  25.88  23.78  259406.0  600848
        latest = rlt[-1:]
        open = latest['open']
        close = latest['close']
        delta = (close._values[0]  - open._values[0]) / open._values[0] * 100.0
        return delta

    def is_increase(self, days=5):
        today = datetime.date.today() - datetime.timedelta(days=1)
        str_today = today.strftime('%Y-%m-%d')
        bygone_days = today - datetime.timedelta(days=days)
        str_bygone_days= bygone_days.strftime('%Y-%m-%d')
        rlt = ts.get_k_data(self._code, start=str_bygone_days, end=str_today)
        volumes = rlt['volume']
        always_increase = True
        for i in range(0, days - 1):
            if volumes._values[i + 1] - volumes._values[i] < 0:
                always_increase = False
                break
        return always_increase









stock = StockInstance('600848')
if stock.get_current_day_gain() > 4:
    print(u"当日收盘涨幅大于4%")

if stock.is_increase(5):
    print(u"过去5日成交量递增")


