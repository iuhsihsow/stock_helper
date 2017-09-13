#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Filter:

    def __init__(self, adjudicators):
        self._adjudicators = adjudicators

    def can_pass(self, stock_id):
        for j in self._adjudicators:
            if not j.can_pass(stock_id):
                return False
        return True
