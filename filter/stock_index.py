#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .basic_type import IndexType


class IndexValue:

    def __init__(self, start, duration):
        self._start = start
        self._duration = duration

    def value(self, stock_id):
        pass


class CloseIncreaseValue(IndexValue):

    def __init__(self, start, duration):
        super(CloseIncreaseValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class AvgPriceValue(IndexValue):

    def __init__(self, start, duration):
        super(AvgPriceValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class AvgVolumeValue(IndexValue):

    def __init__(self, start, duration):
        super(AvgVolumeValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class MaxPriceCloseValue(IndexValue):

    def __init__(self, start, duration):
        super(MaxPriceCloseValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class MinPriceCloseValue(IndexValue):

    def __init__(self, start, duration):
        super(MinPriceCloseValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class VolumeValue(IndexValue):

    def __init__(self, start, duration):
        super(VolumeValue, self).__init__(start, duration)

    def value(self, stock_id):
        pass


class IndexValueFactory:

    @staticmethod
    def create(index_type, start, duration):
        if index_type == IndexType.CLOSE_INCREASE:
            return CloseIncreaseValue(start, duration)
        elif index_type == IndexType.AVG:
            return AvgPriceValue(start, duration)
        elif index_type == IndexType.V_AVG:
            return AvgVolumeValue(start, duration)
        elif index_type == IndexType.MAX:
            return MaxPriceCloseValue(start, duration)
        elif index_type == IndexType.MIN:
            return MinPriceCloseValue(start, duration)
        elif index_type == IndexType.VOLUME:
            return VolumeValue(start, duration)
        else:
            return None



