#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from basic_type import IndexType
from tushare_utils.stock_utils import StockInstance


class IndexValue:

    def __init__(self, type, start, duration):
        self._start = start
        self._duration = duration
        self._type = type

    def value(self, stock_id):
        pass

    def to_json(self):
        return json.dumps({"type":self._type, "start": self._start, "duration":self._duration})


class CloseIncreaseValue(IndexValue):

    def __init__(self, type, start, duration):
        super(CloseIncreaseValue, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).get_current_day_gain()


class AvgPriceValue(IndexValue):

    def __init__(self, type, start, duration):
        super(AvgPriceValue, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).ma_5_10_20(self._start)[0]


class AvgVolumeValue(IndexValue):

    def __init__(self,type, start, duration):
        super(AvgVolumeValue, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).v_ma(self._duration, self._start)


class MaxPriceCloseValue(IndexValue):

    def __init__(self, type, start, duration):
        super(MaxPriceCloseValue, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).max(self._duration, self._start)


class MinPriceCloseValue(IndexValue):

    def __init__(self, type, start, duration):
        super(MinPriceCloseValue, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).min(self._duration, self._start)


class PriceDifference(IndexValue):

    def __init__(self, type, start, duration):
        super(PriceDifference, self).__init__(type, start, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).change(self._duration, self._start)


class IndexValueFactory:

    @staticmethod
    def create(index_type, start, duration):
        if index_type == IndexType.CLOSE_INCREASE:
            return CloseIncreaseValue(index_type, start, duration)
        elif index_type == IndexType.AVG:
            return AvgPriceValue(index_type, start, duration)
        elif index_type == IndexType.V_AVG:
            return AvgVolumeValue(index_type, start, duration)
        elif index_type == IndexType.MAX:
            return MaxPriceCloseValue(index_type, start, duration)
        elif index_type == IndexType.MIN:
            return MinPriceCloseValue(index_type,start, duration)
        elif index_type == IndexType.P_DIFF:
            return PriceDifference(index_type,start, duration)
        else:
            return None

    @staticmethod
    def from_json(json_str):
        value = json.loads(json_str)
        return IndexValueFactory.create(value['type'], value['start'], value['duration'])



