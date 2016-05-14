import unittest
from datetime import datetime
from recommend import SimplePredictor


class TestSimplePredictor(unittest.TestCase):
    def test_predict(self):
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        pred = SimplePredictor(data)
        res = pred.predict()
        res1 = pred.predict(current_date=datetime(2015, 2, 9, 13, 0, 0))
        res2 = pred.predict(current_date=datetime(2015, 2, 15, 21, 0, 0))
        res3 = pred.predict(current_date=datetime(2015, 2, 14, 19, 0, 0))
        self.assertEqual(res, {"item1": 0.0})
        self.assertEqual(res1, {"item1": 0.33})
        self.assertEqual(res2, {"item1": 0.33})
        self.assertEqual(res3, {"item1": 0.33})

