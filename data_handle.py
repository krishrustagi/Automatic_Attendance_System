from clock import today_date
import pandas as pd
import numpy as np

def find_record(name, course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False)
    name = df[df['Enrolment No.'] == name]['Name'].values[0]
    return name

def add_record(course):
    df = pd.read_csv(f'data/{course}/datafile/{course}.csv', error_bad_lines=False)
    dt, mn, yr = today_date()

    df[f"{mn}+'/'+{dt}+'/'+{yr}"] = 0
    print(df)

if __name__ == "__main__":
    print(find_record('BT19CSE057', 'Course_1'))
    add_record("Course_1")