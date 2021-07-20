from clock import today_date
import pandas as pd
import numpy as np


# finding the name of student using the enrolment number
# for the face recognition
def find_record(enr, course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False)
    name = df[df['Enrolment No.'] == enr]['Name'].values[0]
    return name

# addting attendance record for the current date for the given course
# initialize everyone attendance as absent
def add_record(course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False)
    dt, mn, yr = today_date()

    df[f"{mn}/{dt}/{yr}"] = 0
    df.to_csv(f'data/{course}/datafile/{course}.csv', index=False)

# marking present if encountered the student by the camera
# 0 -> absent
# 1 -> present
def mark_present(course, enr):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False, index_col=0)
    dt, mn, yr = today_date()

    df.at[enr, f"{mn}/{dt}/{yr}"] = 1
    df.to_csv(f'data/{course}/datafile/{course}.csv')

# print the attendance sheet
def printdf(course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False, index_col=0)
    print(df)

# total number of students present calculated
def total_present(course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False, index_col=0)
    dt, mn, yr = today_date()
    return (df[f"{mn}/{dt}/{yr}"] == 1).sum()



if __name__ == "__main__":
    # print(find_record('BT19CSE057', 'Course_1'))
    add_record("Course_1")
    mark_present("Course_1", "BT19CSE089")