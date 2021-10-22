import pandas as pd
import numpy as np
from datetime import timedelta 


class Transform_date():
    def __init__(self):
        return

    def datify(self, 
               df : object,
               date_col_name : str,
               format : str,
               coerce : str = 'coerce'):

        df.loc[:,date_col_name] = pd.to_datetime(df.loc[:,date_col_name], format=format, errors=coerce)

        return df

    def indexitfy(self,
                df : object,
                date_col_name : str):
    
        return df.set_index(df.loc[:,date_col_name],inplace=False).sort_index()

    def last_idxDate(
        self,
        df : object,
        idxDate_col_name : str):

        return str(df[idxDate_col_name].sort_index().iloc[-1,].date())

    def first_date(
                self,
                df : object,
                date_col_name : str):
                
        return str(df[date_col_name].sort_values().iloc[0,].date())

    def last_date(
                self,
                df : object,
                date_col_name : str):
                
        return str(df[date_col_name].sort_values().iloc[-1,].date())



    def first_idxdate(
            self,
            df : object,
            date_col_name : str):
            
        return str(df[date_col_name].sort_index().iloc[0,].date())

    def last_idxdate(
            self,
            df : object,
            date_col_name : str):
            
        return str(df[date_col_name].sort_index().iloc[-1,].date())

    def sevenDay_after_date(self,
                            date_timestamp : object):
        
        result = date_timestamp.date() + timedelta(days=6)
        
        return result 


    