import time
import xlwings as xw
import openpyxl
import typing
# sht = xw.Book().sheets[0]
# sht.range('A1').value = "hello_world"
# sht.save()

# xw.books.add()
# xw.sheets.view()

# Open the excel app
# app1 = xw.App()
# app1.Book()

# xw.Book('bigbigshop').sheets
# xw.view(sht)

# Range in sheet
# xw.Range('A1')
# xw.Range('A1:C3')
# xw.Range((1,1))
# xw.Range((1,1), (3,3))
# xw.Range('NamedRange')
# xw.Range(xw.Range('A1'), xw.Range('B2'))



# wb = openpyxl.load_workbook(filePath)
# sheet = wb['Sheet1']

# for command in params.split(',')
# command_params = command.split('|')

# # coordinate = command

# rows = sheet
# .iter_rows(

# )

# workbook_path = 'abc.xlsx'8
# wb = xw.Book(workbook_path)
# ============================================

# list_of_values = [1, 2, 3]
# wb = xw.Book()
# ws = wb.sheets['sheet1']
# ws1 = wb.sheets[1]

# ws1.name = "lol"
# wb.sheets[2].delete()

# ws.range('A1').value = list_of_values
# ws1.range((2,1)).value = 'hello world'

# wb.save('abc.xlsx')
# wb.close()

# ============================================
# (name='Arial', size=14)




# Set Font character style 
# ws.range("A:AI").api.Font.Name = "Arial"
# ws.range('A1').column_width = 1.0
# ws.range('A1').value = 'Hello world'

# list of route sheet 
# color them


# List of route name => should be dynamic from local Db


def format_ws(ws_name : str):
    # try catch the worksheet name 
    


    # Ttile   => started at date 
    
    # Report content 
    ws.range('B4').value = "Income"
    ws.range('B5').value = "Revenue"

    ws.range('B4').api.Font.Bold = True
# ====================================


wb = xw.Book()
list_of_route_name = ['General_Waste', 'Cardboard', 'Comingled', 'Subcontractor', 'UOS']

num_route_name = len(list_of_route_name)
num_sheets = len(wb.sheets)

if num_route_name > num_sheets:
    add_num_sheets = num_route_name - num_sheets
    for n in range(add_num_sheets):
        wb.sheets.add()

for (i, route_name) in enumerate(list_of_route_name):
    wb.sheets[i].name = route_name 

    format_ws(route_name)

# ====================================


# Revenue 
# Fixed Revenue (Est)
# Recycling and Processing - Cardboard
# Rate
# Add Rebate


    #  wb.sheets[i] =
    # print(i, route_name)

# [route_name for route_name in list_of_route_name ]
# number_list = [ x for x in range(20) if x % 2 == 0]
# new_list = [expression for member in iterable]


# Position Class
# Object of Head Title 

# Title size of 13
# Title 
# Weekly Financial Management Report - General Waste Route
# date at :  xx/yy/2021 - Wed 

# format as dollar figure

# Also the Total 
# Tab has all different routes
# Different color
# Also the dataset of respective categoise

# By Truck Number 
# By Bin Vol




