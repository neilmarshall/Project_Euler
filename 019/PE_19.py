import datetime

def count_sundays(first_day, last_day):
    """
    How many Sundays fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000)?
    
    >>> count_sundays(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))
    171
    """
    sunday_count = 0
    while first_day <= last_day:
        sunday_count += (first_day.day == 1 and first_day.weekday() == 6)
        first_day += datetime.timedelta(days=1)
    return sunday_count


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
