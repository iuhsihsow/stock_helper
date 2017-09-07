import tushare as ts
from pandas import Series, DataFrame
import pandas as pd
import datetime
from tushare_utils.datetime_utils import DateTimeUtils


class StockInstance:

    def __init__(self, code):
        self._code = code

    def get_current_day_gain(self):
        today = DateTimeUtils.bygone_day(1)
        str_today = DateTimeUtils.date_to_string(today)
        five_days_ago = DateTimeUtils.bygone_day(5, today)
        str_five_days_ago =DateTimeUtils.date_to_string(five_days_ago)
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
        delta = (close.values[0] - open.values[0]) / open.values[0] * 100.0
        return delta

    def is_increase(self, duration=5):
        today = DateTimeUtils.bygone_day(1)
        str_today = DateTimeUtils.date_to_string(today)
        bygone_days = today - datetime.timedelta(days=duration)
        str_bygone_days= bygone_days.strftime('%Y-%m-%d')
        rlt = ts.get_k_data(self._code, start=str_bygone_days, end=str_today)
        volumes = rlt['volume']
        always_increase = True
        for i in range(0, duration - 1):
            if volumes.values[i] - volumes.values[i + 1] < 0:
                always_increase = False
                break
        return always_increase

    def v_ma(self, duration, start=None):
        today = start if start is not None else DateTimeUtils.bygone_day(1)
        str_today = DateTimeUtils.date_to_string(today)
        bygone_days = DateTimeUtils.bygone_day(duration, today)
        str_bygone_days = DateTimeUtils.date_to_string(bygone_days)
        rlt = ts.get_k_data(self._code, start=str_bygone_days, end=str_today)
        return rlt['volume'].mean()

    def ma_5_10_20(self, start=None):
        today = start if start is not None else DateTimeUtils.bygone_day(1)
        str_today = DateTimeUtils.date_to_string(today)
        bygone_days = DateTimeUtils.bygone_day(5, today)
        str_bygone_days = DateTimeUtils.date_to_string(bygone_days)
        rlt = ts.get_hist_data(self._code, start=str_bygone_days, end=str_today)
        ma5 = rlt['ma5'].values[0]
        ma10 = rlt['ma10'].values[0]
        ma20 = rlt['ma20'].values[0]
        return ma5, ma10, ma20

    def change(self, duration, start=None):
        start, end = DateTimeUtils.start_end_date(duration, DateTimeUtils.bygone_day(1))
        rlt = ts.get_k_data(self._code, start, end)
        max = rlt['high'].max()
        min = rlt['low'].min()
        return (max - min) / min * 100.0

    def close(self, date=None):
        start, end = DateTimeUtils.start_end_date(5, DateTimeUtils.bygone_day(1) if date is None else date)
        rlt = ts.get_k_data(self._code, start, end)
        return rlt['close'].values[0]

    def max(self, duration, start=None):
        start, end = DateTimeUtils.start_end_date(30)
        rlt = ts.get_k_data(self._code, start, end)
        return rlt['high'].max()


if __name__ == '__main__':
    stock = StockInstance('600848')
#    if stock.get_current_day_gain() > 4:
#        print(u"当日收盘涨幅大于4%")

#    if stock.is_increase(5):
#        print(u"过去5日成交量递增")

#    if stock.v_ma(5) > stock.v_ma(30):
#        print(u"近5日的平均成交量超过前30日的平均成交量")

#    ma5, ma10, ma20 = stock.ma_5_10_20()
#    if ma5 > ma10 and ma10 > ma20:
#        print(u"5日均价 > 10日均价 > 20日均价 > 60日均价")

#    if stock.change(1000) > 300:
#        print(u"过去1000天最高最低价相差不超过300%")

    if stock.close() > stock.max(30):
        print(u"当日的收盘价高于过去30日内的最高价")
