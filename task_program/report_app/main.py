import pandas as pd 
import numpy as np
import typing
import xlwings as xw
import glob
import datetime
from datetime import datetime 


from report_outlook.components import Components
from report_outlook.style import Style
from report_data.total_info import Total_info 
from raw_data_transformation.incomes import Incomes
from raw_data_transformation.routes_list import By_Revenue_type  
from report_data.route_info import Route_info
from utils.utils import Utils 
from tip.waste_edge import Waste_edge


if __name__ == "__main__":
    WEEK = "42th_2021"
# =================================================
# Booking 

    PATH_BOOKING = f"D:\\Run Analysis\\blob_storage\\booking\\processed\\{WEEK}.csv"

    booking_df = pd.read_csv(PATH_BOOKING)

    startDate = booking_df.iloc[0,1]
    
    endDate = booking_df.iloc[-1,1]
    
    reformat_startDate = datetime.strptime(startDate, '%Y-%m-%d').strftime('%d/%m/%Y')

    reformat_endDate = datetime.strptime(endDate, '%Y-%m-%d').strftime('%d/%m/%Y')

    
# =================================================
# Tipping Waste Edge
    

    PATH_WE = f"D:\\Run Analysis\\blob_storage\\tip_waste_edge\\processed\\{WEEK}.csv"

    weTipping_df = pd.read_csv(PATH_WE)


# ===========================
# report outlook 

    wb = xw.Book()

    wb.sheets[0].name = "main_report"

    main_report = wb.sheets["main_report"]
    
# main report styling
    main_report.range('A1').column_width = 1.0
    main_report.range('B1').column_width = 8.5
    main_report.range('C1').column_width = 1
    main_report.range('J1').column_width = 1
    
    main_report.range('A9').row_height = 8
    main_report.range('A15').row_height = 8
    main_report.range('A29').row_height = 8


# Form Header
# =====================

    style = Style()

    components = Components()

    style.fonts_arialify(wb, "main_report")

    components.report_header_title(wb, "main_report")
    
    # date
    components.period_header_title(wb, "main_report", reformat_startDate, reformat_endDate)

# =====================

# Form Session - Reveune

    components.session_title(wb, "main_report", "B5", 12, "Recenue / Run")

    components.session_title(wb, "main_report", "B6", 12, "% of the Total Revenue")
    
# Form Session - Direct Cost session

    components.session_title(wb, "main_report", "B8", 12, "Add : Recycling Income(CB)")

    components.session_title(wb, "main_report", "B10", 12, "Less : Direct Cost")

    components.session_title(wb, "main_report", "C11", 11, "Tipping", False)

    components.session_title(wb, "main_report", "D12", 11, "General Waste", False)

    components.session_title(wb, "main_report", "D13", 11, "Mixed Recycling", False)

    components.session_title(wb, "main_report", "C14", 11, "Wages", False)

    components.session_title(wb, "main_report", "C16", 12, "Total : Direct Cost", True)

# Motor Vehicle
    components.session_title(wb, "main_report", "B18", 12, "Less : Motor Vehicle Expenses", True)

    components.session_title(wb, "main_report", "C19", 11, "MV - Fuel", False)

    components.session_title(wb, "main_report", "C20", 11, "MV - Rego", False)

    components.session_title(wb, "main_report", "C21", 11, "MV - Tolls", False)

    components.session_title(wb, "main_report", "C22", 11, "MV - Insurance", False)

    components.session_title(wb, "main_report", "C23", 11, "Repair & Maintenance - Cab & Chassic", False)

    components.session_title(wb, "main_report", "C24", 11, "Repair & Maintenance - Compactor / Body", False)

    components.session_title(wb, "main_report", "C25", 11, "Repair & Maintenance - Misc. Consumables", False)

    components.session_title(wb, "main_report", "C26", 11, "Repair & Maintenance - Tyres", False)
    
    components.session_title(wb, "main_report", "C27", 11, "Workshop Contractor Labour", False)

    components.session_title(wb, "main_report", "C28", 11, "MV exp - Others ", False)

    components.session_title(wb, "main_report", "C30", 12, "Total : Motor Vehicle Expense ", True)
    
