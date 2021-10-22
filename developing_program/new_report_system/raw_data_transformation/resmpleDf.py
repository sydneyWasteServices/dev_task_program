import pandas as pd
import numpy as np


class ResampleDf():
    def __init__(self):
        return

    def resample_weekly(self, 
                        df: object):
        
        df_groups = df.resample('7D')

        return df_groups

    def resample_monthly(self, 
                        df: object):
        
        df_groups = df.resample('M')

        return df_groups

    def get_groups_key(self,
                       resampled_df : dict):
        return list(resampled_df.groups.keys)

    def get_first_group(self,
                        resampled_df : dict):
        
        first_key = list(resampled_df.groups.keys())[0]

        first_group = resampled_df.get_group(first_key)

        return first_group