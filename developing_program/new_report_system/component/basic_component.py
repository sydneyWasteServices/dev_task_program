import xlwings as xw
# from report_outlook.component.style import Style
from datetime import timedelta 

class Basic_component:
    def __init__(self):
        pass

    def add_n_sheet(
            self,
            wb: object,
            number_sheet : int):
  
        [wb.sheets.add() for n in range(number_sheet)]
