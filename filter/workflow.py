#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .connector import InputConnector
from .stock_index import IndexValueFactory
from .basic_type import IndexType, ComparisionOperator
from ..common import DateTimeUtils
from .adjudicator import ConstantAdjudicator, IndexValueAdjudicator
from .filter import Filter

stock_ids = ['600848']
input = InputConnector(stock_ids)

judges = []
current_close = IndexValueFactory.create(IndexType.CLOSE, DateTimeUtils.today(), 0)
c_value = 0.04
judge = ConstantAdjudicator(len(judges), current_close, ComparisionOperator.GREATER, c_value)
judges.append(judge)

con_filter = Filter(judges)
passed_ids = []
for s in input.stock_ids:
    if con_filter.can_pass(s):
        passed_ids.append(s)
