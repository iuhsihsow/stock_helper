#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum


class ComparisionOperator(Enum):
    GREATER = 1
    LESS = 2
    EQUAL = 3


class IndexType(Enum):
    CLOSE_INCREASE = 1
    AVG = 2
    V_AVG = 3
    MAX = 4
    MIN = 5
    P_DIFF = 7