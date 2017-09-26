#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from basic_type import ComparisionOperator, ConditionType
from stock_index import IndexValueFactory


class Condition:

    def __init__(self, id):
        self._id = id

    def can_pass(self, stock_id):
        return False

    def id(self):
        return self._id

    def to_json(self):
        pass


class ConstantCondition(Condition):

    def __init__(self, id, i_value, operator, c_value):
        super(ConstantCondition, self).__init__(id)
        self._i_value = i_value
        self._operator = operator
        self._c_value = c_value

    def can_pass(self, stock_id):
        delta = self._i_value.value(stock_id) - self._c_value
        if self._operator == ComparisionOperator.GREATER:
            return True if delta > 0 else False
        else:
            return True if delta <= 0 else False

    def to_json(self):
        condition = dict()
        condition['id'] = self._id
        condition['type'] = ConditionType.INDEX_TO_CONST.name
        condition['index_value'] = json.loads(self._i_value.to_json())
        condition['operator'] = self._operator.name
        condition['const_value'] = self._c_value
        return json.dumps(condition)

    @staticmethod
    def from_json(json_str):
        condition = json.loads(json_str)
        return ConstantCondition(condition['id'],
                                 IndexValueFactory.from_json(json.dumps(condition['index_value'])),
                                 ComparisionOperator[condition['operator']],
                                 condition['const_value'])


class IndexValueCondition(Condition):

    def __init__(self, id, value_1, operator, value_2):
        super(IndexValueCondition, self).__init__(id)
        self._value_1 = value_1
        self._value_2 = value_2
        self._operator = operator

    def can_pass(self, stock_id):
        delta = self._value_1.value(stock_id) - self._value_2.value(stock_id)
        if self._operator == ComparisionOperator.GREATER:
            return True if delta > 0 else False
        else:
            return True if delta <= 0 else False

    def to_json(self):
        condition = dict()
        condition['id'] = self._id
        condition['type'] = ConditionType.INDEX_TO_INDEX.name
        condition['value_1'] = json.loads(self._value_1.to_json())
        condition['operator'] = self._operator.name
        condition['value_2'] = json.loads(self._value_2.to_json())
        return json.dumps(condition)

    @staticmethod
    def from_json(json_str):
        condition = json.loads(json_str)
        return IndexValueCondition(condition['id'],
                                   IndexValueFactory.from_json(json.dumps(condition['value_1'])),
                                   ComparisionOperator[condition['operator']],
                                   IndexValueFactory.from_json(json.dumps(condition['value_2'])))


class ConditionFactory:

    @staticmethod
    def from_json(json_str):
        condition = json.loads(json_str)
        if condition['type'] == ConditionType.INDEX_TO_INDEX.name:
            return IndexValueCondition.from_json(json_str)
        elif condition['type'] == ConditionType.INDEX_TO_CONST.name:
            return ConstantCondition.from_json(json_str)
        else:
            return None




