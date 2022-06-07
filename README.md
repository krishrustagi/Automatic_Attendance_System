# README.md

# Automatic Attendance System

**Last Updated: *7 June 2022***

1. Demonstration
2. What is an Automatic Attendance System?
3. Prerequisites
4. Getting Started- How to use it?
5. Description

## 1. Demonstration

## 2. What is an Automatic Attendance System?

The automatic Attendance System is designed to collect and manage students’ attendance records from video camera devices installed in a classroom. Based on the verification of student identification in the video cameras, attendance will be updated in the database. Attendance will be taken in every class for only an interval of 15 minutes time. This works on a timetable which tells when the attendance starts for the particular course. 

## 3. Prerequisites

- To use this project Python Version > 3.6 is recommended.
- To contribute to this project, knowledge of basic python scripting, Machine Learning, and Deep Learning will help.

## 4. Getting Started - How to use it?

### Clone this repository

`git clone <https://github.com/krishrustagi/Automatic_Attendance_System>`

### Install required packages

To install all the packages required to run this python program<br><br>
`pip install -r requirements.txt`
<br><br>
**Note:** This project requires a camera. So make sure you have a connection to the camera to your device.

### Add required files and folders

### Time Table

The file `timetable.csv` is just an example. You can the timetable accordingly. Follow the instructions to change the `timetable.csv`

1. Replace the `timetable.csv` with your own timetable and rename it to `timetable.csv`.
2. The format of the timetable in excel format should be like this:

![https://user-images.githubusercontent.com/54409969/126529396-1e9541ff-c424-425a-b3e3-5685e7af4d91.png](https://user-images.githubusercontent.com/54409969/126529396-1e9541ff-c424-425a-b3e3-5685e7af4d91.png)

or in CSV format like this:<br>

```
Day,9:00,10:00,11:35,13:05,15:30,17:00
Monday,Test 2,Test 1,FR101,Test 2,,
Tuesday,,Test 1,FR101,Test 2,,
Wednesday,,Test 2,FR101,,,Test 1
Thursday,,,Test 1,Test 2,FR101,Test 1
Friday,FR101,Test 2,,,Test 1,FR101

```

### Courses/Test Folders

The folders present in the `data` are the attendance records (data files) and the image files for the courses and tests. It contains folders with the name CourseID or TestID as also present as example FR101, Test 2.

1. The CSV file includes `Enrolment No.` and `Name` and it should be named after the course title, e.g. Test 1.csv, FR101.csv.
2. The images folder should include the required images of the students enrolled in the course and every image file should be named to {Enrolment No.}.jpg, e.g. BT19CSE089.jpg

It should follow the given hierarchy:

```
data
|── {CourseID/TestID}
|   └── images
|       └── {Enrolment No.}.jpg
|   └── datafile
|       └── {CourseID/TestID}.csv
|
|── {CourseID/TestID}
|   └── images
|       └── {Enrolment No.}.jpg
|   └── datafile
|       └── {CourseID/TestID}.csv
|

```

### Run

To run this python program, you need to execute the `main.py` python file.

## 5. Description

This program includes 4 things.

1. The records and data are being handled for the automatic attendance using the panda's python library in the file `data_handle.py`.
2. As we have a timetable, so we are using the data time python library to get the current date and time. The attendance is marked with the given date in the format `MM/DD/YYYY`. the time kept is in the format `HH:MM` has also shown in the timetable. All of this is handled in the file `clock.py`.
3. The main part of the program is the face recognition which is handled in the file `face_reco.py` where the face is being detected and recognized using the python module face_recognition. This is a video capture-based project and to perform the video capturing, the cv2 module has been used.
4. This project also includes a text-to-speech service performed using the python module gTTS and the sound will be stored in `speak.mp3` which is then played. This is included in the `speak.py` python file.
