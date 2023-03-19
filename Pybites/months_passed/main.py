from datetime import date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def check_if_valid_datetime_obj(year:int, month:int, day:int) -> None:
    try:
        datetime_obj = date(year, month, day)
    except TypeError:
        raise TypeError('Type Error encountered')
    except ValueError:
        raise ValueError('Value Error encountered')
    
    if datetime_obj < START_DATE:
        raise ValueError('datetime obj cannot be before the start date')
    

def calc_months_passed(year, month, day):
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    total_months = 0
    
    check_if_valid_datetime_obj(year, month, day)
    
    datetime_obj = date(year, month, day)
    timedelta_obj = relativedelta(datetime_obj, START_DATE)
    year_diff, month_diff, day_diff = timedelta_obj.years, timedelta_obj.months, timedelta_obj.days
    
    years_convert_to_months = year_diff * MONTHS_PER_YEAR
    
    total_months += years_convert_to_months
    
    total_months += years_convert_to_months
    
    if day_diff >= MIN_DAYS_TO_COUNT_AS_MONTH:
        total_months += 1
    
    return total_months
    

years, months, days = 2018, 12, 10
print(calc_months_passed(years, months, days))