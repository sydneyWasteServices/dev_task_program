import pandas as pd
import numpy as np


class Waste_edge_fuel_report():
    def __init__(self):
        return

    def fuel_cost(self, df : object, route : str):
        
        df = df.groupby('RouteNumber')['FuelCost'].sum().reset_index()

        result = df[df.RouteNumber.eq(route)].FuelCost.item()

        return result


    def report(self, df : object):
        
        df = df.groupby('RouteNumber')['FuelCost'].sum().reset_index()

        return df


    