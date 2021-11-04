import pandas as pd 
import numpy as np
import typing
from functools import reduce
import operator
import xlwings as xw
import glob

from report_data.routes_list import By_Revenue_type


from raw_data_transformation.cleaner import Cleaner
from raw_data_transformation.filter import Filter
from raw_data_transformation.incomes import Incomes
from raw_data_transformation.transform_date import Transform_date
from raw_data_transformation.resmpleDf import ResampleDf

from tip.waste_edge_tip import Waste_edge_tip

from report_data.general_waste_info import General_waste_info


# Class feature for lcating rotue header
from report_outlook.locator import Locator


# Data info objects
from report_data.route_info import Route_info

# Roster 
from roster.roster import Roster

# Calculate Suez per Run
from tip.suez_tip import Suez_tip

# Calculate Salary 
from salary.salary import Salary

# Calculate Fuel from Waste Edge

from fuel.we_fuel import Waste_edge_fuel_report  

# Calculate toll cost

from toll.toll import Toll

# Calculate Rego 

from rego.rego import Rego

# Calculate Rego 

from mv_exp.mv_exp import Mv_exp


CURRENT_WEEK = '18th_2021'

BOOKING_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\booking_weekly\\{CURRENT_WEEK}.csv'

TIPPING_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\waste_edge_tipping\\{CURRENT_WEEK}.csv'

SUEZ_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\tipping_weekly\\og_tipping_suez\\weekly\\{CURRENT_WEEK}.csv'

# Excel
ROSTER_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed\\{CURRENT_WEEK}.xlsx'

# Excel
SALARY_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\Drivers_pay\\{CURRENT_WEEK}.xlsx'

# Excel
FUEL_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\fuel\\waste_edge_fuel_transactions\\{CURRENT_WEEK}.xlsx'

TOLL_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\toll\\og_toll\\{CURRENT_WEEK}.csv'

TOLL_TAGID_PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\toll_id.csv'

# Excel
PATH_REGO = 'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\Rego_2021.xlsx'

# Excel 
PATH_MVEXP = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\all_other_mv_expense\\to_be_process\\{CURRENT_WEEK}.xlsx'

# Will concat all roster for Ratio
PATH_ALL_ROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed'

VISY_PATH = ''

r_types = [
    # 'TOTAL', 
    # 'TOTAL_EXCL_SUBCON', 
    'GENERAL_WASTE', 
    'COMINGLE',
    'CARDBOARD',
    'UOS'
    # 'SUBCONTRACTED'
]

# UOS RUN  AND NIWPR1 2 runs

gw = sorted(By_Revenue_type['GENERAL_WASTE'].value)
cm = sorted(By_Revenue_type['COMINGLE'].value)
cb = sorted(By_Revenue_type['CARDBOARD'].value)
uos = sorted(By_Revenue_type['UOS'].value)

NON_GW_ROUTE = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP','CBK', 'RLC', 'RLG', 'DOY','NEPCB','UOSCB','CMDCB','CUMCB']

booking_df = pd.read_csv(BOOKING_PATH, dtype={"Schd Time Start": str, "PO": str})

# Cleaning and Transform Dataframe 
# Booking
# =====================================
booking_df = Cleaner().cleanNsplit_routes(booking_df, 'Route number')

booking_df = Transform_date().datify(booking_df, 'Date', '%d/%m/%y')

booking_df = Transform_date().indexitfy(booking_df, 'Date')

booking_df = Filter().confirmed_only(booking_df)
# =====================================
# resampled - so get group key first, then get df group 
booking_df = ResampleDf().resample_weekly(booking_df)

booking_df = ResampleDf().get_first_group(booking_df)

# Filter Non Confirm rows

booking_df = Filter().confirmed_only(booking_df)

# Cleaning and Transform Dataframe 
# Waste Edge Tipping 
# ==============================================
we_tipping_df = pd.read_csv(TIPPING_PATH)

we_tipping_df = Cleaner().cleanNsplit_routes(we_tipping_df, 'Route No')

we_tipping_df = Transform_date().datify(we_tipping_df, 'Route Date', '%d-%b-%Y')

we_tipping_df = Transform_date().datify(we_tipping_df, 'Disposal Date', '%d-%b-%Y')

