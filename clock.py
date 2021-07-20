import datetime
from datetime import date
import time

# current date
def today_date():
    current_date = date.today()
    return str(current_date.day), str(current_date.month), str(current_date.year)

# current time
def curr_time():
    current_time = datetime.datetime.now()
    return current_time.hour, current_time.minute, current_time.second

# when the current time exceeds the end time of the attendance
# switch camera off
def end_face_reco(end_time):
    hr, min, sec = curr_time()
    hr*=60*60
    min *= 60

    if hr+min > end_time:
        return True
    return False