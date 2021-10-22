import xlwings as xw
import pandas as pd 
import numpy as np 
# ==================================================================================
# data source 


PATH = "D:\\Run Analysis\\waste_reports\\Jul2021.csv"

PATH_AUG = "D:\\Run Analysis\\waste_reports\\Aug2021.csv"

SAMPLEPATH = "D:\\Run Analysis\\waste_reports\\sample\\sample.xlsx"

df = pd.read_csv(PATH)

# df_aug = pd.read_csv(PATH_JUL)

# ==================================================================================


# ==================================================================================
# Data 

for i in range(0, df.shape[0]):
    try:    
        date = '\'Jul 2021'

        customer_nmuber = df.iloc[i,0]

        address = df.iloc[i,1]

        waste = df.iloc[i,2]

        cardboard = df.iloc[i,3]

        comingle = df.iloc[i,4]

        organics = df.iloc[i,5]

    # ======================
        # Excel posiiton

        adddress_x = 'c1'

        row = 3

        date_x = f'a{row}'

        cardboard_x = f'c{row}'

        comingle_x = f'd{row}'

        waste_x = f'e{row}'

        organics_x = f'f{row}'

        # wb = xw.books.open(SAMPLEPATH)
        
        wb = xw.Book(SAMPLEPATH)

        ws = wb.sheets['Data - CM']

        ws.range(date_x).value = date

        ws.range(adddress_x).value = address

        ws.range(cardboard_x).value = cardboard

        ws.range(comingle_x).value = comingle

        ws.range(waste_x).value = waste

        ws.range(organics_x).value = organics

        wb.save(f'D:\\Run Analysis\\waste_reports\\current_waste_reports\\{customer_nmuber}_{address}')

        wb.close()
        
        
    except  Exception as e:
        print(e)
        print(f'{customer_nmuber} {address}')
        
        
    # ==================================================================================
