#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from basic_type import IndexType
from tushare_utils.stock_utils import StockInstance
from common.datetime_utils import DateTimeUtils


class IndexValue:

    def __init__(self, type, end, duration):
        self._end = end
        self._duration = duration
        self._type = type

    def value(self, stock_id):
        pass

    def to_json(self):
        value_dict = {
            "type": self._type.name,
            "start": DateTimeUtils.date_to_string(self._end),
            "duration": self._duration}
        return json.dumps(value_dict)


class CloseIncreaseValue(IndexValue):

    def __init__(self, type, end, duration):
        super(CloseIncreaseValue, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).get_current_day_gain()


class AvgPriceValue(IndexValue):

    def __init__(self, type, end, duration):
        super(AvgPriceValue, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).ma_5_10_20(self._end)[0]


class AvgVolumeValue(IndexValue):

    def __init__(self, type, end, duration):
        super(AvgVolumeValue, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).v_ma(self._duration, self._end)


class MaxPriceCloseValue(IndexValue):

    def __init__(self, type, end, duration):
        super(MaxPriceCloseValue, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).max(self._duration, self._end)


class MinPriceCloseValue(IndexValue):

    def __init__(self, type, end, duration):
        super(MinPriceCloseValue, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).min(self._duration, self._end)


class PriceDifference(IndexValue):

    def __init__(self, type, end, duration):
        super(PriceDifference, self).__init__(type, end, duration)

    def value(self, stock_id):
        return StockInstance(stock_id).change(self._duration, self._end)


class IndexValueFactory:

    @staticmethod
    def create(index_type, start, duration):
        if index_type == IndexType.CLOSE_INCREASE.name or index_type == IndexType.CLOSE_INCREASE:
            return CloseIncreaseValue(IndexType[index_type], start, duration)
        elif index_type == IndexType.AVG.name or index_type == IndexType.AVG:
            return AvgPriceValue(IndexType[index_type], start, duration)
        elif index_type == IndexType.V_AVG.name or index_type == IndexType.V_AVG:
            return AvgVolumeValue(IndexType[index_type], start, duration)
        elif index_type == IndexType.MAX.name or index_type == IndexType:
            return MaxPriceCloseValue(IndexType[index_type], start, duration)
        elif index_type == IndexType.MIN.name or index_type == IndexType.MIN:
            return MinPriceCloseValue(IndexType[index_type],start, duration)
        elif index_type == IndexType.P_DIFF.name or index_type == IndexType.P_DIFF:
            return PriceDifference(IndexType[index_type],start, duration)
        else:
            return None

    @staticmethod
    def from_json(json_str):
        value = json.loads(json_str)
        return IndexValueFactory.create(
            value['type'],
            DateTimeUtils.date_from_string(value['start']),
            value['duration'])



