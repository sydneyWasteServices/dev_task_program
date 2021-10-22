import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
xw.view(df)


import xlwings as xw
import pandas as pd

def GetDataFrame(wb_file,Sheets_i,N,M):
    wb = xw.books(wb_file)   #open your workbook
         #Specify the value of the cell of the worksheet
    Data=wb.sheets[Sheets_i].range((1,1),(N,M)).value  
    Data=pd.DataFrame(Data)
    Data=Data.dropna(how='all',axis=1)
    Data=Data.dropna(how='all',axis=0)
    return Data



# how to delete sheet
# how to name sheet
