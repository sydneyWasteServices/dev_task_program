import pandas as pd
import numpy as np
import xlwings as xw
import glob 

if __name__ == "__main__":

    WEEK = "40th_2021"

    PATH_TRANSFORMED_MVEXP = f"D:\\Run Analysis\\blob_storage\\truck_exp_other\\transformed_og_ds\\{WEEK}.csv"

    PATH_ROSTER = f"D:\\Run Analysis\\blob_storage\\roster\\{WEEK}.xlsx" 

# =============================================================================================
# =============================================================================================
    # To Find out What turck is sitting in the yard(MYOB account), 
    # Not in Roster

    
    mvexp_df = pd.read_csv(PATH_TRANSFORMED_MVEXP)

    roster_df = pd.read_excel(PATH_ROSTER)


    mvexp_df_trucks_list = mvexp_df['Job No.'].unique()


    pri_trucks = roster_df.dropna(subset=['Primary_truck']).Primary_truck.str.replace(' ','').unique()

    sec_trucks = roster_df.dropna(subset=['Alternative_Truck']).Alternative_Truck.str.replace(' ','').unique()

    roster_df_trucks_list = np.append(pri_trucks, sec_trucks)

    uni_ros_trucks = list(set(roster_df_trucks_list))

    ros_trucks = np.array(uni_ros_trucks)

    # Excel 
    trucks_not_in_yard = np.setdiff1d(ros_trucks,mvexp_df_trucks_list  ,assume_unique=True)
    # Excel 
    trucks_in_yard = np.setdiff1d(mvexp_df_trucks_list,ros_trucks  ,assume_unique=True)



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
                            .rename(columns={"index" : "number_plate", 0: "runs"})
                            
                            )


# =============================================================================================
    # MV expense Join Roster counts

    mvexp_truckcounts_df = pd.merge(mvexp_df, total_truck_runs_count, how="left", left_on='Job No.', right_on='number_plate')

    mvexp_truckcounts_df['per_run_mv_cost'] = mvexp_truckcounts_df.Debit / mvexp_truckcounts_df.runs

    