import pandas as pd
import numpy as np

class Waste_edge():
    def __init__(self):
        return

    def group_gw_cost(self):
        pass

    def group_cb_cost(self):
        pass

    def group_gw_cost(self):
        pass

    def indie_gw_cost(self,
                      df: object,
                      list_of_routes: list):
        route = []

        route.append(list_of_routes)

        result = df[df.Route_number.isin(route)].General_waste_cost.sum()

        return result

    def indie_cb_cost(self,
                      df: object,
                      list_of_routes: list):
        route = []

        route.append(list_of_routes)

        grima_result = df[df.Route_number.isin(route)].Cardboard_Grima_rebate.sum()

        poly_result = df[df.Route_number.isin(route)].Cardboard_Poly_rebate.sum()

        result = grima_result + poly_result

        return result

    def indie_cm_cost(self,
                      df: object,
                      list_of_routes: list):
        route = []

        route.append(list_of_routes)

        result = df[df.Route_number.isin(route)].Comingle_cost.sum()

        return result
