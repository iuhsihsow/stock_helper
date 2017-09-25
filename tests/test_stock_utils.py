#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from tushare_utils.stock_utils import StockInstance


class BasicsTestCase(unittest.TestCase):

    def test_can_work(self):
        stock = StockInstance('600848')
        self.assertFalse(stock.get_current_day_gain() is None)
        self.assertFalse(stock.is_increase(5) is None)
        self.assertFalse(stock.v_ma(5) is None)
        self.assertFalse(stock.ma_5_10_20() is None)
        self.assertFalse(stock.close() is None)
        self.assertFalse(stock.max(5) is None)
