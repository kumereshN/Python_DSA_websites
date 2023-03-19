import os
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def convert_date_str_date_obj(date_str: str, date_format: str = '%Y-%m-%d') -> date:
    return datetime.strptime(date_str, date_format).date()

def get_all_days(start_date: date, end_date: date) -> List[date]:
        
    start_date_obj = convert_date_str_date_obj(start_date)
    end_date_obj = convert_date_str_date_obj(end_date)
    
    all_dates_lst = [start_date_obj + timedelta(days=x) for x in range((end_date_obj-start_date_obj).days + 1)]
    
    return all_dates_lst


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    all_days_lst = get_all_days(start, end)
    
    rates_date = {convert_date_str_date_obj(date_str): rates for date_str, rates in sorted(daily_rates['rates'].items(), key =lambda x: x[0])}.keys()
    
    return rates_date


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    
    rates_file = json.loads(RATES_FILE.read_text())
    
    match_daily_rates(start_date, end_date, rates_file)
    
    pass



start_date, end_date = "2020-01-01", "2020-09-01"
rates_file = json.loads(RATES_FILE.read_text())

print(match_daily_rates(start_date, end_date, rates_file))
# print(sorted(rates_file.items(), key = lambda x: x[0]))