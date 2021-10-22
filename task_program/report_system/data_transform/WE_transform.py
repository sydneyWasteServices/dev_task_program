# This class is to transform and clean dataframe before we ever start extracting
import pandas as pd
import numpy as np
import re
import typing
from enum import Enum


# WE stands for WasteEdge
# df : dataFrame
class WE_transform():
    def __init__(self):
        pass

    def transform_and_clean_Route_num(
            self,
            df: object):

        df['Route number'] = df['Route number'].astype('str')
        df[['Route number', 'weekday']] = df['Route number'].str.split(
            '-', 1, expand=True)
        return df

    # dataframe type with   DATE column
    # transform date into date time index for resample

    def transform_date(
            self,
            df: object):

        df['Date_idx'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
        # df['Date'] = pd.DatetimeIndex(df['Date'])
        
        return df.set_index(df['Date_idx'], inplace=False)
    
    # Sort by date Desc

    # def sort_by_date_desc(self, df):
    #     return df.sort_values(by=['Date'], inplace=True, ascending=False)

    # df.sort(['Peak', 'Weeks'], ascending=[True, False], inplace=True)
