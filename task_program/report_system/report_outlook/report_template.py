import xlwings as xw
import typing
from report_outlook.component.complex_component import Complex_component
from report_outlook.component.routes_analysis_component import Routes_analysis_component


class Report_template(Complex_component, Routes_analysis_component):
    def __init__(self):
        super().__init__()
        return

    def weekly_op_summary(
            self,
            wb: object,
            ws_name: list,
            date: str,
            endDate:str,
            op_inc: object = {},
            op_exp: object = {},
            op_salary: object = {},
            mv_exp: object = {},
            admin_exp: object = {},
            bins_exp: object = {}):

        super().report_headers(
            wb,
            ws_name,
            date,
            endDate,
            "Weekly Financial Report Summary")

    # Anchor Cell at B6
    # Operating Income
    # Table Headers

        op_tb_header = ["Ton", "Rate per Ton", "% of Total Operating Inc"]

        no_tb_header = []

        super().report_formating(
            wb,
            ws_name)

        # Anchor at B10
        # Operating Income
        if op_inc:
            super().session(
                wb,
                ws_name,
                "Operating Income",
                True,
                op_tb_header,
                op_inc,
                10)
        else:
            print("Operating income items is empty")
            return 0

    # Anchor at B24
    # Operating Expense
        if op_exp:
            super().session(
                wb,
                ws_name,
                "Operating Expense",
                False,
                op_tb_header,
                op_exp,
                24)
        else:
            print("Operating Expense items is empty")
            return 0

        if op_salary:
            super().session(
                wb,
                ws_name,
                "Operating Salary",
                False,
                no_tb_header,
                op_salary,
                36)
        else:
            print("Operating Salary items is empty")
            return 0

        if mv_exp:
            super().session(
                wb,
                ws_name,
                "Motor Vehicle Expense",
                False,
                no_tb_header,
                mv_exp,
                43)
        else:
            print("Motor Vehicle expense items is empty")
            return 0

        if admin_exp:
            super().session(
                wb,
                ws_name,
                "General & Administration",
                False,
                no_tb_header,
                admin_exp,
                59)
        else:
            print("Admin expense items is empty")
            return 0

        if bins_exp:
            super().session(
                wb,
                ws_name,
                "Bins Purchase",
                False,
                no_tb_header,
                bins_exp,
                68)
        else:
            print("Bins expense items is empty")
            return 0

        wb.sheets[ws_name].range('B75').value = 'Total Expense'

        wb.sheets[ws_name].range('B77').value = 'Operating Margin'
        wb.sheets[ws_name].range('B78').value = '% Op Margin'

# Small Temporary Modification on report
        ws = wb.sheets[ws_name]
# Headers
    # Per Waste Edge App - Header
        ws.range("M13").value = "Per WE"
        ws.range("M13").api.Font.Size = 13
        ws.range("M13").api.Font.Bold = True
# Coloring the Weekly Summary
    # GW color 230 184 183
        ws.range("K13").color = (230,184,183)
        ws.range("K26").color = (230,184,183)
    # CB color 0 176 240
        ws.range("K14").color = (0,176,240)
    # CM color 255 255 0
        ws.range("K15").color = (255,255,0)
        ws.range("K27").color = (255,255,0)
    # Sub 255 192 0
        ws.range("K16").color = (255,192,0)
        ws.range("K29").color = (255,192,0)
        ws.range("K30").color = (255,192,0)
    # UOS 177 160 199
        ws.range("K17").color = (177,160,199)
        ws.range("M17").color = (177,160,199)
    # FR 146,205,220
        ws.range("K18").color = (166,166,166)
    # CB Rebate
        ws.range("K19").color = (146,205,220)

    
# ===================================================================================

    def by_rev_type(self,
                    wb: object,
                    ws_name: str,
                    date: str,
                    endDate: str,
                    routes_info: object):

        super().report_formating(
            wb,
            ws_name)

        super().report_headers(
            wb,
            ws_name,
            date,
            endDate,
            "Weekly Financial Report Summary")


        (
            super()
            .income_session(wb, ws_name, routes_info)
            .weight_session(wb, ws_name, routes_info, 9)
            .gross_operating_margin(wb, ws_name, routes_info, 13)
        )

        


        # route_op_inc
        # {
        # routesName : [1,2,3,4,5]
        # routesInc : [M1, M2, M3, M4]
        # }
