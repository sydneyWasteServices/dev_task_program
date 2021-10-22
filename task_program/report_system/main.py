# data Transform - waste Edge
from data.operating_inc import Operating_inc as op_inc
from data.operating_exp import Operating_exp as op_exp
from data.operating_salary import Operating_salary as salary
from data.mv_exp import Mv_exp as mv_exp
from data.admin_exp import Admin_exp as admin_exp
from data.bins_exp import Bins_exp as bins_exp

from data.routes_analysis_data.routes_info import Routes_info
# from data.routes_analysis_data.all_routes_info import All_routes_info

from data.rate import Rate
from data_transform.WE_transform import WE_transform as dt_wet
from revenue.revenue import Revenue as rev
from revenue.revenue_by_type import Revenue_by_type
from routes_tipping.routes_tipping import Routing_tipping

from report_outlook.report_template import Report_template as rt
from report_outlook.component.basic_component import Basic_component as bc

import xlwings as xw
import pandas as pd
from datetime import timedelta

# Fixed as Weds to Tues
# Start with df, suppose it is querying from Wed
# dataframe in new downloaded folder
# dataVault\waste_edge_booking_data\23.12.2020_to_26.1.2021
# $ /c/Users/gordon/Desktop/

# Only Count Confirms - Since it  ['V','N','F','R'] Status, not confirm to get paid 

booking_path = 'D:\\Run Analysis\\blob_storage\\booking\\41th_2021.csv'

tipping_path = 'D:\\Run Analysis\\blob_storage\\tip_waste_edge\\41th_2021.csv'

list_rev_types = ['GENERAL_WASTE',
                  'CARDBOARD',  
                  'COMINGLED',
                  'SUBCONTRACTED',
                  'UOS',
                  'TOTAL']

list_report_sheets = ['WEEKLY_SUMMARY',
                      'TOTAL',
                      'GENERAL_WASTE',
                      'CARDBOARD',
                      'COMINGLED',
                      'SUBCONTRACTED',
                      'UOS']

df = pd.read_csv(booking_path, dtype={"Schd Time Start": str, "PO": str})

no_pay_status = ['V','N','F']

df = df[~df['Status'].isin(no_pay_status)]

# Transform
trans_df = dt_wet().transform_and_clean_Route_num(df)
trans_df = dt_wet().transform_date(df)

# resample df by 7D
resampled_df = rev().resample_by_7d(trans_df)

date_keys = rev().date_keys(resampled_df)

print(date_keys)
# print(len(date_keys))

current_date = date_keys[0].date()

# Day include the selected date so is days=6
end_date = date_keys[0].date() + timedelta(days=6)

df_by_date = rev().get_df_by(resampled_df, current_date)

booking_df = Revenue_by_type(df_by_date)

print(f"current_date is {current_date}")

# =============================================================================================
# Tipping report Dataframe
tipping_df = pd.read_csv(tipping_path, encoding = "ISO-8859-1")

route_tipping = Routing_tipping()

tipping_df = route_tipping.transform(tipping_df)

tipping_df = route_tipping.drop_no_docket(tipping_df)

tipping_df = Routing_tipping(tipping_df)

# ===========================================================================================

# D:\Operations\PAIGE\Tonnes of PC & Co-mingle
# TOTAL
# GENERAL_WASTE
# CARDBOARD
# COMINGLED
# SUBCONTRACTED
# UOS

total_inc = booking_df.total_inc('TOTAL')
gw_inc = booking_df.total_inc('GENERAL_WASTE')
cb_inc = booking_df.total_inc('CARDBOARD')
cm_inc = booking_df.total_inc('COMINGLED')
sub_inc = booking_df.total_inc('SUBCONTRACTED')
uos_inc = booking_df.total_inc('UOS')
# rate data => General Waste, Cardboard, Comingle, Organics
rate = Rate(265, 150, 190, 240)
fr_inc = 57038


current_op_inc = op_inc(total_inc, gw_inc, cb_inc, cm_inc,
                        sub_inc, uos_inc, fr_inc, rate.CARDBOARD)

current_op_exp = (op_exp(
    rate.GENERAL_WASTE,
    rate.COMINGLED,
    rate.ORGANICS,
    0.03, 0.0132, 0.003))


current_op_salary = salary(0.303)
current_mv_exp = mv_exp(0.03, 0.0046, 0.0086, 0.0122,
                        0.0178, 0.013, 0.0006, 0.0039, 0.012, 0.0024)
current_admin_exp = admin_exp(0.0218, 0.011, 0.0243)
current_bin_exp = bins_exp(0.0132)

report_bc_tools = bc()

wb = report_bc_tools.open_wb()

# Add All Sheets
report_bc_tools.add_sheets(wb, list_report_sheets)

weekly_report = rt()

(weekly_report
    .weekly_op_summary(
        wb,
        "WEEKLY_SUMMARY",
        current_date,
        end_date,
        current_op_inc,
        current_op_exp,
        current_op_salary,
        current_mv_exp,
        current_admin_exp,
        current_bin_exp
    )
 )

# ['GENERAL_WASTE', => GW
# 'CARDBOARD', => CB
# 'COMINGLED', => CM
# 'SUBCONTRACTED', => Nothing
# 'UOS', => GW
# 'TOTAL']

def create_routes_info(rev_type: str):
    total_inc = booking_df.total_inc(rev_type)
    total_weight = tipping_df.routes_total_weight(rev_type)

    # routes_inc_series =>  returns numpy object
    routes_inc_series = booking_df.routes_inc_series(rev_type)
    routes_weight_series = tipping_df.route_weight_series(rev_type)

# ============================
# Pick rate 
    def rate_switcher(type_choice: str):
        switcher = {
            'GENERAL_WASTE': rate.GENERAL_WASTE,
            'CARDBOARD' : rate.CARDBOARD ,
            'COMINGLED' : rate.COMINGLED ,
            'SUBCONTRACTED' : 0,
            'UOS' : {
                'GW': rate.GENERAL_WASTE,
                'CB': rate.CARDBOARD,
                'CO': rate.COMINGLED
            },
            'TOTAL' : 0
            }        
        return switcher.get(type_choice)

    route_rate = rate_switcher(rev_type)
# ============================
    route_info = (
        Routes_info(
            rev_type,
            total_inc,
            total_weight,
            routes_inc_series,
            routes_weight_series,
            route_rate)
    )

    return route_info


routes_info_data = [create_routes_info(rev_type)
                    for rev_type in list_rev_types]

(
    [weekly_report
     .by_rev_type(wb,
                  route_info_data.rev_type,
                  current_date,
                  end_date,
                  route_info_data)
     for route_info_data in routes_info_data]
)


# self.rev_type = rev_type
# self.total_inc = total_inc
# self.total_weight = total_weight
# self.booking_price_series = booking_price_series
# self.tipping_weight_series = tipping_weight_series

# list_rev_types = ['GENERAL_WASTE',
#                   'CARDBOARD', 'COMINGLED', 'SUBCONTRACTED', 'UOS', 'TOTAL']

wb.save(f'D:\\Run Analysis\\WEEKLY_SUMMARY\\{str(current_date)}.xlsx')
wb.close()
