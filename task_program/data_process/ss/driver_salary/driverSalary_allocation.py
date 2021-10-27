import pandas as pd
import numpy as np
import xlwings as xw

# Rather Calculating Driver's Salary per Hours 
# Just Calculate them as per occurence of Roster


CURRENT_WEEK = '31th_2021'

PATH_ROSTER = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{CURRENT_WEEK}.xlsx'
PATH_PAYSHEET = f'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\{CURRENT_WEEK}.xlsx'
PATH_COMPLETE = f'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\weekly_pay_summary\\{CURRENT_WEEK}.xlsx'

df_ros = pd.read_excel(PATH_ROSTER)
df_sal = pd.read_excel(PATH_PAYSHEET)

# Remember to change the employeeID column header to EmpID 
df_sal.EmpID = df_sal.EmpID.str.lower()
df_sal.EmpID = df_sal.EmpID.str.strip()

df_ros.Primary_employeeID = df_ros.Primary_employeeID.str.strip()
# Occurrence of drivers on the run and Total 
occurrence = df_ros.groupby(['Primary_employeeID','Primary_route'])['Run_type'].count().reset_index()

total = df_ros.groupby('Primary_employeeID')['Run_type'].count().reset_index()

df_combine = pd.merge(occurrence, total, how='left', on='Primary_employeeID')

# print this table 
df_roster_run_count = df_combine.rename(columns={'Run_type_y' : 'Total'})

df_roster_run_count['portion'] = df_roster_run_count.pipe(lambda data : data['Run_type_x'] / data['Total'])

# Merge Roster Count df and Salary df 
df_sal_costPerRun = pd.merge(df_roster_run_count, df_sal, 
                             how='left', 
                             left_on='Primary_employeeID', 
                             right_on='EmpID')

df_sal_costPerRun['cost_per_run']= df_sal_costPerRun.pipe(lambda data : data['portion'] * data['Total_payment'])


df_result = df_sal_costPerRun[['Primary_route', 'cost_per_run']].groupby('Primary_route')['cost_per_run'].sum().reset_index()

# Create Excel WorkBook that has 
wb = xw.Book()

# Print Run Cost Ratio to Excek sheet 0 
wb.sheets[0].name = 'Route_RationOnSal' 

wb.sheets[0].range('A1').value = df_roster_run_count

# Print Result df

wb.sheets[1].name = 'Result'

wb.sheets[1].range('A1').value = df_result

# Original Salary Payment

wb.sheets[2].name = 'The_Salary_Payment'

wb.sheets[2].range('A1').value = df_result

wb.save(PATH_COMPLETE)
wb.close()