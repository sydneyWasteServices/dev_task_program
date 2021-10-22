import pandas as pd
import numpy as np


class Rego():
    def __init__(self):
        return
    
    def allocation(self, ratio : object, rego : object):
        
        merge = pd.merge(ratio, rego, how='left', left_on='Primary_truck', right_on='Rego')

        merge['amount'] = merge.weekly_rego_payment * merge.portion

        merge = merge.groupby('Primary_route_x')['amount'].sum().reset_index()

        return merge
