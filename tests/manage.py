#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

if __name__ == "__main__":
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
