# os.path.dirname(__file__) just gives you the directory that your current python file is in,
#  and then we navigate to 'Common/' the directory and import 'Common' the module.
# data Transform - waste Edge

import sys
import os
sys.path.append(sys.path[0] + "/..")

from report_outlook.component.routes_analysis_component import Routes_analysis_component
import time
import pandas as pd
import xlwings as xw
from report_outlook.component.basic_component import Basic_component as bc
from report_outlook.report_template import Report_template as rt
from revenue.revenue_by_type import Revenue_by_type
from revenue.revenue import Revenue as rev
from data_transform.WE_transform import WE_transform as dt_wet
from data.rate import Rate
from data.routes_analysis_data.routes_info import Routes_info
from data.bins_exp import Bins_exp as bins_exp
from data.admin_exp import Admin_exp as admin_exp
from data.mv_exp import Mv_exp as mv_exp
from data.operating_salary import Operating_salary as salary
from data.operating_exp import Operating_exp as op_exp
from data.operating_inc import Operating_inc as op_inc
from routes_tipping.routes_tipping import Routing_tipping


# from data.routes_analysis_data.all_routes_info import All_routes_info


# ===========================================


# , 'ORGANICS'

tipping_path = "../../../ubuntuShareDrive/Datasets/tipping_monthly/Jan_2021.csv"
booking_path = "../../../ubuntuShareDrive/Datasets/booking_monthly/Jan_2021.csv"

tipping_df = pd.read_csv(tipping_path)

# series_a = [routes_tip_df.route_weight_series(tip) for tip in tiplist]
# print(series_a[1].index)

booking_df = pd.read_csv(booking_path, dtype={
                         "Schd Time Start": str, "PO": str})

# Transform
trans_df = dt_wet().transform_and_clean_Route_num(booking_df)
trans_df = dt_wet().transform_date(booking_df)

# resample df by 7D
resampled_df = rev().resample_by_7d(trans_df)

date_keys = rev().date_keys(resampled_df)

print(date_keys)
print(len(date_keys))

current_date = date_keys[0].date()

df_by_date = rev().get_df_by(resampled_df, current_date)

booking_df = Revenue_by_type(df_by_date)


print(f"current_date is {current_date}")

# =============================================================================================
# Tipping report Dataframe
tipping_df = pd.read_csv(tipping_path)

route_tipping = Routing_tipping()

tipping_df = route_tipping.transform(tipping_df)

tipping_df = route_tipping.drop_no_docket(tipping_df)

tipping_df = Routing_tipping(tipping_df)

# ===========================================================================================

GENERAL_WASTE_TOTAL_INC = booking_df.total_inc('GENERAL_WASTE')
GENERAL_WASTE_INC_SERIES = booking_df.routes_inc_series('GENERAL_WASTE')


print(GENERAL_WASTE_INC_SERIES.index)
print(GENERAL_WASTE_INC_SERIES.values)


revenue_type_list = ['GENERAL_WASTE', 'CARDBOARD', 'COMINGLED']


# def create_routes_info(revenue_type):
#     routes_info_data = (
#         Routes_info(
#             revenue_type,
#             booking_df.total_inc(revenue_type),
#         )
#     )
#     return routes_info_data


def create_routes_info(rev_type : str):
    print(rev_type)
    total_inc = booking_df.total_inc(rev_type)
    print(total_inc)
    total_weight = tipping_df.routes_total_weight(rev_type)
    print(total_weight)
    routes_inc_series = booking_df.routes_inc_series(rev_type)
    print(routes_inc_series)
    routes_weight_series = tipping_df.route_weight_series(rev_type)
    print(routes_weight_series)
    route_info = Routes_info(rev_type, total_inc, total_weight, routes_inc_series, routes_weight_series)
    return route_info
    

routes_info_data = [create_routes_info(rev_type) for rev_type in revenue_type_list]




