#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Connector:

    def __init__(self, stock_ids):
        self.stock_ids = []


class InputConnector(Connector):

    def __init__(self, stock_ids):
        super(InputConnector, self).__init__(self)


class OutputConnector(Connector):

    def __init__(self, stock_ids):
        super(OutputConnector, self).__init__(self)

