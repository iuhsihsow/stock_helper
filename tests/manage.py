#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
