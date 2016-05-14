import unittest
from datetime import datetime
from recommend.utils import reduce_dates, calc_probs


class TestUtils(unittest.TestCase):
    def test_reduce_dates_empty_list_or_has_one_item(self):
        res = reduce_dates([])
        res1 = reduce_dates([datetime(2015, 1, 13, 12, 0, 0)])
        self.assertEqual(res, [])
        self.assertEqual(res1, [])

    def test_reduce_dates_not_empty_list(self):
        dates = [
            datetime(2015, 1, 13, 12, 0, 0),
            datetime(2015, 1, 17, 19, 3, 0),
            datetime(2015, 1, 27, 13, 0, 0),
            datetime(2015, 2, 5, 12, 0, 0),
        ]
        res = reduce_dates(dates)
        self.assertEqual(res, [4, 10, 9])

    def test_calc_probs(self):
        res1 = calc_probs([])
        res2 = calc_probs([1, 1, 2, 3, 3, 3, 4, 5, 5])
        self.assertEqual(res1, {})
        self.assertEqual(
            res2,
            {1: 0.22, 2: 0.11, 3: 0.33, 4: 0.11, 5: 0.22}
        )
