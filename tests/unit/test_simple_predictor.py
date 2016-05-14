import unittest
from datetime import datetime
from dateutil.parser import parse
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

    def test_predict_unsorted(self):
        data = {
            "item1": [
                parse("2016-05-04T18:29:51.7340000Z"),
                parse("2016-05-08T18:29:55.6010000Z"),
                parse("2016-05-10T18:29:58.9250000Z"),
                parse("2016-05-12T18:30:02.4870000Z"),
                parse("2016-05-02T18:30:05.9970000Z"),
                parse("2016-05-06T18:36:29.1080000Z")
            ]
        }
        pred = SimplePredictor(data)
        res = pred.predict()
        res1 = pred.predict(current_date=datetime(2016, 5, 13, 13, 0, 0))
        self.assertEqual(res, {"item1": 1.0})
        self.assertEqual(res1, {"item1": 0.0})

