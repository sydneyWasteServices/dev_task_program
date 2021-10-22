import pandas as pd
import numpy as np
import glob

# To generate a ratio list of MV items 

PATH_OLDROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\Rearranged_past_roster\\All_Past_Sorted_ROSTER.csv'
PATH_CURROS = 'D:\\Run Analysis\\BLOB_STORAGE\\Roster\\weekly_roster_processed'


# Process Old Roster df
df_old_ros = pd.read_csv(PATH_OLDROS)

# Clean Date and time
df_old_ros.Date = df_old_ros.Date.str.split(' ', 1 ,expand=True)[0]

df_old_ros.Date = pd.to_datetime(df_old_ros.Date, format='%d/%m/%Y')

# Old Roster Dataframe must be selected before 06 Apr 2021 - 
# Since we have Current Roster from 07 Apr 2021
df_old_ros = df_old_ros.loc[df_old_ros.Date <= '20210406' ]

# Current Roster Started from 
df_cur_ros = pd.concat(map(pd.read_excel, glob.glob(f'{PATH_CURROS}//*.xlsx')))