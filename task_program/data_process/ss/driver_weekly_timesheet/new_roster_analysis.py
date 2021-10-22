import pandas as pd
import numpy as np
import xlwings as xw
# Not apportion to avg hourly wage  

CURRENT_WEEK = "17th_2021"
    
PATH_PAYSHEET = 'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\paysheet_28.04-04.05.2021_17th_2021.xlsx'
PATH_ROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\17th_2021.xlsx'

COMPLETE_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\weekly_pay_summary\\{CURRENT_WEEK}.xlsx'

df_paysheet = pd.read_excel(PATH_PAYSHEET)
df_ros = pd.read_excel(PATH_ROS)

# lower case the Employee ID in pay sheet
df_paysheet['EmpID'] = df_paysheet.EmpID.str.lower()

# ============================================================================
# Data Audit - Is Employee Name and ID correct 
df_Roster_Emp_counts = (df_ros
 .groupby(['Primary_employeeID'
           ,'Primary_driver_Name'
           ,'Primary_route'])[['Run_type']].count().reset_index()
)

# ============================================================================

df_total_counts_on_run = (df_ros
 .groupby('Primary_employeeID')['Primary_route'].count().reset_index()
)

df_runs_totalnOccurrence = pd.merge(df_Roster_Emp_counts, df_total_counts_on_run, how='left', on='Primary_employeeID')

# rename the column, so not to confuse
df_runs_totalnOccurrence = df_runs_totalnOccurrence.rename(columns={'Run_type' : 'run_count', 'Primary_route_y' : 'total_run'})

# Calculate Portion
df_runs_totalnOccurrence['portion']= df_runs_totalnOccurrence.pipe(lambda data : data['run_count'] / data['total_run'])

# Merge portion with Salary & 
df_salary_run_portion = pd.merge(df_runs_totalnOccurrence, df_paysheet, how='left', left_on='Primary_employeeID', right_on='EmpID')

# Calculate Hour and Salary portion to each route
df_salary_run_portion['hour_portion'] = df_salary_run_portion.pipe(lambda data : data.work_hours * data.portion )

df_salary_run_portion['total_salary_portion'] = df_salary_run_portion.pipe(lambda data : data.Total_payment * data.portion )

# DataSet for Manager 
df_dataset = df_salary_run_portion[[
'Primary_employeeID',
'Primary_driver_Name',
'Primary_route_x',
'portion',
# 'Emp_status',
'hour_portion',
'total_salary_portion']].sort_values('Primary_route_x')

salary_per_run = df_dataset.groupby('Primary_route_x')['total_salary_portion'].sum().reset_index()

wb = xw.Book()

wb.sheets[2].name = 'Employee_name_ID_check' 

wb.sheets[2].range('A1').value = df_Roster_Emp_counts

wb.sheets[1].name = 'dataset'

wb.sheets[1].range('A1').value = df_dataset

wb.sheets[0].name = 'Salary per run'

wb.sheets[0].range('A1').value = salary_per_run



wb.save(COMPLETE_PATH)
wb.close()