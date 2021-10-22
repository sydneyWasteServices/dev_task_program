import pandas as pd
import numpy as np


class Incomes:
    def __init__(self):
        return

    def types_income(
        self,
        df : object,
        list_of_routes : list):
        
        df_type_inc = df[df['Route number'].isin(list_of_routes)]

        result = df_type_inc.Price.sum()

        return result 


    def routes_income(
        self,
        df : object,
        list_of_routes : list):
        
        df_type_inc = df[df['Route number'].isin(list_of_routes)]    
        
        df_routes_income = df_type_inc.groupby('Route number')['Price'].sum().sort_index().reset_index()

        return df_routes_income


    def all_route_income(
        self,
        df : object):

        result = df.groupby('Route number').Price.sum()        

        return result 
