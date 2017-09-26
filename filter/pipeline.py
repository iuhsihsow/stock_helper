#!/usr/bin/env python
# -*- coding: utf-8 -*-
from connector import InputConnector
from stock_index import IndexValueFactory
from basic_type import IndexType, ComparisionOperator
from common import DateTimeUtils
from condition import ConstantCondition, IndexValueCondition
from filter import Filter
import json


class Pipeline:

    def __init__(self, inputs, filter):
        self._inputs = inputs
        self._filter = filter
        self._outputs = []

    @staticmethod
    def from_json(json_str):
        workflow = json.loads(json_str)
        _inputs = workflow['stock_ids']
        _filter = Filter.from_json(json.dumps(workflow['filter']))
        return Pipeline(_inputs, _filter)

    def to_json(self):
        workflow = dict()
        workflow['stock_ids'] = self._inputs
        workflow['filter'] = json.loads(self._filter.to_json())
        return json.dumps(workflow)

    def run(self):
        for s in self._inputs:
            if self._filter.can_pass(s):
                self._outputs.append(s)
        self._filter.print_result()


if __name__ == '__main__':
    # inputs
    stock_ids = ['600848']

    # conditions
    conditions = []

    current_close = IndexValueFactory.create(IndexType.CLOSE_INCREASE, DateTimeUtils.today(), 0)
    c_value = 0.04

    condition = ConstantCondition(len(conditions), current_close, ComparisionOperator.GREATER, c_value)
    conditions.append(condition)

    v_avg_5 = IndexValueFactory.create(IndexType.V_AVG, DateTimeUtils.date_from_string('2017-9-1'), 5)
    v_avg_10 = IndexValueFactory.create(IndexType.V_AVG, DateTimeUtils.date_from_string('2017-9-1'), 10)
    cond2 = IndexValueCondition(len(conditions), v_avg_5, ComparisionOperator.GREATER, v_avg_10)
    conditions.append(cond2)

    con_filter = Filter(conditions)

    pipeline = Pipeline(stock_ids, con_filter)
    json_pipeline = pipeline.to_json()
    print(json_pipeline)

    pipeline_copy = Pipeline.from_json(json_pipeline)
    pipeline_copy.run()

