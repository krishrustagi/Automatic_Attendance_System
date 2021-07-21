from speak import speak
from face_reco import face_reco
from data_handle import add_record, printdf, total_present
from clock import curr_time, today
import pandas as pd

print("------------- Attendance Management System -------------\n")

attendance_dur = 15 # duration of attendance

# time table reading
df = pd.read_csv("timetable.csv", index_col=0)

# printing the time table
print("\t\t\t Time Table")
print(df, "\n")

times = list(df.columns) # timing of attendance for the courses available in the time table

# to not to check for the same time again and again
class_complete = set()

while True:
    hr, min, sec = curr_time()
    day = today()
    
    if(min > 9):
        st = str(hr)+":"+str(min) # time in HH:MM
    else:
        st = str(hr)+":0"+str(min) # time in HH:MM

    # if it is weekend or the time is out of shift auto turn off
    if day == "saturday" or day == "sunday":
        print("OFF DUTY!")
        break
    if(hr < 7 or hr >= 19):
        print("OFF DUTY!")
        break

    # if the current time is present in times and not has been recorded for the given minute
    if (st not in class_complete) and (st in times):
        course = df.at[day, st]
        if(not pd.isnull(course)):

            class_complete.add(st)

            speak(f"Initializing record of {course} for today")
            
            # adding new record with today's date as column name
            add_record(course)

            start_time = hr*60+min
            end_time = start_time+attendance_dur

            face_reco(course, end_time)
            printdf(course) # print the final attendance sheet after attendance is over

            speak(f"{total_present(course)} students present!") # no. of students present