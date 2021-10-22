import pandas as pd
import numpy as np
import glob


class Mv_exp():
    def __init__(self):
        return



    def filter_df_by(
        self, 
        df : object, 
        runs : list = []):

        df = df[df.Primary_route.isin(runs) & df.Primary_truck.ne('??????')]              

        return df


    def df_concat(self, path : str):
        df = pd.concat(map(pd.read_excel, glob.glob(f'{path}\\*.xlsx')))
        
        return df

    
    def allocation(self, all_roster : object, df_mv_exp : object):
        
        occurrence = all_roster.groupby(['Primary_truck', 'Primary_route'])['Run_type'].count().reset_index()     

        total = all_roster.groupby('Primary_truck')['Run_type'].count().reset_index()

        table_ratio = pd.merge(occurrence, total, on='Primary_truck', how='left')        

        table_ratio['portion'] = table_ratio.Run_type_x /  table_ratio.Run_type_y

        table_ratio = table_ratio[['Primary_truck','Primary_route', 'portion']]

        table_mvexp_ratio = pd.merge(df_mv_exp, table_ratio, left_on='Job No.', right_on='Primary_truck')

        table_mvexp_ratio['amount'] = table_mvexp_ratio.portion * table_mvexp_ratio.Debit 

        table_mvexp_ratio = table_mvexp_ratio.drop(columns=['Debit','Memo', 'Job No.'])

        table_mvexp_ratio = table_mvexp_ratio.groupby(['catID','Primary_route'])['amount'].sum()

        return table_mvexp_ratio