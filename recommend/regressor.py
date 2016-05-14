"""
This module contains simple linear Regressor implementation
"""
import math
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from .utils import reduce_dates, prepare_date


class Regressor:
    def __init__(self):
        self._items = {}
        self._lin_reg = LinearRegression()

    def fit(self, data):
        """
        Fit prediction algorithm

        :param data: dict, a dictionary with data, example:
        {"item 1": [date1, date2, date3], "item2": [date3, date4]}
        :return: linear regressor
        """
        _pd = prepare_date
        for item, dates in data.items():
            if len(dates) < 3:
                continue
            lin_reg = LinearRegression()

            dates = sorted(dates)
            date_deltas = reduce_dates(dates)
            target = np.array(date_deltas)
            features = np.array(list(range(len(target)))).reshape(len(date_deltas), 1)
            lin_reg.fit(features, target)
            self._items[item] = {
                'regressor': lin_reg,
                'last_val': features[-1],
                'latest_date': _pd(max(dates))
            }

    def predict(self, current_date=None):
        """
        Predict recommendation for the current day

        :return: dict with probabilities of items in form of
        {"item1": 0.8, "item2": 0.3}
        """
        _pd = prepare_date
        if current_date is None:
            current_date = datetime.now()
        current_date = prepare_date(current_date)

        res = {}
        for item, item_data in self._items.items():
            pred_val = item_data['last_val'] + 1
            next_interval = item_data['regressor'].predict([pred_val])[0]
            low_int, high_int, dec_part = (
                math.floor(next_interval),
                math.ceil(next_interval),
                round(np.modf(next_interval)[0], 2)
            )
            low_date = _pd(item_data['latest_date'] + timedelta(low_int))
            high_date = _pd(item_data['latest_date'] + timedelta(high_int))
            low_prob = round(1.0 - dec_part, 2)
            if current_date == low_date:
                res[item] = low_prob
            elif current_date == high_date:
                res[item] = dec_part
            else:
                res[item] = 0.0

        return res
