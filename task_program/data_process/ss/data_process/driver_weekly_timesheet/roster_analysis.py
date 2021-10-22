import pandas as pd 
import numpy as np

# Paths 
PATH_ROSTER = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\15th_2021.xlsx'

PATH_SALARY = 'D:\\Run Analysis\\BLOB_STORAGE\\Driver_weekly_timesheet\\processed_timesheet\\15th_2021.csv'


PATH_DRIVERS_COST_EMPID = 'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\15th_2021_drivers_cost_EMPID.csv'

PATH_DRIVERS_COST = 'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\15th_2021_drivers_cost.csv'


# 56,887.79 

# Issues
# 1. Roster naming => Route Number  HOOK  should change to HOOK1
# 2. Roster naming => UOS run need to go back to   the Roster aganist Waste edge booking 
#                   to check which Actual run belongs to the Roster


WEEKLY_DRIVERS_SALARY = 68398.82

df_sal = pd.read_csv(PATH_SALARY)
df_ros = pd.read_excel(PATH_ROSTER)

# Merge Total hours to Roster 
df_sal_ros = pd.merge(df_ros, df_sal , left_on='Primary_employeeID',right_on='EmployeeID_y')

# trim the table
df_sal_ros[[
    'Date',
    'Run_type',
    'Primary_employeeID',
    'Secondary_employeeID',
    'Primary_driver_Name',
    'Secondary_Driver_Name',
    'Primary_route',
    'Satellite_Route_1',
    'Satellite_Route_2',
    'Primary_truck',
    'Alternative_Truck',
    'Subcontracted_From/Special_Client',
    'Total_hour'
]]

# Count occurence that Run against a driver  
occurence_per_runs = (df_sal_ros
 .groupby(['Primary_employeeID', 'Primary_route','Total_hour'])['Run_type']
 .count()
 .reset_index())

# count total runs of a driver 
total_runs = df_sal_ros.groupby('Primary_employeeID')['Run_type'].count().reset_index()

# Merge occurence_per_runs and total_runs
df = pd.merge(occurence_per_runs, total_runs, on='Primary_employeeID', how='left')

# Sum all drivers Hours to get the total hour of the week 
df_total_hours = df.drop_duplicates(subset='Primary_employeeID',keep='first')

total_drivers_hour = df_total_hours.Total_hour.sum()

avg_rate = WEEKLY_DRIVERS_SALARY / total_drivers_hour



df['hours_per_run'] = df.pipe(lambda data :data['Total_hour'] * (data['Run_type_x']/data['Run_type_y']) )


df['driver_cost_per_run'] = df.pipe(lambda data :data['hours_per_run'] * avg_rate )



df.sort_values('Primary_route').to_csv(PATH_DRIVERS_COST_EMPID, index=False)

df = df.groupby('Primary_route')['driver_cost_per_run'].sum().reset_index()

df.sort_values('Primary_route').to_csv(PATH_DRIVERS_COST, index=False)


# Inspect what's in Roster not in waste edge


# notin_run = ['ALLMED','AUSSKIP','BIN','BR1',
# 'BR2','BR3','CBK','CKG','CLN','CMDCB',
# 'CMDGW','CUMCB','CUMGW','DOY','FL2',
# 'FLG','FLP','GRACE','GRIMA','HOOK1',
# 'HYG','JJR','JJT','NEPCB','NEPGW',
# 'OWE','RED','REM','REP','REQ',
# 'RL1','RL2','RL4','RL5','RL6',
# 'RL7','RL8','RL9','RLC','RLD',
# 'RLE','RLG','RLH','RLI','RLJ',
# 'RLK','RLP','RLR','RRNW','RRR',
# 'SHR','SPD','SUB','SUE','SWG',
# 'UOSCB','UOSCO','UOSGW',
# 'URM','VEO','VEOACT','VTG']
# df[~df.Primary_route.isin(notin_run)]



# df_ros.info()
# series_1 = df_sal_ros.groupby(['Primary_employeeID', 'Total_hour'])['Run_type'].count().reset_index()

# df_sal_ros
# df_1.groupby/('Primary_employeeID')['Total_hour'].count()


