# Automatic Attendance System

**Last Updated: *21 July 2021***<br>
1. What is Automatic Attendance System?
2. Prerequisites
3. Getting Started- How to use it?
4. Working

## 1. What is Automatic Attendance System
Automatic Attendance System is designed to collect and manage student’s attendance records from video camera devices installed in a class rooms. Based on the verification of student identification in the video cameras, attendance will be updated in data base. Attendance will be taken in every class for only an interval of 15 minutes time. This works on a timetable which tells when the attendance starts for the particular course. <br>

**Check out the demo video for its working:** 

## 2. Prerequisites
- To use this project Python Version > 3.6 is recommended.
- To contribute in this project, knowledge of basic python scripting, Machine Learning and Deep Learning will help.

## 3. Getting Started - How to use it?
### Clone this Repository
``
git clone https://github.com/krishrustagi/Automatic_Attendance_System
``
### Install required packages
To install all the packages required to run this python program<br><br>
``
pip install -r requirements.txt
``
<br><br>
**Note:** This project requires camera. So make sure you have connected camera to your device. 

### Add required files and folders
#### Time Table
The file `timetable.csv` is just an for an example. You can the timetable accordingly. Follow the instructions to change the `timetable.csv`
1. Replace the `timetable.csv` with your own timetable and rename it to `timetable.csv`.
2. Format of the timetable in excel format should be like this:

![tt_ex](https://user-images.githubusercontent.com/54409969/126529396-1e9541ff-c424-425a-b3e3-5685e7af4d91.png)

or in csv format like this:<br>
```
Day,9:00,10:00,11:35,13:05,15:30,17:00
Monday,Test 2,Test 1,FR101,Test 2,,
Tuesday,,Test 1,FR101,Test 2,,
Wednesday,,Test 2,FR101,,,Test 1
Thursday,,,Test 1,Test 2,FR101,Test 1
Friday,FR101,Test 2,,,Test 1,FR101
```
#### Couses/Test Folders
The folders present in `data` are the attendance records (datafiles) and the images files for the courses and test. 
1. The csv file includes `Enrolment No.` and `Name` and it should be named after the course title, e.g. Test 1.csv, FR101.csv. 
2. The images folder should include the required images of the students enrolled in the course and every image file should be named to {Enrolment No.}.jpg, e.g. BT19CSE089.jpg

It should follow the given heirarchy:
 ```
 data
 └── {CourseID}
     └── images
         └── {Enrolment No.}.jpg
     └── datafile    
         └── {CourseID}.csv
 
 └── {CourseID}
     └── images
         └── {Enrolment No.}.jpg
     └── datafile    
         └── {CourseID}.csv
 |
 |
 
 ```

### Run
To run this python program, you need to execute `main.py` python file.

## 4. Working
