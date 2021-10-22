import pandas as pd 
import numpy as np


class Cleaner():
    def __init__(self):
        return

    def cleanNsplit_routes(
            self,
            df : object,
            route_col_name : str):

            # df['Route number'] = df['Route number'].astype('str')

            df[[route_col_name, 'Weekday']] = df[route_col_name].str.split('-', 1, expand=True)

            return df
            
    
