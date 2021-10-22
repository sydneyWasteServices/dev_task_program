import pandas as pd
import numpy as np
import xlwings as xw 

# Check Route name in Roster

# GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG']
# CARDBOARD = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP']
# COMINGLED = ['CBK', 'RLC', 'RLG', 'DOY']
# SUBCONTRACTED = ['SUB', 'JJT', 'ALLMED', 'BIN', 'CKG', 'CLN', 'GRACE', 'JJR', 'OWE', 'REM', 
# 'REP', 'REQ', 'RRNW', 'RRR', 'SHR', 'SPD', 'SUE', 'URM', 'VEO', 'VEOACT', 'VTG', 'AUSSKIP','GRIMA']
# UOS = ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']

WEEK_NUM = '31th_2021'
TOLL_FILE_EXT = 'csv'

PATH_TOLLCOST = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\toll\\og_toll\\{WEEK_NUM}.{TOLL_FILE_EXT}'
PATH_TAGID = 'D:\\Run Analysis\\BLOB_STORAGE\\toll_id.csv'
PATH_ROS = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{WEEK_NUM}.xlsx'

PATH_COMPLETE = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\toll\\weekly_summary_toll\\{WEEK_NUM}.xlsx'

# df_toll = pd.read_csv(PATH_TOLLCOST)

df_toll = pd.read_csv(PATH_TOLLCOST)
df_tagid = pd.read_csv(PATH_TAGID)
df_ros = pd.read_excel(PATH_ROS)

# =======================================================================
# Clean the df 

df_ros['Primary_truck'] = df_ros.Primary_truck.str.replace(' ', '')

df_toll = df_toll.loc[df_toll['LPN/Tag number'].str.isnumeric()]

df_toll['Tag_ID'] = pd.to_numeric(df_toll['LPN/Tag number'])

df_toll['Trip Cost'] = df_toll['Trip Cost'].str.replace('$', '').astype(float)

df_toll = df_toll.rename(columns={'Start Date': 'Date'})


df_toll = df_toll[['Date', 'Tag_ID', 'Details' ,'Trip Cost']]

df_tollcostwRego = pd.merge(df_toll, df_tagid, how='left', on='Tag_ID')

df_tollcostwRego = df_tollcostwRego[['Date_x', 'rego','Tag_ID','Details' ,'Trip Cost']]

# =======================================================================

run_occurence = df_ros.groupby(['Primary_truck','Primary_route'])['Primary_driver_Name'].count().reset_index()

total_runs  = df_ros.groupby('Primary_truck')['Primary_driver_Name'].count().reset_index()

df_ros_occurence_count = pd.merge(run_occurence, total_runs, how='left', on='Primary_truck')

df_ros_occurence_count['portion'] = df_ros_occurence_count.pipe(lambda data : data['Primary_driver_Name_x'] / data['Primary_driver_Name_y'])

df_toll_run_cost = df_tollcostwRego.groupby('rego')['Trip Cost'].sum().reset_index()

# 
df_toll_costwRoute = pd.merge(df_ros_occurence_count, df_toll_run_cost, how='left', left_on='Primary_truck', right_on='rego')


df_toll_costwRoute['run_toll_cost'] = df_toll_costwRoute.pipe(lambda data : data['Trip Cost'] * data['portion'] )

df_result = df_toll_costwRoute.groupby('Primary_route')['run_toll_cost'].sum().reset_index()


df_toll_costwRoute = df_toll_costwRoute[[
'Primary_route',
'rego',
'portion',
'run_toll_cost']].sort_values('Primary_route')

wb = xw.Book()

wb.sheets[0].name = 'Toll to Route'

wb.sheets[1].name = 'Toll Dataset'

wb.sheets[0].range('A1').value = df_result

wb.sheets[1].range('A1').value = df_toll_costwRoute


wb.save(PATH_COMPLETE)
wb.close()
# df_result.to_csv(PATH_COMPLETE, index=False)
