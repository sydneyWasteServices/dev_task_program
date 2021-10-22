import pandas as pd
import numpy as np


WEEK = '31th_2021'

SOURCE_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\fuel\\waste_edge_fuel_transactions\\{WEEK}.xlsx'
COMPLETED_PATH = f'D:\\Run Analysis\\BLOB_STORAGE\\expenses_truck\\fuel\\waste_edge_fuel_transactions\\{WEEK}_processed.csv'

# ,engine='openpyxl'
df = pd.read_excel(SOURCE_PATH)


df[['RouteNumber', 'weekday']]= df.RouteNumber.str.split('-', 1, expand=True)


fuel_route_cost_df = df.groupby('RouteNumber')['FuelCost'].sum().reset_index()


fuel_route_cost_df.to_csv(COMPLETED_PATH, index=True)