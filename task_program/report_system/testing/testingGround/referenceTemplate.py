

def add_sheets(
            self,
            wb: object,
            list_of_wsname=[]):
        
        num_list_of_wsname = len(list_of_wsname)
        num_sheets = len(wb.sheets)

        if num_list_of_wsname > num_sheets:
            add_num_sheets = num_list_of_wsname - num_sheets
            [wb.sheets.add() for n in range(add_num_sheets)]

        for i, wsname in enumerate(list_of_wsname):
            wb.sheets[i].name = wsname