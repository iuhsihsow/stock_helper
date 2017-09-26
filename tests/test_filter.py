import os, sys
import unittest

filter_folder = os.path.join(os.path.dirname(__file__), "../filter")
sys.path.insert(0, filter_folder)

from filter import Filter


class FilterTestCase(unittest.TestCase):

    def test_can_pass(self):
        pass

    def test_from_to_json(self):
        filter_json = "{\"conditions\": [{\"operator\": \"GREATER\", \"index_value\": {\"duration\": 0, \"start\": \"2017-09-26\", \"type\": \"CLOSE_INCREASE\"}, \"id\": 0, \"const_value\": 0.04, \"type\": \"INDEX_TO_CONST\"}, {\"operator\": \"GREATER\", \"value_1\": {\"duration\": 5, \"start\": \"2017-09-01\", \"type\": \"V_AVG\"}, \"value_2\": {\"duration\": 10, \"start\": \"2017-09-01\", \"type\": \"V_AVG\"}, \"id\": 1, \"type\": \"INDEX_TO_INDEX\"}]}"
        filter = Filter.from_json(filter_json)
        self.assertFalse(filter is None)
        filter_to_json = filter.to_json()
        str_output_json = "{\"conditions\": [{\"id\": 0, \"index_value\": {\"duration\": 0, \"start\": \"2017-09-26\", \"type\": \"CLOSE_INCREASE\"}, \"type\": \"INDEX_TO_CONST\", \"operator\": \"GREATER\", \"const_value\": 0.04}, {\"id\": 1, \"value_1\": {\"duration\": 5, \"start\": \"2017-09-01\", \"type\": \"V_AVG\"}, \"type\": \"INDEX_TO_INDEX\", \"value_2\": {\"duration\": 10, \"start\": \"2017-09-01\", \"type\": \"V_AVG\"}, \"operator\": \"GREATER\"}]}"
        self.assertEquals(filter_json, str_output_json)


if __name__ == '__main__':
    unittest.main()
