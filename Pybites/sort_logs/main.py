from datetime import datetime, timezone
from pathlib import Path
import re
from time import sleep
from typing import Tuple, List
from operator import itemgetter
from zipfile import ZipFile

TMP = Path('./tmp')

LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'

def create_logs():
    # LOG_DIR.mkdir()
    for i in range(1, 10, 2):
        sleep(0.01)
        p = LOG_DIR / f"{i}.log"
        p.write_text('log line')


def zip_last_n_files(directory: Path = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
                         
        
    log_entries = list(directory.glob('*.log'))
    
    converted_entries = [(log.name, datetime.fromtimestamp(log.stat().st_atime, tz = timezone.utc)) for log in log_entries]
    n_sorted_entries = sorted(converted_entries, key = itemgetter(1), reverse = True)[:n]
    renamed_log_entries = list()

    for log_entry, created_time in n_sorted_entries:
        log_entry_replacement = log_entry.replace('.log','')
        created_time_str = datetime.strftime(created_time, '%Y-%m-%d')
        new_log_filename = f'file{log_entry_replacement}_{created_time_str}.log'
        Path(directory / log_entry).rename(Path(directory / new_log_filename))
        renamed_log_entries.append(new_log_filename)
    
    with ZipFile(zip_file, 'w') as myzip:
        for log in renamed_log_entries:
            myzip.write(Path(directory / log), (Path(directory / log).name))

    return renamed_log_entries


zip_file = TMP / ZIP_FILE

# create_logs()
# print(zip_last_n_files(zip_file = zip_file))


zip_ = ZipFile(zip_file)
files = sorted(zip_.namelist())


print(files[0])
assert re.match(r'^5_\d{4}-\d{2}-\d{2}.log$', files[0].replace('file',''))