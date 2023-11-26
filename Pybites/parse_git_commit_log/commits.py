from collections import Counter
import os
from typing import Tuple
from urllib.request import urlretrieve
import re

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(
    commit_log: str = commits,
    year: int = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    date_pattern_regex = re.compile('\s+(.*)')
    insertion_deletion_pattern = re.compile('(\d+)\sinsertion[s]?|(\d+)\sdeletion[s]?')

    c = Counter()

    with open(commit_log, 'r') as r:
        lines = r.readlines()
        for line in lines:
            raw_date_str, raw_insertion_deletion = line.split('|')
            date = parse(re.findall(date_pattern_regex, raw_date_str)[0]).strftime('%Y-%m')

            insertion_deletion_str = re.findall(insertion_deletion_pattern, raw_insertion_deletion)
            total_insertion_deletion_sum = sum([int(y) for x in insertion_deletion_str for y in x if y])
            c[date] += total_insertion_deletion_sum
    
    if not year:
        return (min(c, key=c.get), max(c, key=c.get))
    else:
        c = {k:v for k,v in c.items() if str(year) in k}
        return (min(c, key=c.get), max(c, key=c.get))


print(get_min_max_amount_of_commits(year=2019))