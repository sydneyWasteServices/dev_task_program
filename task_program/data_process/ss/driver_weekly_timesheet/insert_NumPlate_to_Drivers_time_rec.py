import pandas as pd
import numpy as np


week = "15th_2021"

PATH_ROS = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{week}.xlsx'
PATH_EMPID = "D:\\Run Analysis\\BLOB_STORAGE\\EmployeeID.csv"

PATH_DRIVERS_TIME_REC = 'D:\\Run Analysis\\BLOB_STORAGE\\driver_timesheet_rec\\15th_2021_driver_time_rec.xlsx'


COMPLETE_PATH = f'D:\Run Analysis\BLOB_STORAGE\driver_timesheet_rec\driver_time_rec_with_NumPlate\\{week}.csv'


df_ros = pd.read_excel(PATH_ROS)

df_emp = pd.read_csv(PATH_EMPID)
df_Drivers_rec = pd.read_excel(PATH_DRIVERS_TIME_REC)



df_Drivers_rec_ID = pd.merge(df_Drivers_rec, df_emp, how='left', on=['firstname', 'lastname'])


df_ros.sort_values(['Primary_employeeID', 'Date'])

df_Drivers_rec_ID = df_Drivers_rec_ID.rename(columns={'EmployeeID' : 'Primary_employeeID'})


df_export = pd.merge(df_Drivers_rec_ID, df_ros, how='left', on=['Date', 'Primary_employeeID'])

df_export = df_export.rename(columns={'Boomgate_Employee_Time In' : 'Boomgate_Time In'})


df_export = df_export[['Name_x',
'tanda_start_time',
'tanda_end_time',
'Boomgate_Time Out',
'Boomgate_Time In',
'Primary_route',
'Primary_truck']]


df_export.loc[df_export['Boomgate_Time Out'].isnull() | df_export['Boomgate_Time In'].isnull()].to_csv(COMPLETE_PATH)