we_tipping_df = Waste_edge_tip().filter(we_tipping_df)

all_route_waste_edge_tip = Waste_edge_tip().route_tip(we_tipping_df)

# Clean Roster DataFrame 
# For Suez General Waste tipping only  
# ==============================================

df_ros = pd.read_excel(ROSTER_PATH)

df_ros = Roster().rm_space('Primary_truck', df_ros)

# ===========================================================
df_gw_ros = Roster().df_gw_runs(NON_GW_ROUTE, df_ros)

df_gw_ratio = Roster().suez_ratio(df_gw_ros)

df_suez = pd.read_csv(SUEZ_PATH)

# ****************************************************************
# Display Dataset in tab for supporting
# Full Suez Ton and Price, Have yet grouped

# Display
table_detail_suez_cost_per_run = Suez_tip().detail_allocation(df_gw_ratio, df_suez)
# Display
table_suez_cost_per_run = Suez_tip().allocation(df_gw_ratio, df_suez)

# ***************************************************************
# ===================================================================
# Clean Salary ID 
 
df_sal = pd.read_excel(SALARY_PATH)

df_sal = Salary().lowercase_ID(df_sal)
# ***************************************************************
# Display Dataset in tab for Salary
salary_ratio = Roster().salary_ratio(df_ros)

# Display
table_detail_salary_per_run = Salary().detail_allocation(salary_ratio, df_sal)

# Display
table_salary_per_run = Salary().allocation(salary_ratio, df_sal)

# *******************************************************************
# Fuel Report from Waste Edge  
# ===================================================================

df_we_fuel = pd.read_excel(FUEL_PATH)

df_we_fuel =  Cleaner().cleanNsplit_routes(df_we_fuel, 'RouteNumber')

# Display
df_waste_edge_fuel_cost_per_run = Waste_edge_fuel_report().report(df_we_fuel)

# ===================================================================
# Insert info into route income objects

# *******************************************************************
# Toll Expense  
# ===================================================================

df_toll_cost  = pd.read_csv(TOLL_PATH)

df_toll_tagID = pd.read_csv(TOLL_TAGID_PATH)

toll_ratio = Roster().toll_ratio(df_ros)

df_toll_cost = Toll().process_tollCost(df_toll_cost)

df_toll_cost = Toll().merge_rego_tollcost(df_toll_cost, df_toll_tagID)

# Display
table_tollCost_per_run = Toll().allocation(toll_ratio, df_toll_cost)

# *******************************************************************
# rego Expense  
# ===================================================================

df_rego = pd.read_excel(PATH_REGO)

rego_ratio = Roster().rego_ratio(df_ros)

table_rego_per_run = Rego().allocation(rego_ratio, df_rego)


# *******************************************************************
# Mv Expense  
# ===================================================================

# # Excel 
# PATH_MVEXP = 'D:\Run Analysis\BLOB_STORAGE\expenses_truck\all_other_mv_expense\to_be_process'

# # Will concat all roster for Ratio
# PATH_ALL_ROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed'

df_mvexp = pd.read_excel(PATH_MVEXP)

df_all_ros = Mv_exp().df_concat(PATH_ALL_ROS)

###### Current Week routes 
currentWk_routes = Roster().current_routes(df_ros)

df_all_ros = Mv_exp().filter_df_by(df_all_ros, currentWk_routes)


# df_mvexp_ratio = Mv_exp().ratio(PATH_ALL_ROS)

table_mvexp_per_run = Mv_exp().allocation(df_all_ros, df_mvexp)


print(table_mvexp_per_run)
# if rego exist

# Problem on not showing full frame



# if rego not exists  
# Fleet 



# table_mvexp_per_run.to_csv(completed_path)


# df_ros

ROUTE_INFO_LIST = {}

all_route_income_name = Incomes().all_route_income(booking_df)



# Populate income into ROUTE_INFO_LIST
for name in all_route_income_name.index:
    ROUTE_INFO_LIST[name] = Route_info(name)
    ROUTE_INFO_LIST[name].income = all_route_income_name[name]


# Populate Waste Edge Weight Only GW CM CB

# Populate Suez Tipping


