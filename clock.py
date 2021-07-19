import datetime
from datetime import date
import time

def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

def today_date():
    current_date = date.today()
    return date.day, date.month, date.year