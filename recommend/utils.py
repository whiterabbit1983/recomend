def prepare_date(date):
    """
    Set hours, minutes and seconds of a datetime object to zero
    """
    return date.replace(hour=0, minute=0, second=0, microsecond=0)


def reduce_dates(dates_list):
    """
    Reduces a list of dates and returns a list
    of days between those dates
    :param dates_list: list of datetime
    :return: list of int
    """
    _pd = prepare_date
    if len(dates_list) <= 1:
        return []
    res = []
    for i in range(len(dates_list)):
        if i == 0:
            continue
        d1 = _pd(dates_list[i])
        d2 = _pd(dates_list[i - 1])
        res.append((d1 - d2).days)
    return res


def calc_probs(values):
    """
    Calculates 'probability' of each value in the list, relative to
    list length
    :param values: list
    :return:
    """
    denom = len(values)
    res = {}
    if not denom:
        return res

    vals_set = set(values)
    for val in vals_set:
        res[val] = round(values.count(val)/denom, 2)

    return res
