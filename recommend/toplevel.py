"""
This module contains toplevel functions
"""


from .regressor import Regressor, RFRegressor
from .simple_predictor import SimplePredictor


def _handle_regressor(data, current_date):
    reg = Regressor()
    reg.fit(data)
    return reg.predict(current_date=current_date)


def _handle_simple_predictor(data, current_date):
    return SimplePredictor(data).predict(current_date=current_date)


def _handle_random_forest(data, current_date):
    reg = Regressor()
    reg.fit(data)
    return reg.predict(current_date=current_date)


def predict(data, current_date=None, algo='regressor'):
    handler = globals().get("_handle_{}".format(algo), None)
    if handler is None:
        return {'error': "No such algorithm: {}".format(algo)}
    return handler(data, current_date)
