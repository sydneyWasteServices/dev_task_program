import pandas as pd 
import numpy as np
import typing
import xlwings as xw
import glob

from report_outlook.components import Components
from report_outlook.style import Style

if __name__ == "__main__":

    pass

    wb = xw.Book()

# ===========================
# report outlook 
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
    components.period_header_title(wb, "main_report", "10-10-2021", "20-10-2021")

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
    
    
    





