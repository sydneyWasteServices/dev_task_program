

class Locator:
    def __init__(self):
        return
    

    def get_route_header_address(
        self,
        workbook : object,
        worksheet,
        start_row : int, 
        start_column : int):    

        route_header_addresses = {}

        end_column = workbook.sheets[worksheet].range((start_row, start_column)).end('right').column
        # Route Value : Address 

        # Shift Column and get address 
        for i in range(start_column, end_column):
            route = workbook.sheets[worksheet].range((start_row, i)).value
            route_header_addresses[route] = workbook.sheets[worksheet].range((start_row, i)).get_address(True, False, True)
            


        return route_header_addresses
    
#     >>> import xlwings as xw
# >>> wb = xw.Book()
# >>> xw.Range((1,1)).get_address()
# '$A$1'
# >>> xw.Range((1,1)).get_address(False, False)
# 'A1'
# >>> xw.Range((1,1), (3,3)).get_address(True, False, True)
# 'Sheet1!A$1:C$3'
# >>> xw.Range((1,1), (3,3)).get_address(True, False, external=True)
# '[Book1]Sheet1!A$1:C$3'