import pandas as pd
import numpy as np
import xlwings as xw

CURRENT_WEEK = '24th_2021'

# PATH_ROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\.xlsx' 
# df_ros = pd.read_excel(PATH_ROS)

PATH_SUEZ = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\og_tipping_suez\\weekly\\{CURRENT_WEEK}.csv' 
PATH_WE = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\waste_edge_tipping\\{CURRENT_WEEK}.csv'

COMPLETE_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\tipping_rec\\{CURRENT_WEEK}.xlsx'

df_suez = pd.read_csv(PATH_SUEZ)
df_we = pd.read_csv(PATH_WE)


GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG']
NOTGW_RUN = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP', 'HOOKCB','CBK', 'RLC', 'RLG', 'DOY','NEPCB', 'UOSCB','UOSCO','CMDCB','CUMCB']
UOS = ['UOSGW', 'CMDGW', 'CUMGW', 'NEPGW']

# GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG','UOSGW', 'CMDGW', 'CUMGW', 'NEPGW']
# Date
df_suez.Date = pd.to_datetime(df_suez.Date, format='%d/%m/%Y',errors='ignore')
df_we[['Route No','weekday']]= df_we['Route No'].str.split('-', 1, expand=True)

df_we['Route Date'] = pd.to_datetime(df_we['Route Date'], format='%d-%b-%Y', errors='ignore')
df_we['Disposal Date'] = pd.to_datetime(df_we['Disposal Date'], format='%d-%b-%Y', errors='ignore')
# =====================================

# Filter No Gross and Tare Weight All & Non_GW_run
df_we = df_we.loc[(df_we['Gross Weight'] > 0) & df_we['Tare Weight']]
df_gw_runs = df_we[~df_we['Route No'].isin(NOTGW_RUN)]
df_gw_runs = df_gw_runs.drop(columns=['Disposal Date','Total Charge','Cost Rate','Charge Rate','UOM','Branch','Booking No','Customer Details'])    

# Clean Dockets 
# df_gw_runs['Docket No'].
df_gw_runs['Docket No'] = df_gw_runs['Docket No'].str.replace('.0','',regex=False).str.replace(' ','')   

# Inspect Any Duplicate in Waste Edge Tipping
duplicate_gw_docket = df_gw_runs[df_gw_runs.duplicated(subset=['Docket No'])]
print(f'Waste Edge {duplicate_gw_docket}')

# Inspect Any Duplicate in Suez Tipping
duplicate_suez_docket = df_suez[df_suez.duplicated(subset=['Docket'])]
print(f'Suez  {duplicate_suez_docket}')

# Docket
waste_edge_dockets = df_gw_runs['Docket No']

suez_dockets = df_suez.Docket


we_to_suez_diff = np.setdiff1d(waste_edge_dockets,suez_dockets)

# Waste Edge to Suez Difference
df_we_to_suez = df_gw_runs[df_gw_runs['Docket No'].isin(we_to_suez_diff)]

# Suez to  Waste Edge Difference

suez_to_we_diff = np.setdiff1d(suez_dockets,waste_edge_dockets)

df_suez_to_we = df_suez[df_suez.Docket.isin(suez_to_we_diff)]



wb = xw.Book()

wb.sheets[0].name = 'WE_Suez_difference'

wb.sheets[0].range('A1').value = df_we_to_suez

wb.sheets[1].name = 'Suez_WE_difference'

wb.sheets[1].range('A1').value = df_suez_to_we


wb.save(COMPLETE_PATH)
wb.close()