# General & Admin
 
    components.session_title(wb, "main_report", "B32", 12, "Less : General & Administration", True)
    
    components.session_title(wb, "main_report", "C33", 11, "General & Administration", False)

    components.session_title(wb, "main_report", "C34", 11, "Business Promotion", False)

    components.session_title(wb, "main_report", "C35", 11, "Occupancy Cost", False)
    
    components.session_title(wb, "main_report", "C36", 12, "Total General & Administration", True)
    
# Op Margin

    components.session_title(wb, "main_report", "B38", 12, "Operating Margin", True)

    components.session_title(wb, "main_report", "B39", 12, "% Op Margin", True)
    
# Routes list - by type
   

    all_routes = []

    indie_routes = {}

    gw = sorted(By_Revenue_type['GENERAL_WASTE'].value)
    cm = sorted(By_Revenue_type['COMINGLE'].value)
    cb = sorted(By_Revenue_type['CARDBOARD'].value)

    uos = sorted(By_Revenue_type['UOS'].value)
    
    all_routes.append(gw)
    all_routes.append(cm)
    all_routes.append(cb)
    all_routes.append(uos)


    agg_gw = By_Revenue_type['AGG_GENERAL_WASTE'].value
    agg_cb = By_Revenue_type['AGG_CARDBOARD'].value
    agg_cm = By_Revenue_type['AGG_COMINGLE'].value


# =============================
# Module Objects
    utils = Utils()

    incomes = Incomes()

    tip_waste_edge = Waste_edge()

# =======================================================================================================
# Populate Total info Object 

    total = Total_info()
    
    all_routes = utils.flatten(all_routes)

    total.income = incomes.group_income(booking_df, all_routes)

# ======================================================================================================
# Populate to excel spread sheet
# 
#  



# Indie Route title starts

    indie_route_title_start_row = 4
    indie_route_title_start_column = 11


# Populate All "routes Title" Excel location and route info Object 
    for route in all_routes:
        
        # ================================
        # Populate to Object
        # Fill route_info Object and then populate object to  "indie_routes"   indie_routes.Route_name  
        route_info = Route_info(route)        
        
        route_info.address_in_total_sheet = wb.sheets["main_report"].range((indie_route_title_start_row, indie_route_title_start_column))

        indie_routes[route_info.route_name] = route_info

        components.route_title(indie_routes[route].address_in_total_sheet, 13, route_info.route_name)

        indie_route_title_start_column = indie_route_title_start_column + 1

# Populate "Income" into Excel and route info Object
    for route in all_routes:

        indie_routes[route].income = incomes.indie_route_income(booking_df, route)

        indie_routes[route].address_in_total_sheet.offset(row_offset=1).value = indie_routes[route].income

# Populate "General Waste cost" into Excel and route info Object
    for route in agg_gw:
        
        indie_routes[route].gw_waste_edge_cost = tip_waste_edge.indie_gw_cost(weTipping_df, route)
        
        indie_routes[route].address_in_total_sheet.offset(row_offset=8).value = indie_routes[route].gw_waste_edge_cost

# Populate "Cardboard cost" into Excel and route info Object

    for route in agg_cb:

        indie_routes[route].cb_cost = tip_waste_edge.indie_cb_cost(weTipping_df, route)

        indie_routes[route].address_in_total_sheet.offset(row_offset=4).value = indie_routes[route].cb_cost

# Populate "Comingle cost" into Excel and route info Object

    for route in agg_cm:
    
        indie_routes[route].cm_cost = tip_waste_edge.indie_cm_cost(weTipping_df, route)

        indie_routes[route].address_in_total_sheet.offset(row_offset=9).value = indie_routes[route].cm_cost
    
    



    SAVE_PATH  = f"D:\\Run Analysis\\WEEKLY_SUMMARY\\reports\\{WEEK}_{startDate}_{endDate}.xlsx"
    
    wb.save(SAVE_PATH)

    wb.close()

    


        # route_info.income = incomes.indie_route_income(booking_df, route)

        # # ================================

        # # ================================
        # # Populate to Excel Spread sheet
        

        # 

        # # ================================

        # # From start to Next route Column location in Excel Spread sheet 

        # print(route_info.address_in_total_sheet)
