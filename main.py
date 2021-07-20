from speak import speak
from face_reco import face_reco
from data_handle import add_record, printdf, total_present
from clock import curr_time


hr, min, sec = curr_time()
hr*=60*60
min *= 60

start_time = 14*60*60+49*60
end_time = 14*60*60+49*60

# while True:
if hr+min >= start_time and hr+min <= end_time:
    course = "Course_1"
    add_record(course)
    face_reco(course, end_time)
    printdf(course)
    speak(f"{total_present(course)} students present")
