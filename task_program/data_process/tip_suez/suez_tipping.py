import pandas as pd
import numpy as np
import xlwings as xw
# Target 

# Generate Total Tonnage - General Waste Ton
# Generate Run Ton
# Generate which Truck is not including in the Roster

# list of trucks in Roster 
# list of trucks in Suez  

# Any Truck can go any type of runs 

current_week = '31th_2021'

PATH_suez = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\og_tipping_suez\\weekly\\{current_week}.csv'

PATH_ros = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{current_week}.xlsx'

df_suez = pd.read_csv(PATH_suez)

df_ros = pd.read_excel(PATH_ros)

OTHER_ROUTE = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP','CBK', 'RLC', 'RLG', 'DOY','NEPCB','UOSCB','CMDCB','CUMCB']

df_ros= df_ros[~df_ros['Primary_route'].isin(OTHER_ROUTE)]

df_ros['Primary_truck'] = df_ros.Primary_truck.str.replace(' ','')

# Display 
# LIST of Roster Truck 
trucks_on_roster = df_ros.groupby('Primary_truck')['Primary_truck'].count().index

# Column list of Roster Trucks
col_roster_trucks = np.reshape(trucks_on_roster, (-1,1))

# Display 
# LIST of Suez Truck 
trucks_on_suez = df_suez.groupby('Rego')['Date'].count().index

# Column list of Suez
col_suez_trucks = np.reshape(trucks_on_suez, (-1,1))

# Since some truck runs for
# NIWPR1, NIWPR2 - Subcontract runs
# Some Runs for Cardboard and Comingle 

# Display 
diff_on_trucks = np.setdiff1d(np.array(trucks_on_roster), np.array(trucks_on_suez))

col_diff_on_trucks = np.reshape(diff_on_trucks, (-1,1))

# ================================
# Data process roster
occurrence_on_run = df_ros.groupby(['Primary_truck','Primary_route'])['Primary_driver_Name'].count().reset_index()

total_occurrence = df_ros.groupby('Primary_truck')['Primary_route'].count()

df_run_occurrence = pd.merge(occurrence_on_run, total_occurrence, on='Primary_truck', how='left')

df_run_occurrence['tip_portion'] = df_run_occurrence.pipe(lambda data : data.Primary_driver_Name / data.Primary_route_y) 

df_run_occurrence = df_run_occurrence[['Primary_truck', 'Primary_route_x', 'tip_portion']]

# ================================
# Data process 

weekly_suez_tonNprice = df_suez.groupby(['Rego'])[['Net (t)','total_price']].sum().reset_index()

# Display 
suez_ton = weekly_suez_tonNprice['Net (t)'].sum()
suez_price = weekly_suez_tonNprice['total_price'].sum()

weekly_tipping = pd.merge(df_run_occurrence, weekly_suez_tonNprice, how='left', left_on='Primary_truck', right_on='Rego')


# Display 
weekly_tipping['ton_per_run'] = weekly_tipping.pipe(lambda data : data['Net (t)'] * data['tip_portion'])
weekly_tipping['cost_per_run'] = weekly_tipping.pipe(lambda data : data['total_price'] * data['tip_portion'])

# Display 
weekly_suez_ton_per_run = weekly_tipping.groupby('Primary_route_x')[['ton_per_run', 'cost_per_run']].sum()

weekly_tipping['ton_per_run'] = weekly_tipping.pipe(lambda data : data['Net (t)'] * data['tip_portion'])

weekly_tipping['cost_per_run'] = weekly_tipping.pipe(lambda data : data['total_price'] * data['tip_portion'])


wb = xw.Book()

wb.sheets[0].name = 'tipping_info' 

summarySheet = wb.sheets[0]

summarySheet.range('B1').value = 'Roster'

summarySheet.range('C1').value = 'Suez'

summarySheet.range('D1').value = 'Diff on Trucks'

summarySheet.range('B2').value = col_roster_trucks

summarySheet.range('C2').value = col_suez_trucks

summarySheet.range('D2').value = col_diff_on_trucks

summarySheet.range('E1').value = 'Total Cost'
 

summarySheet.range('E2').value = suez_price

summarySheet.range('F1').value = 'Current Week Ton'

summarySheet.range('F2').value = suez_ton

summarySheet.range('G1').value = 'LastWeek ton bring forward'

summarySheet.range('G2').value = suez_ton - weekly_tipping.ton_per_run.sum()

wb.sheets[1].name = 'Suez_tipping_data'

suez_tipping_data = wb.sheets[1]

suez_tipping_data.range('A1').value = weekly_tipping[['Primary_route_x', 'Primary_truck', 'ton_per_run','cost_per_run']]

wb.sheets[2].name = 'route_cost_ton_data'

wb.sheets[2].range('A1').value = weekly_tipping.groupby('Primary_route_x')[['ton_per_run','cost_per_run']].sum().reset_index()

wb.save(f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\suez_weekly_summary\\{current_week}.xlsx')
wb.close()