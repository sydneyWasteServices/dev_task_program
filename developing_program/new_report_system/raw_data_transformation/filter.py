import pandas as pd
import numpy as np


class Filter():
    def __init__(self):
        return

    def confirmed_only(self, 
                        df : object):
        
        fails_status = ['V','N','F']

        df = df[~df['Status'].isin(fails_status)]
        
        return df