for name in all_route_waste_edge_tip.index:

    if name in gw:
        try:
            
            ROUTE_INFO_LIST[name].gw_waste_edge_weight = all_route_waste_edge_tip[name].item()
            
            ROUTE_INFO_LIST[name].gw_suez_weight = table_suez_cost_per_run[table_suez_cost_per_run.Primary_route_x.eq(name)].ton_per_run.item()
            
            ROUTE_INFO_LIST[name].gw_var_on_waste_edge_to_suez_weight = ROUTE_INFO_LIST[name].gw_suez_weight - ROUTE_INFO_LIST[name].gw_waste_edge_weight

            ROUTE_INFO_LIST[name].gw_suez_cost = table_suez_cost_per_run[table_suez_cost_per_run.Primary_route_x.eq(name)].cost_per_run.item()

            ROUTE_INFO_LIST[name].driver_salary = table_salary_per_run[table_salary_per_run.Primary_route.eq(name)].cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_fuel = Waste_edge_fuel_report().fuel_cost(df_we_fuel, name)

            ROUTE_INFO_LIST[name].mv_tolls = table_tollCost_per_run[table_tollCost_per_run.Primary_route.eq(name)].toll_cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_rego = table_rego_per_run[table_rego_per_run.Primary_route_x.eq(name)].amount.item()

            
            
        except:
            
            print(f'GW Cant fill ====> {name}')
        
    elif name in cm:
        try:
            ROUTE_INFO_LIST[name].cm_waste_edge_weight = all_route_waste_edge_tip[name].item()
            
            ROUTE_INFO_LIST[name].driver_salary = table_salary_per_run[table_salary_per_run.Primary_route.eq(name)].cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_fuel = Waste_edge_fuel_report().fuel_cost(df_we_fuel, name)

            ROUTE_INFO_LIST[name].mv_tolls = table_tollCost_per_run[table_tollCost_per_run.Primary_route.eq(name)].toll_cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_rego = table_rego_per_run[table_rego_per_run.Primary_route_x.eq(name)].amount.item()

        except:
            
            print(f'CM Cant fill ====> {name}')

    elif name in cb:

        try:
            ROUTE_INFO_LIST[name].cb_waste_edge_weight = all_route_waste_edge_tip[name].item()

            ROUTE_INFO_LIST[name].driver_salary = table_salary_per_run[table_salary_per_run.Primary_route.eq(name)].cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_fuel = Waste_edge_fuel_report().fuel_cost(df_we_fuel, name)

            ROUTE_INFO_LIST[name].mv_tolls = table_tollCost_per_run[table_tollCost_per_run.Primary_route.eq(name)].toll_cost_per_run.item()

            ROUTE_INFO_LIST[name].mv_rego = table_rego_per_run[table_rego_per_run.Primary_route_x.eq(name)].amount.item()

        except:
            
            print(f'CB Cant fill ====> {name}')

    # UOS runs - Mixed with GW CM CB => split the actual weight 



print(ROUTE_INFO_LIST['BR1'].mv_rego)



# mv_rm_cc : float = 0 ,
#         mv_rm_cb : float = 0 ,
#         mv_rm_mc : float = 0 ,
#         mv_rm_tyre : float = 0 ,
#         labour : float = 0 ,
#         mv_others : float = 0


# # ====================================================================
# # General Waste Info process 


# gw_total_income = Incomes().types_income(booking_df, gw)

# gw_route_income_table = Incomes().routes_income(booking_df, gw)

# gw_routes_number = list(gw_route_income_table['Route number'])

# gw_routes_income = list(gw_route_income_table['Price'])

# # General Waste Rotue Header start at
# # Row 4 Column 12  

# wb = xw.Book()

# START_GW_ROUTE_HEADER_ROW = 4

# START_GW_ROUTE_HEADER_COL = 12


# # Total Sheet
# # =================================================
# wb.sheets[0].name = 'Total'

# # =================================================

# wb.sheets[0].range((START_GW_ROUTE_HEADER_ROW,START_GW_ROUTE_HEADER_COL)).value = gw_routes_number

# gw_total_route_addresses = Locator().get_route_header_address(wb, 0,START_GW_ROUTE_HEADER_ROW,START_GW_ROUTE_HEADER_COL)

# gw_info = General_waste_info(gw_total_income, gw_routes_income, gw_total_route_addresses)


# print(gw_info.address_in_total_sheet)

