import pandas as pd
import xlwings as xw
import time


wb = xw.Book()
ws1 = wb.sheets[0]

ws1.range((2,1)).value = [1,2,3]

time.sleep(10)
wb.close()


