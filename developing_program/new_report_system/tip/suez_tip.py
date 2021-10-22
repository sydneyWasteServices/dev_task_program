import pandas as pd
import numpy as np 

class Suez_tip():
    def __init__(self):
        return

    def detail_allocation(self, df_ros_ratio : object, df_suez : object):
        
        df_suezSummary = df_suez.groupby(['Rego'])[['Net (t)','total_price']].sum().reset_index()

        merge_ratio_suezSummary = pd.merge(df_ros_ratio, df_suezSummary, how='left', left_on='Primary_truck', right_on='Rego')

        # Suez in weight per route
        merge_ratio_suezSummary['ton_per_run'] = merge_ratio_suezSummary['Net (t)'] * merge_ratio_suezSummary['tip_portion']

        # Suez in Price per route
        merge_ratio_suezSummary['cost_per_run'] = merge_ratio_suezSummary['total_price'] * merge_ratio_suezSummary['tip_portion']
        
        return merge_ratio_suezSummary

    # def uos_tip

    def allocation(self, df_ros_ratio : object, df_suez : object):
            
        df_suezSummary = df_suez.groupby(['Rego'])[['Net (t)','total_price']].sum().reset_index()

        merge_ratio_suezSummary = pd.merge(df_ros_ratio, df_suezSummary, how='left', left_on='Primary_truck', right_on='Rego')

        # Suez in weight per route
        merge_ratio_suezSummary['ton_per_run'] = merge_ratio_suezSummary['Net (t)'] * merge_ratio_suezSummary['tip_portion']

        # Suez in Price per route
        merge_ratio_suezSummary['cost_per_run'] = merge_ratio_suezSummary['total_price'] * merge_ratio_suezSummary['tip_portion']

        result = merge_ratio_suezSummary.groupby('Primary_route_x')['ton_per_run', 'cost_per_run'].sum().reset_index()

        return result