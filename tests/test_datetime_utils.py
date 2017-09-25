#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from common.datetime_utils import DateTimeUtils


class BasicsTestCase(unittest.TestCase):

    def test_date_and_string(self):
        today = DateTimeUtils.today()
        self.assertFalse(today is None)

        str_today = DateTimeUtils.date_to_string(today)
        self.assertFalse(str_today is None)

        today_cp = DateTimeUtils.date_from_string(str_today)
        self.assertEquals(DateTimeUtils.date_to_string(today), DateTimeUtils.date_to_string(today_cp))


