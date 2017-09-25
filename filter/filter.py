#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from condition import ConditionFactory

class Filter:

    def __init__(self, conditions):
        self._conditions = conditions
        self._failed_infos = []
        self._passed_ids = []

    def can_pass(self, stock_id):
        for j in self._conditions:
            if not j.can_pass(stock_id):
                self._failed_infos.append({"id" : stock_id, "condition": j.id()})
                return False
        self._passed_ids.append(stock_id)
        return True

    def to_json(self):
        filter = dict()
        conditions = []
        conditions.append(json.loads(c.to_json() for c in self._conditions))
        filter['conditions'] = conditions
        return json.dumps(filter)

    @staticmethod
    def from_json(json_str):
        filter_dict = json.loads(json_str)
        conditions_value = filter_dict['conditions']
        conditions_object = []
        for c in conditions_value:
            conditions_object.append(ConditionFactory.from_json(json.dumps(c)))
        return Filter(conditions_object)

    def print_result(self):
        for f in self._failed_infos:
            print("stock id: {0}, failed in condition: {1}.\n".format(f['id'], f['condition']))
        for p in self._passed_ids:
            print("stock id: {0} passed all conditions.\n".format(p))
