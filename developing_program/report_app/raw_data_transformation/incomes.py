import pandas as pd
import numpy as np


class Incomes:
    def __init__(self):
        return

    def group_income(
            self,
            df: object,
            list_of_routes: list):

        result = df[df.Route_number.isin(list_of_routes)].excl_gst_price.sum()

        return result

    def indie_route_income(
            self,
            df: object,
            list_of_routes: list):

        route = []

        route.append(list_of_routes)

        result = df[df.Route_number.isin(route)].excl_gst_price.sum()

        return result
