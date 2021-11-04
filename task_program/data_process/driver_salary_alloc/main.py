import pandas as pd
import numpy as np

WEEK = "40th_2021"

PATH_ROSTER = f"D:\\Run Analysis\\blob_storage\\roster\\{WEEK}.xlsx"
PATH_SAL = f"D:\\Run Analysis\\blob_storage\\driver_salary\\processed\\{WEEK}.xlsx"

PATH_COMPLETE_DETAIL = f"D:\\Run Analysis\\blob_storage\\driver_salary\\allocated\\{WEEK}_detail.csv"
PATH_COMPLETE_ALLOC = f"D:\\Run Analysis\\blob_storage\\driver_salary\\allocated\\{WEEK}.csv"

sal_df = pd.read_excel(PATH_SAL)

roster_df = pd.read_excel(PATH_ROSTER)

sal_df.Employee_ID = sal_df.Employee_ID.str.lower()

sal_df['total'] = sal_df.Gross + sal_df.Super

count_pri_dr = roster_df.groupby(['Primary_employeeID'])['Date'].count().rename("pri_dr")

count_sec_dr = roster_df.groupby(['Secondary_employeeID'])['Date'].count().rename("sec_dr")

count_dr_shifts = pd.concat([count_pri_dr, count_sec_dr], axis=1).fillna(0)

count_dr_shifts['Total'] = count_dr_shifts.pri_dr + count_dr_shifts.sec_dr

count_dr_shifts = count_dr_shifts['Total'].reset_index().rename(columns={"index" : "Employee_ID", "Total" : "total_shifts"})   
sal_shifts_df = sal_df.merge(count_dr_shifts, how="left", on="Employee_ID")

sal_shifts_df['per_shift_pay'] = sal_shifts_df.total / sal_shifts_df.total_shifts
sal_per_shift = sal_shifts_df[["Employee_ID", "per_shift_pay"]]

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


roster_df['pri_sal'] = roster_df.apply(pri_sal_cost, axis=1)
roster_df['sec_sal'] = roster_df.apply(sec_sal_cost, axis=1)

roster_df['sal_cost'] = roster_df.pri_sal + roster_df.sec_sal

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

sal_df_1 = sal_df[sal_df.Primary_route.ne(
    0)][["Date", "Primary_route", "per_run_sal", "count_of"]].rename(columns={'Primary_route': 'route'})

sal_df_2 = sal_df[sal_df.Satellite_Route_1.ne(
    0)][["Date", "Satellite_Route_1", "per_run_sal", "count_of"]].rename(columns={'Satellite_Route_1': 'route'})

sal_df_3 = (sal_df[sal_df.Satellite_Route_2.ne(0)][["Date", "Satellite_Route_2", "per_run_sal", "count_of"]]
            .set_index(['Date', 'per_run_sal', 'count_of'])
            .apply(lambda x: x['Satellite_Route_2']
            .split('/') if type(x['Satellite_Route_2']) == str else 0, axis=1)
            .explode()
            .reset_index()
            .rename(columns={ 0 : 'route'})
            )

# ===========================
sal_alloc_df = pd.concat([sal_df_1,sal_df_2,sal_df_3])
# ===========================

sal_alloc_df.to_csv(PATH_COMPLETE_DETAIL, index=False)


sal_alloc_df.groupby('route')['per_run_sal'].sum().reset_index().to_csv(PATH_COMPLETE_ALLOC, index=False)


