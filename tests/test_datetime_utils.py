#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from common.datetime_utils import DateTimeUtils


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self._str_start = '2017-8-29'
        self._str_end = '2017-9-1'
        self._duration = 3

    def test_date_and_string(self):
        today = DateTimeUtils.today()
        self.assertFalse(today is None)

        str_today = DateTimeUtils.date_to_string(today)
        self.assertFalse(str_today is None)

        today_cp = DateTimeUtils.date_from_string(str_today)
        self.assertEquals(DateTimeUtils.date_to_string(today), DateTimeUtils.date_to_string(today_cp))

    def test_bygone_day(self):
        str_test_date = self._str_end
        test_date = DateTimeUtils.date_from_string(str_test_date)
        three_day_before_test_date = DateTimeUtils.bygone_day(3, test_date)
        str_three_day_before_test_date = DateTimeUtils.date_to_string(three_day_before_test_date)
        self.assertEquals(str_three_day_before_test_date,
                          DateTimeUtils.date_to_string(DateTimeUtils.date_from_string(self._str_start)))

    def test_start_end_date(self):
        end_date = DateTimeUtils.date_from_string(self._str_end)
        start_date = DateTimeUtils.date_from_string(self._str_start)
        str_start, str_end = DateTimeUtils.start_end_date(3, end_date)
        self.assertEquals(DateTimeUtils.date_to_string(start_date), str_start)
        self.assertEquals(DateTimeUtils.date_to_string(end_date), str_end)



