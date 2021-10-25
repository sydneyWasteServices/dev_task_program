import pandas as pd
import numpy as np


def clean_sal_df(df : object):
    df.Employee_ID = df.Employee_ID.str.lower()
    df['total'] = df.Gross + df.Super
    return df 

PATH_ROSTER = "D:\\Run Analysis\\blob_storage\\roster\\35th_2021.xlsx"

PATH_SAL = "D:\\Run Analysis\\blob_storage\\driver_salary\\processed\\35th_2021.xlsx"

sal_df = pd.read_excel(PATH_SAL)

roster_df = pd.read_excel(PATH_ROSTER)

sal_df = clean_sal_df(sal_df)

# =======================================
# Count shifts per driver 
# Cost Per shift for driver
# =======================================

pri_dr = roster_df.groupby(['Primary_employeeID'])['Date'].count().rename("pri_dr")

sec_dr = roster_df.groupby(['Secondary_employeeID'])['Date'].count().rename("sec_dr")

dr_shifts = pd.concat([pri_dr, sec_dr], axis=1).fillna(0)

dr_shifts['Total'] = dr_shifts.pri_dr + dr_shifts.sec_dr

dr_shifts = dr_shifts['Total'].reset_index().rename(columns={"index" : "Employee_ID", "Total" : "total_shifts"})   

sal_shifts_df = sal_df.merge(dr_shifts, how="left", on="Employee_ID")

sal_shifts_df['per_shift_pay'] = sal_shifts_df.total / sal_shifts_df.total_shifts

# =======================================
# Export that 
# sal_shifts_df
# =======================================

# =======================================
# Populate cost per shift to Roster 
# Primary Driver Salary and Secondary Driver Salary
# =======================================

def pri_sal_cost(df):
    emp_id = df.Primary_employeeID
    sal = sal_per_shift.loc[sal_per_shift.Employee_ID == emp_id].per_shift_pay.values
    if len(sal) != 0:
       return sal[0]
    else:
        return 0

def sec_sal_cost(df):
    emp_id = df.Secondary_employeeID
    sal = sal_per_shift.loc[sal_per_shift.Employee_ID == emp_id].per_shift_pay.values
    if len(sal) != 0:
       return sal[0]
    else:
        return 0

roster_df['pri_sal'] = roster_df.apply(sal_cost, axis=1)
roster_df['sec_sal'] = roster_df.apply(sal_cost, axis=1)
roster_df['sal_cost'] = roster_df.pri_sal + roster_df.sec_sal

# ==================================
# Salary with  
# ==================================

sal_df = roster_df[['Date','sal_cost','Primary_route', 'Satellite_Route_1','Satellite_Route_2']].fillna(0)    

def per_route_cost(df):
    count = 0 
    p_route = df.Primary_route
    route_1 = df.Satellite_Route_1
    route_2 = df.Satellite_Route_2
    if p_route != 0:
        count = count + 1
    if route_1 != 0:
        count = count + 1
    if route_2 != 0:
        routes = route_2.split("/")
        count = count + len(routes)
    cost = df.sal_cost / count
    return cost, count

sal_df[['per_run_sal', "count_of"]] = sal_df.apply(per_route_cost, axis=1, result_type='expand')

# Salary_Df with 1 Route

sal_df = sal_df[sal_df.count_of.eq(1)][["Date", "Primary_route","per_run_sal","count_of"]].rename()








# ============================================================================
# data process============================================================================
# ============================================================================

# Salary_Df more than 1 , less than 4
# Salary_Df count of Route from 1 to 3
df_2 = sal_df[(sal_df.count_of.gt(1)) & (sal_df.count_of.lt(4))]

sal_df_1 = sal_df[sal_df.count_of.eq(1)][["Date", "Primary_route","per_run_sal","count_of"]].rename(columns={"Primary_route" : "route"})
sal_df_2 = df_2[["Date", "Primary_route","per_run_sal","count_of"]].rename(columns={"Primary_route" : "route"})
sal_df_3 = df_2[["Date", "Satellite_Route_1","per_run_sal","count_of"]].rename(columns={"Satellite_Route_1" : "route"})
sal_df_4 = df_2[["Date", "Satellite_Route_2","per_run_sal","count_of"]].rename(columns={"Satellite_Route_2" : "route"})
# ============================================================================


# Salary_Df count more than 3 routes 
# ============================================================================
df_3 = sal_df[sal_df.count_of.gt(3)]

sal_df_a = df_3[["Date", "Primary_route","per_run_sal","count_of"]].rename(columns={"Primary_route" : "route"})
sal_df_b = df_3[["Date", "Satellite_Route_1","per_run_sal","count_of"]].rename(columns={"Satellite_Route_1" : "route"})




# Salary_Df more than 1 , greater than 4


df_3 = sal_df[sal_df.count_of.gt(3)]



# sal_df_1 = sal_df_1[sal_df_1.route.ne(0)]
# Mark Salary cost to Roster , Primary Driver and Secondary driver
#  



# Roster