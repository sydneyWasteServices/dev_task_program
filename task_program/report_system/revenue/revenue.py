# Revenue class => critera get DF and rev figure
# summarised data - income , dataset etc
# WatedpIt is categorise based on the runn

# main => init
import pandas as pd
import typing

# df is going to resampling here


class Revenue:
    def __init__(
            self):
        pass

    def resample_by_7d(self, df: object):
        return  df.resample('7D')

    def date_keys(self, df: object):
        return list(df.groups.keys())

    def get_df_by(self,df : object,date_key: str = "dd/mm/yy"):
        return df.get_group(date_key)

    # return key : route, value : figure

    def filter_df_by_rev_routes(self, df: object, list_of_routes : list):
        df = df.filter(items=list_of_routes)
        # df = df[df['Route number'].isin(list_of_routes)]
        return df
