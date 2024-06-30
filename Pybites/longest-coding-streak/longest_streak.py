import json
from dateutil.tz import gettz
from datetime import date, datetime, timedelta, tzinfo
from pathlib import Path
from typing import Tuple, Optional, List
import os

DATA_FILE_NAME = "test1.json"
TMP = Path(os.getenv("TMP", "/tmp"))
DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New_York")
UTC = gettz("UTC")

def calculate_streaks(date_lst: List[datetime]) -> List[Tuple[datetime, datetime]]:

    if len(date_lst) == 1:
        single_date = date_lst.pop()
        return [(single_date, single_date)]


    max_streak = 0
    cur_streak = 0

    first_day_streak = None
    last_day_streak = None

    res = []

    for i in range(1, len(date_lst)):
        current_date = date_lst[i]
        prev_date = date_lst[i-1]
        timedelta_days = (current_date - prev_date).days

        # Found a streak
        if timedelta_days == 1:
            cur_streak += 1
            max_streak = max(max_streak, cur_streak)
            if not first_day_streak:
                first_day_streak = prev_date
        else:
            # Get the best streak
            if cur_streak >= max_streak:
                last_day_streak = current_date
                max_streak = cur_streak
                # Append the first and last day of the streak
                res.append((first_day_streak, last_day_streak))
                first_day_streak, last_day_streak = None, None
            # Reset cur_streak
            cur_streak = 0
    
    if first_day_streak and not last_day_streak:
        last_day_streak = current_date
        res.append((first_day_streak, last_day_streak))
    return res

def longest_streak(
    data_file: Path = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) -> Optional[Tuple[date, date]]:
    """Retrieve datetime strings of passed commits and calculate the longest
    streak from the user's data

    Note: The datetime strings will need to be used to create aware datetime objects

    All datetimes are in UTC, and the timezone of the user is part of the context
    for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
    New York City. You will need to convert datetimes from UTC into the supplied timezone.

    The tests show an example of how a streak can change based on the timezone used.

    If the dataset has two or more streaks of the same length as longest, provide
    only the most recent streak.

    Return a tuple containing start and end date for the longest streak
    or None
    """
    with open(data_file) as f:
        data = json.load(f)
        commits = data.get("commits", None)
        get_dates = sorted([datetime.fromisoformat(x.get("date", None)).astimezone(my_tz).date() for x in commits if x.get("passed", None) == True])
        streaks_lst = calculate_streaks(get_dates)
        return streaks_lst.pop() if streaks_lst else None

# print(longest_streak(my_tz=MY_TZ))

"""
if __name__ == "__main__":
    streak = longest_streak(my_tz=MY_TZ)
    print(f"My longest streak went from {streak[0]} through {streak[1]}")
    print(f"The streak lasted {(streak[1]-streak[0]).days + 1} days")
"""

