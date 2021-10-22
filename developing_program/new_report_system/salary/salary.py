import pandas as pd
import numpy as np


class Salary():
    def __init__(self):
        return

    def lowercase_ID(self, df : object):

        df['EmpID'] = df.EmpID.str.lower()
        
        return df 

        

    def detail_allocation(self, df_ros: object, df_sal: object):
        df_ros.Primary_employeeID = df_ros.Primary_employeeID.str.strip()
        merge = pd.merge(df_ros, df_sal, how='left',
                         left_on='Primary_employeeID', right_on='EmpID')

        merge['cost_per_run'] = merge.portion * merge.Total_payment

        merge = merge[['Primary_employeeID', 'Primary_route', 'portion', 'Total_payment', 'cost_per_run']]

        return merge

    def allocation(self, df_ros: object, df_sal: object):
        
        df_sal = df_sal[['EmpID','Total_payment']]
        # print(df_sal)
        df_ros = df_ros[['Primary_employeeID', 'Primary_route', 'portion']]
        # print(df_ros)

        merge = pd.merge(df_ros, df_sal, how='left',left_on='Primary_employeeID', right_on='EmpID')

        merge['cost_per_run'] = merge.portion * merge.Total_payment

        merge = merge[['Primary_route', 'cost_per_run']].groupby('Primary_route')['cost_per_run'].sum().reset_index()

        return merge
