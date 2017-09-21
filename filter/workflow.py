#!/usr/bin/env python
# -*- coding: utf-8 -*-
from connector import InputConnector
from stock_index import IndexValueFactory
from basic_type import IndexType, ComparisionOperator
from common import DateTimeUtils
from condition import ConstantCondition, IndexValueCondition
from filter import Filter
import json

class WorkFlow:

    def __init__(self, inputs, filter):
        self._inputs = inputs
        self._filter = filter

    @staticmethod
    def from_json(self, json_str):
        workflow = json.loads(json_str)
        _inputs = workflow['stock_ids']
        _filter = workflow['filter']
        return WorkFlow(_inputs, _filter)

    def to_json(self):
        workflow = dict()
        workflow['stock_ids'] = self._inputs
        workflow['filter'] = self._filter.to_json()
        return json.dumps(workflow)

if __name__ == '__main__':
    # inputs
    stock_ids = ['600848']

    # conditions
    conditions = []

    current_close = IndexValueFactory.create(IndexType.CLOSE_INCREASE, DateTimeUtils.today(), 0)
    c_value = 0.04

    condition = ConstantCondition(len(conditions), current_close, ComparisionOperator.GREATER, c_value)
    conditions.append(condition)

    con_filter = Filter(conditions)
    passed_ids = []
    for s in stock_ids:
        if con_filter.can_pass(s):
            passed_ids.append(s)

    con_filter.print_result()
