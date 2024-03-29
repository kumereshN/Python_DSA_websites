from datetime import datetime

from dateutil.parser import parse

from math import floor

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


def get_number_books_read(books_per_year_goal: int,
                          at_date: str = None) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    at_date = at_date or str(NOW)
    # TODOs

    # 1. use dateutil's parse to convert at_date into a
    # datetime object
    at_date_datetime = parse(at_date)

    # 2. check books_per_year_goal and at_date and raise
    # a ValueError if goal <= 0 or at_date in the past (< NOW)
    if books_per_year_goal <= 0 or at_date_datetime < NOW:
        raise ValueError('Should have positive goal and future date')

    # 3. check the offset of at_date in the year ("week of the
    # year" - e.g. whatweekisit.com) and based on the books_per_year_goal,
    # calculate the number of books that should have been read / completed
    get_week = at_date_datetime.isocalendar()[1]
    return floor((get_week / WEEKS_PER_YEAR) * books_per_year_goal)


print(get_number_books_read(100, '2019-04-02'))