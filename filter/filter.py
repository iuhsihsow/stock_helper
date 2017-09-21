#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Filter:

    def __init__(self, conditions):
        self._conditions = conditions
        self._failed_infos = []
        self._passed_ids = []

    def can_pass(self, stock_id):
        for j in self._conditions:
            if not j.can_pass(stock_id):
                self._failed_infos.append({"id" : stock_id, "condition" : j.id()})
                return False
        self._passed_ids.append(stock_id)
        return True

    def to_json(self):
        filter = dict()
        conditions = []
        for c in self._conditions:
            c_json = c.to_json()
            conditions.append(json.loads(c_json))
        filter['conditions'] = conditions
        return json.dumps(filter)

    @staticmethod
    def from_json(self, json_str):
        filter = json.loads(json_str)
        conditions = filter['conditions']
        for c in conditions:
            self._conditions.append(c.from_json())
        pass

    def print_result(self):
        for f in self._failed_infos:
            print("stock id: {0}, failed in condition: {1}.\n".format(f['id'], f['condition']))
        for p in self._passed_ids:
            print("stock id: {0} passed all conditions.\n".format(p))
