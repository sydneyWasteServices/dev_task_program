import pandas as pd
import numpy as np
import xlwings as xw
import glob

if __name__ == "__main__":

    WEEK = "41th_2021"

    PATH_TRANSFORMED_MVEXP = f"D:\\Run Analysis\\blob_storage\\truck_exp_other\\transformed_og_ds\\{WEEK}.csv"

    PATH_ROSTER = f"D:\\Run Analysis\\blob_storage\\roster\\{WEEK}.xlsx"

    PATH_COMPLETE_ALLOC = f"D:\\Run Analysis\\blob_storage\\truck_exp_other\\processed\\{WEEK}_alloc.csv"

    PATH_COMPLETE_DETAIL = f"D:\\Run Analysis\\blob_storage\\truck_exp_other\\processed\\{WEEK}_deatiled.csv"

# =============================================================================================
# =============================================================================================
    # To Find out What turck is sitting in the yard(MYOB account),
    # Not in Roster

    mvexp_df = pd.read_csv(PATH_TRANSFORMED_MVEXP)

    roster_df = pd.read_excel(PATH_ROSTER)

    mvexp_df_trucks_list = mvexp_df['Job No.'].unique()

    pri_trucks = roster_df.dropna(
        subset=['Primary_truck']).Primary_truck.str.replace(' ', '').unique()

    sec_trucks = roster_df.dropna(
        subset=['Alternative_Truck']).Alternative_Truck.str.replace(' ', '').unique()

    roster_df_trucks_list = np.append(pri_trucks, sec_trucks)

    uni_ros_trucks = list(set(roster_df_trucks_list))

    ros_trucks = np.array(uni_ros_trucks)

    # Excel
    trucks_not_in_yard = np.setdiff1d(
        ros_trucks, mvexp_df_trucks_list, assume_unique=True)
    # Excel
    trucks_in_yard = np.setdiff1d(
        mvexp_df_trucks_list, ros_trucks, assume_unique=True)


# =============================================================================================
# =============================================================================================
    def clean_roster_df(df):
        df.Primary_truck = df.Primary_truck.str.replace(" ", "")
        df.Alternative_Truck = df.Alternative_Truck.str.replace(" ", "")
        df = df.fillna(0)
        return df

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
                              .reset_index()
                              .rename(columns={"index": "number_plate", 0: "trucks"})

                              )

    # total_truck_runs_count  -> counting how many runs for the trucks
# =============================================================================================
    # MV expense Join Roster counts
    # Output Cost summary

    mvexp_truckcounts_df = pd.merge(
        mvexp_df, total_truck_runs_count, how="left", left_on='Job No.', right_on='number_plate')

    mvexp_truckcounts_df['per_truck_cost'] = mvexp_truckcounts_df.Debit / \
        mvexp_truckcounts_df.trucks

    mvexp_cost_summary_df = mvexp_truckcounts_df[[
        'Acc_name', 'Job No.', 'per_truck_cost']].dropna(subset=['per_truck_cost'])
# =============================================================================================
# =============================================================================================

    pri_truck_cost = pd.merge(roster_df, mvexp_cost_summary_df, how="left",left_on='Primary_truck', right_on='Job No.')

    alt_truck_cost = pd.merge(roster_df, mvexp_cost_summary_df, how="left", left_on='Alternative_Truck', right_on='Job No.')  

    truck_cost= pd.concat([pri_truck_cost, alt_truck_cost], ignore_index=True)

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
        
        cost = df.per_truck_cost / count
        return cost, count

# # ===========================
# # ===========================

    truck_cost[['per_run_cost', 'count_of']] = truck_cost.apply(per_route_cost, axis=1, result_type='expand')
        
# # =============================================================================
# # Calculating per run Mv expenses

    trucks_cost_summary_1 = (
        truck_cost[truck_cost.Primary_route.ne(0)]
        .drop(columns=['Satellite_Route_1', 'Satellite_Route_2'])
        .rename(columns={"Primary_route": "route"})
    )

    trucks_cost_summary_2 = (
        truck_cost[truck_cost.Satellite_Route_1.ne(0)]
        .drop(columns=['Satellite_Route_2', 'Primary_route'])
        .rename(columns={"Satellite_Route_1": "route"})
    )

    trucks_cost_summary_3 = (
        truck_cost[truck_cost.Satellite_Route_2.ne(0)]
        .set_index(['Date', 'per_run_cost','Acc_name'])
        .apply(lambda x: x['Satellite_Route_2']
               .split('/') if type(x['Satellite_Route_2']) == str else 0, axis=1)
        .explode()
        .reset_index()
        .rename(columns={0: 'route'})
    )

    total_truck_cost_summary = pd.concat([trucks_cost_summary_1, trucks_cost_summary_2, trucks_cost_summary_3], ignore_index=True)

    
    total_truck_cost_summary.to_csv(PATH_COMPLETE_DETAIL, index=False)

    total_truck_cost_summary.groupby(['route', 'Acc_name'])['per_run_cost'].sum().reset_index().sort_values(by='Acc_name').to_csv(PATH_COMPLETE_ALLOC, index=False)

