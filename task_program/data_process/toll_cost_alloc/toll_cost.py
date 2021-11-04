import pandas as pd
import numpy as np
import xlwings as xw

WEEK = "40th_2021"

PATH_TAG_ID = "D:\\Run Analysis\\blob_storage\\toll_id.csv"

PATH_TOLL = f"D:\\Run Analysis\\blob_storage\\truck_toll\\{WEEK}.csv"

PATH_ROS = f"D:\\Run Analysis\\blob_storage\\roster\\{WEEK}.xlsx"


tagid_df = pd.read_csv(PATH_TAG_ID)

tollCost_df = pd.read_csv(PATH_TOLL)

roster_df = pd.read_excel(PATH_ROS)

# =============================================================================================


def clean_tollCost_df(df):
    df = df.loc[df['LPN/Tag number'].str.isnumeric()]
    df['tag_serial_number'] = pd.to_numeric(df['LPN/Tag number'])
    df['tag_serial_number'] = pd.to_numeric(df['tag_serial_number'])
    df['Trip Cost'] = df['Trip Cost'].str.replace('$', '').astype(float)
    df = df.rename(columns={'Start Date': 'Date', "Trip Cost": "trip_cost"})
    df.Date = pd.to_datetime(df.Date, format="%d/%m/%Y %H:%M")
    df = df[['Date', 'Details', 'trip_cost', 'tag_serial_number']]
    return df


def clean_roster_df(df):
    df.Primary_truck = df.Primary_truck.str.replace(" ", "")
    df.Alternative_Truck = df.Alternative_Truck.str.replace(" ", "")
    df = df.fillna(0)
    return df

# =============================================================================================


tollCost_df = clean_tollCost_df(tollCost_df)

roster_df = clean_roster_df(roster_df)


pri_truck_runs_count = roster_df.Primary_truck.value_counts()
sec_truck_runs_count = roster_df.Alternative_Truck.value_counts()

# =============================================================================================
# Counting Trucks runs
total_truck_runs_count = (pd
                          .concat([pri_truck_runs_count, sec_truck_runs_count])
                          .reset_index()
                          .groupby('index')
                          .sum().iloc[1:]
                          .rename(columns={0: "runs"})
                          )
# =============================================================================================
# Join TagId table to TollCost Table to join Cost to truck Number Plate

tollCost_per_truck_df = (pd
                         .merge(tollCost_df, tagid_df, how='left', on='tag_serial_number')
                         .groupby('number_plate')['trip_cost']
                         .sum()
                         .reset_index())


# =============================================================================================
# Join Truck Toll Cost to Truck Runs count to get result of per run toll cost

proof_of_toll = (pd
                         .merge(
                             tollCost_per_truck_df,
                             total_truck_runs_count,
                             how='left',
                             left_on='number_plate',
                             right_on='index'))


per_runs_toll_cost_df = (pd
                         .merge(
                             tollCost_per_truck_df,
                             total_truck_runs_count,
                             how='left',
                             left_on='number_plate',
                             right_on='index')
                         .dropna())

per_runs_toll_cost_df['per_run_toll_cost'] = per_runs_toll_cost_df.trip_cost / per_runs_toll_cost_df.runs

toll_cost_per_truck_per_shift_df = per_runs_toll_cost_df[['number_plate', 'per_run_toll_cost']]
# =============================================================================================
# Join per run Toll cost for Primary Truck Toll cost
tollCost_dict = toll_cost_per_truck_per_shift_df.set_index('number_plate')['per_run_toll_cost'].to_dict()


roster_df['pri_truck_toll_cost'] = roster_df.apply(lambda x : tollCost_dict[x['Primary_truck']] if x['Primary_truck'] in tollCost_dict else 0, axis=1)


roster_df['sec_truck_toll_cost'] = roster_df.apply(lambda x : tollCost_dict[x['Alternative_Truck']] if x['Alternative_Truck'] in tollCost_dict else 0, axis=1)

roster_df['toll_cost'] = roster_df['pri_truck_toll_cost']  + roster_df['sec_truck_toll_cost'] 

# =============================================================================================
# Split total cost by runs 

roster_df = roster_df[['Date', 'toll_cost', 'Primary_route', 'Satellite_Route_1','Satellite_Route_2']]

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
    
    cost = df.toll_cost / count
    return cost, count

roster_df[['per_run_toll', "count_of"]] = roster_df.apply(per_route_cost, axis=1, result_type='expand') 

# ==============================================================================
# Per run toll cost dataframe



roster_df[['per_run_sal', "count_of"]] = roster_df.apply(per_route_cost, axis=1, result_type='expand') 

ros_df_1 = roster_df[roster_df.Primary_route.ne(
    0)][["Date", "Primary_route", "per_run_sal", "count_of"]].rename(columns={'Primary_route': 'route'})

ros_df_2 = roster_df[roster_df.Satellite_Route_1.ne(
    0)][["Date", "Satellite_Route_1", "per_run_sal", "count_of"]].rename(columns={'Satellite_Route_1': 'route'})

ros_df_3 = (roster_df[roster_df.Satellite_Route_2.ne(0)][["Date", "Satellite_Route_2", "per_run_sal", "count_of"]]
            .set_index(['Date', 'per_run_sal', 'count_of'])
            .apply(lambda x: x['Satellite_Route_2']
            .split('/') if type(x['Satellite_Route_2']) == str else 0, axis=1)
            .explode()
            .reset_index()
            .rename(columns={ 0 : 'route'})
            )

toll_alloc_df = pd.concat([ros_df_1,ros_df_2 ,ros_df_3])

PATH_DETAIL_ALLOC = f"D:\\Run Analysis\\blob_storage\\truck_toll\\processed\\{WEEK}_detailed.csv"

PATH_ALLOC = f"D:\\Run Analysis\\blob_storage\\truck_toll\\processed\\{WEEK}.csv"

PATH_PROOF_OF_TOLL =  f"D:\\Run Analysis\\blob_storage\\truck_toll\\processed\\{WEEK}_proof_of_toll.csv"

toll_alloc_df.to_csv(PATH_DETAIL_ALLOC, index=False)

toll_alloc_df.groupby('route')['per_run_sal'].sum().reset_index().to_csv(PATH_ALLOC, index=False)


proof_of_toll.to_csv(PATH_PROOF_OF_TOLL, index=False)   