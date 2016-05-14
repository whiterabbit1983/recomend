import unittest
from datetime import datetime
from recommend import predict


class TestToplevel(unittest.TestCase):
    def test_regressor_algo(self):
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        res = predict(data, algo='regressor')
        res1 = predict(data, algo='regressor', current_date=datetime(2015, 2, 17, 12, 0, 0))
        res2 = predict(data, algo='regressor', current_date=datetime(2015, 2, 18, 12, 0, 0))
        self.assertEqual(res, {"item1": 0.0})
        self.assertEqual(res1, {"item1": 0.33})
        self.assertEqual(res2, {"item1": 0.67})

    def test_predictor_algo(self):
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        res = predict(data, algo='simple_predictor')
        res1 = predict(data, algo='simple_predictor', current_date=datetime(2015, 2, 9, 13, 0, 0))
        res2 = predict(data, algo='simple_predictor', current_date=datetime(2015, 2, 15, 21, 0, 0))
        res3 = predict(data, algo='simple_predictor', current_date=datetime(2015, 2, 14, 19, 0, 0))
        self.assertEqual(res, {"item1": 0.0})
        self.assertEqual(res1, {"item1": 0.33})
        self.assertEqual(res2, {"item1": 0.33})
        self.assertEqual(res3, {"item1": 0.33})

    def test_wrong_algo(self):
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        res = predict(data, algo='wrong')
        self.assertEqual(res, {'error': "No such algorithm: wrong"})
