import unittest
from datetime import datetime
from recommend import Regressor


class TestRegressor(unittest.TestCase):
    def test_fit(self):
        reg = Regressor()
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        reg.fit(data)
        self.assertEqual(reg._items['item1']['last_val'], 2)
        self.assertEqual(reg._items['item1']['latest_date'], datetime(2015, 2, 5, 0, 0))
        lin_reg = reg._items['item1']['regressor']
        self.assertAlmostEqual(lin_reg.coef_[0], 2.5)
        self.assertAlmostEqual(lin_reg.intercept_, 5.17, places=2)

    def test_predict(self):
        reg = Regressor()
        data = {
            "item1": [
                datetime(2015, 1, 13, 12, 0, 0),
                datetime(2015, 1, 17, 19, 3, 0),
                datetime(2015, 1, 27, 13, 0, 0),
                datetime(2015, 2, 5, 12, 0, 0)
            ]
        }
        reg.fit(data)
        res = reg.predict()
        res1 = reg.predict(current_date=datetime(2015, 2, 17, 12, 0, 0))
        res2 = reg.predict(current_date=datetime(2015, 2, 18, 12, 0, 0))
        self.assertEqual(res, {"item1": 0.0})
        self.assertEqual(res1, {"item1": 0.33})
        self.assertEqual(res2, {"item1": 0.67})

    def test_predict_2(self):
        reg = Regressor()
        data = {
            "item1": [
                datetime(2016, 5, 2, 12, 0, 0),
                datetime(2016, 5, 4, 19, 3, 0),
                datetime(2016, 5, 6, 13, 0, 0),
                datetime(2016, 5, 8, 12, 0, 0),
                datetime(2016, 5, 10, 12, 0, 0),
                datetime(2016, 5, 12, 12, 0, 0)
            ]
        }
        reg.fit(data)
        res = reg.predict()
        res1 = reg.predict(current_date=datetime(2016, 5, 13, 12, 0, 0))
        self.assertEqual(res, {"item1": 1.0})
        self.assertEqual(res1, {"item1": 0.0})
