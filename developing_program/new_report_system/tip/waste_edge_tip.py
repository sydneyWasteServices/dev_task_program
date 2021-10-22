import pandas as pd
import numpy as np 

class Waste_edge_tip():
    def __init__(self):
        return

    def filter(self, df : object):
        df = df[df['Gross Weight'].gt(0)]

        df = df[df['Tare Weight'].gt(0)]
        
        return df

    def route_tip(self, df : object):
        result = df.groupby('Route No').Weight.sum()
        return result


    
    # def weight(self, df : object):
        