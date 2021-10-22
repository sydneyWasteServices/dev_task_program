import pandas as pd
import numpy as np



class Toll():
    def __init__(self):
        return

    def process_tollCost(self, df : object):
        
        
        df = df.loc[df['LPN/Tag number'].str.isnumeric()]

        df['Tag_ID'] = pd.to_numeric(df['LPN/Tag number'])

        df['Trip Cost'] = df['Trip Cost'].str.replace('$', '').astype(float)

        df = df.rename(columns={'Start Date': 'Date'})
        
        df = df[['Date', 'Tag_ID', 'Details' ,'Trip Cost']]

        return df


    def merge_rego_tollcost(self, df_tollCost : object, df_tagID : object):
        
        df = pd.merge(df_tollCost, df_tagID, how='left', on='Tag_ID')

        df = df[['Date_x', 'rego','Tag_ID','Details' ,'Trip Cost']]

        df = df.groupby('rego')['Trip Cost'].sum().reset_index()

        return df


    def allocation(self, df_ratio : object, df_tollcost : object):
        
        merge = pd.merge(df_ratio, df_tollcost, how='left', left_on='Primary_truck', right_on='rego')

        merge['toll_cost_per_run'] = merge['Trip Cost'] * merge['portion']

        merge = merge.groupby('Primary_route')['toll_cost_per_run'].sum().reset_index()

        return merge 
