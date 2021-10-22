import pandas as pd
import numpy as np

CURRENT_WEEK = '31th_2021'

PATH_REGO = 'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\Rego_2021.xlsx'

PATH_ROS = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{CURRENT_WEEK}.xlsx'

df_rego = pd.read_excel(PATH_REGO)
df_ros = pd.read_excel(PATH_ROS)


# Clean and Process data 
df_ros.Primary_truck = df_ros.Primary_truck.str.replace(' ','')

occurrence = df_ros.groupby(['Primary_truck', 'Primary_route'])['Run_type'].count().reset_index()

total = df_ros.groupby('Primary_truck')['Primary_route'].count().reset_index()

# 
df_counts = pd.merge(occurrence, total, how='left', on='Primary_truck')

df_counts['portion'] = df_counts['Run_type'] / df_counts['Primary_route_y']


df_rego_counts = pd.merge(df_counts, df_rego, how='left', left_on='Primary_truck', right_on='Rego')

# Weekly or monthly ***********************  weekly_rego_payment / monthly_rego_payment
df_rego_counts['amount'] = df_rego_counts.weekly_rego_payment * df_rego_counts.portion
# Weekly or monthly *********************** 

COMPLETED_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\rego\\weekly_rego_expense\\{CURRENT_WEEK}.csv'

df_rego_counts.groupby('Primary_route_x')['amount'].sum().reset_index().to_csv(COMPLETED_PATH)

