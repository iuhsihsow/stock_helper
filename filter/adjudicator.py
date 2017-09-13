#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .basic_type import ComparisionOperator


class Adjudicator:

    def __init__(self, id):
        self._id = id

    def can_pass(self, stock_id):
        return False


class ConstantAdjudicator(Adjudicator):

    def __init__(self, id, i_value, operator, c_value):
        super(ConstantAdjudicator, self).__init__(id)
        self._i_value = i_value
        self._operator = operator
        self._c_value = c_value

    def can_pass(self, stock_id):
        delta = self._i_value.value(stock_id) - self._c_value
        if self._operator == ComparisionOperator.GREATER:
            return True if delta > 0 else False
        else:
            return True if delta <= 0 else False


class IndexValueAdjudicator(Adjudicator):

    def __init__(self, id, value_1, operator, value_2):
        super(IndexValueAdjudicator, self).__init__(id)
        self._value_1 = value_1
        self._value_2 = value_2
        self._operator = operator

    def can_pass(self, stock_id):
        delta = self._value_1.value(stock_id) - self._value_2.value(stock_id)
        if self._operator == ComparisionOperator.GREATER:
            return True if delta > 0 else False
        else:
            return True if delta <= 0 else False


