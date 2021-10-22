import xlwings as xw
from xlwings import Range, Sheet, constants

import time

# wb = Workbook.active()
# >>> import xlwings as xw
# >>> wb = xw.books.active
# >>> my_sum = wb.macro('MySum')
# >>> my_sum(1, 2)
# 3


# =================================
# import xlwings as xw
# app = xw.apps.active
# wb = app.books.active
# key1 = 'BUS'
# if key1 in wb:
#     sht = wb.sheets.activate(key1)
# else:
#     sht = wb.sheets.add(key1)
# =====================================

# python 3.7.3
# xlwings 0.15.8

# import xlwings as xw

# app = xw.apps.active
# wb = app.books.active

# key1 = 'BUS'

# if key1 in [sh.name for sh in wb.sheets]:
#     sht = wb.sheets[key1]
# else:
#     sht = wb.sheets.add(key1)
# ========================================

# import xlwings as xw
# wb = xw.Book('myfile.xls')``
# active_sheet_name = wb.sheets.active.name

# ===============================

wb = xw.Book()  
ws1 = wb.sheets[0]

lst = [1, 2 ,3]
new_lst = [[i] for i in lst]


ws1.range("A1").value = new_lst
# offset(row_offset=0, column_offset=0)
active_sheet_name = wb.sheets.active.name
print(active_sheet_name)

len(lst)

ws1.range((len(lst),1)).offset(column_offset=5).value = "have 5"
# Range('A'+str(i)).offset((0,10)).value = 10


time.sleep(3)
wb.close()