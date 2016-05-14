"""
This module contains simple predictor based on frequency
"""


from datetime import timedelta, datetime
from .utils import reduce_dates, calc_probs, prepare_date


class SimplePredictor:
    def __init__(self, data):
        self._data = data

    def predict(self, current_date=None):
        _pd = prepare_date
        if current_date is None:
            current_date = datetime.now()
        current_date = prepare_date(current_date)
        res = {}
        for item, dates in self._data.items():
            dates = sorted(dates)
            date_intervals = reduce_dates(dates)
            latest_date = max(dates)
            probs = calc_probs(date_intervals)
            future_dates = {_pd(latest_date + timedelta(d)): p for d, p in probs.items()}
            res[item] = future_dates.get(current_date, 0.0)
        return res
