# UOS
# CUM => it has Weight but it is not tipping with itself
        # it is tipping with other waste / Cardboards 
        # I can calculate them, to match up which truck 
        # and day that particular CUM has tip with is hard

# Tips other than UOS Route

# UOS
# UOS_ROUTE = ['NEPCB','UOSCB','UOSCO','UOSGW','CMDCB','CMDGW','CUMCB','CUMGW','NEPGW']

# Cardboard => FLP HYG RED RL5 RL6 RL8 RLP RLR

# Data Audit
# To find out what is not suppose in CB but in CB routes 
# Display General CB route 

# Cardboard Charge Rate difference 
# Polytrde $120
# Grimea $150

import pandas as pd
import numpy as np
import xlwings as xw 

CURRENT_WEEK = '31th_2021'

PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\waste_edge_tipping\\{CURRENT_WEEK}.csv'
COMPLETED_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\processed_waste_edge_tipping\\{CURRENT_WEEK}.xlsx'

df = pd.read_csv(PATH, encoding = "ISO-8859-1")

# Clean Route No and datetime format the date columns
df[['Route No', 'Weekday']]= df['Route No'].str.split('-', 1, expand=True)
df['Route Date'] = pd.to_datetime(df['Route Date'], format='%d-%b-%Y', errors='coerce')
df['Disposal Date'] = pd.to_datetime(df['Disposal Date'], format='%d-%b-%Y', errors='coerce')
df['Tip Site'] = df['Tip Site'].str.lower()

GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG']
COMINGLED = ['CBK', 'RLC', 'RLG', 'DOY']
UOS = ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']

ALL_CB = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP','UOSCB','CMDCB','NEPCB','CUMCB','HOOKCB']

# Rebate Rate Diiference
# ==================================================================================================
# Process Cardboard Rebate Rate Difference
# Polytrade => 120
# Grima => 150
def cb_rate(tip_site):
    try: 
        if "grima" in tip_site:
            return 150
        elif "polytrade" in tip_site:
            return 120
        else: 
            return 150
    except:
        print(tip_site)

df_cb = df[df['Route No'].isin(ALL_CB)]

df_cb['CB_TIP_RATE'] = df_cb['Tip Site'].apply(cb_rate)

# Own Scale Trucks only work for General Waste 

df_cb['CB_Rebate'] = df_cb['Weight'] *  df_cb['CB_TIP_RATE']

df_cb = df_cb.loc[(df_cb['Gross Weight'] > 0) & (df_cb['Tare Weight'] > 0)]

df_cb_rebate_weight = df_cb.groupby('Route No')['Weight','CB_Rebate'].sum().reset_index()
# ==================================================================================================


# Non-Cardboard Runs
# ======================================================================================
# GW Tipping
GW_TIP_RATE = 265

df_gw = df[df['Route No'].isin(GENERAL_WASTE)]

df_gw = df_gw.loc[(df_gw['Gross Weight'] > 0) & (df_gw['Gross Weight'] > 0)]

df_gw['GW_Rebate'] = df_gw['Weight'] *  GW_TIP_RATE

df_gw_cost_weight = df_gw.groupby('Route No')['Weight','GW_Rebate'].sum().reset_index()

# ======================================================================================
# CO Tipping

CO_TIP_RATE = 190

df_co = df[df['Route No'].isin(COMINGLED)]

df_co.loc[(df_co['Gross Weight'] > 0) & (df_co['Gross Weight'] > 0)]

df_co['CO_Rebate'] = df_co['Weight'] *  CO_TIP_RATE

df_co_cost_weight = df_co.groupby('Route No')['Weight','CO_Rebate'].sum().reset_index()

# ======================================================================================

# UOS minor Runs Tipping 
UOS_ROUTE =['NEPCB','UOSCB','UOSCO','UOSGW','CMDCB','CMDGW','CUMCB','CUMGW','NEPGW']

df_uos = df[df['Route No'].isin(UOS_ROUTE)]

df_uos_minor = df_uos.loc[~(df_uos['Gross Weight'] > 0 ) & ~(df_uos['Tare Weight'] > 0 )]

df_uos_minor['Weight_in_ton'] = df_uos_minor['Weight'] / 1000

df_uos_minor_table = df_uos_minor.groupby('Route No')['Weight_in_ton'].sum().reset_index()


# Display What runs in tipping 
# ======================================================================================

df['Route No'].unique()

wb = xw.Book()

wb.sheets.add()
wb.sheets.add()

# OG Tipping Dataset 
# =============
wb.sheets[0].name = 'tipping_df'

wb.sheets[0].range('A1').value = df

# All CB rebate
# ===================
wb.sheets[1].name = 'cb_df'

wb.sheets[1].range('A1').value = df_cb_rebate_weight


# gw cost
# ======================
wb.sheets[2].name = 'gw_df'

wb.sheets[2].range('A1').value = df_gw_cost_weight


# co cost
# ===================


wb.sheets[3].name = 'co_df'

wb.sheets[3].range('A1').value = df_co_cost_weight


# UOS Minor Runs - e.g. NEPCB / CMDCB
# ===================



wb.sheets[4].name = 'UOS_minor'

wb.sheets[4].range('A1').value = df_uos_minor_table 

wb.save(COMPLETED_PATH)
wb.close()






