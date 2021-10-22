import pandas as pd
import numpy as np
import xlwings as xw
import glob 

# If it is fleet, it has to split with NIWPR1 & 2 by total Income Percentage


# From Excel sheet
# Start path
# D:\Run Analysis\BLOB_STORAGE\expenses_truck\all_other_mv_expense\to_be_process

# Complete path
# D:\Run Analysis\BLOB_STORAGE\expenses_truck\all_other_mv_expense\processed

# Use Ratio base to allocate MV expense that has number plate

# Aggregate all past roster to summary a list of Route Occurence for Trucks

CURRENT_WEEK = '29th_2021'

PATH_CURRENT_WEEK = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{CURRENT_WEEK}.xlsx'     

PATH_MVEXP = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\all_other_mv_expense\\to_be_process\\{CURRENT_WEEK}.xlsx'       

PATH_ALLROSTER = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed'

#========================================================================


# Ratio Table
df_all_ros = pd.concat(map(pd.read_excel, glob.glob(f'{PATH_ALLROSTER}\\*.xlsx')))

df_curr_week = pd.read_excel(PATH_CURRENT_WEEK)

df_mvexp = pd.read_excel(PATH_MVEXP)

df_all_ros.Primary_truck = df_all_ros.Primary_truck.str.replace(' ','')


# Only select the Route that Current week Roster has  
curr_wk_route = df_curr_week.Primary_route.unique()

# Plus All the Satellie route
curr_wk_satRoute = df_curr_week[df_curr_week.Satellite_Route_1.notnull()].Satellite_Route_1.unique()   

# Join 2 routes together 
all_curr_routes = np.append(curr_wk_route, curr_wk_satRoute)


# Clean the ?????? in Primary Route
df_all_ros = df_all_ros[df_all_ros.Primary_route.isin(all_curr_routes) & df_all_ros.Primary_truck.ne('??????')]      



occurrence = df_all_ros.groupby(['Primary_truck','Primary_route'])['Run_type'].count().reset_index()   

total = df_all_ros.groupby('Primary_truck')['Run_type'].count().reset_index() 

table_ratio = pd.merge(occurrence, total, how='left', on='Primary_truck') 

table_ratio['portion'] = table_ratio.Run_type_x / table_ratio.Run_type_y



# Display

table_ratio = table_ratio[['Primary_truck', 'Primary_route', 'portion']]

table_mvexp_ratio = pd.merge(df_mvexp, table_ratio, left_on='Job No.', right_on='Primary_truck')

table_mvexp_ratio['amount'] = table_mvexp_ratio.portion * table_mvexp_ratio.Debit 

# Display
table_mvexp_ratio = table_mvexp_ratio.drop(columns=['Debit','Credit' ,'Memo', 'Job No.'])

table_mvexp_ratio = table_mvexp_ratio.groupby(['catID','Primary_route'])['amount'].sum()

# Issues  I Havn't times the total amount into portion

wb = xw.Book()

wb.sheets.add()

wb.sheets[0].name = 'Mv_exp_alloc_details'

wb.sheets[0].range('A1').value = table_mvexp_ratio

wb.sheets[1].name = 'MV_Exp_ratio'

wb.sheets[1].range('A1').value = table_ratio


wb.sheets[2].name = 'mvexp_transaction'

wb.sheets[2].range('A1').value = df_mvexp


COMPLETE_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\all_other_mv_expense\\processed\\{CURRENT_WEEK}.xlsx'

wb.save(COMPLETE_PATH)

wb.close()
