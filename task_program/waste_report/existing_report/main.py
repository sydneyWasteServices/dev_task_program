import xlwings as xw
import pandas as pd
import numpy as np
import os

cusNum_arr = list()
address_arr = list()
filePath_arr = list()

MONTH_FILE = "Aug2021.csv" 

PATH_DIR_EXIST_REPORT = 'D:\\Run Analysis\\waste_reports\\current_waste_reports'

PATH_NEW_DATA = f"D:\Run Analysis\waste_reports\\{MONTH_FILE}"

data_df = pd.read_csv(PATH_NEW_DATA, dtype={'Customer_Number': np.float64})

data_df.Customer_Number = data_df.Customer_Number.round(3)

directory = os.scandir(PATH_DIR_EXIST_REPORT)

for file in directory:
    cusNum_addr = str.split(file.name, "_")
    cusNum_arr.append(cusNum_addr[0]) 
    address_arr.append(cusNum_addr[1])
    filePath_arr.append(file.name)

data = {'customer_number' : cusNum_arr, 'address': address_arr, 'file_path' : filePath_arr}

exist_reports_df = pd.DataFrame(data)

# 
exist_reports_df['customer_number'] = exist_reports_df.customer_number.astype(np.float)
exist_reports_df.customer_number = exist_reports_df.customer_number.round(3)

exist_reports_df['address'] = exist_reports_df.address.astype(str)
exist_reports_df['file_path'] = exist_reports_df.file_path.astype(str)

# From existing reports pick data 
for i in range(0, exist_reports_df.shape[0]):

    customer_number = exist_reports_df.iloc[i,0]
    
    info = data_df[data_df.Customer_Number.eq(customer_number)]
    
    is_empty = info.Customer_Number.empty
    
    num_data = info.Customer_Number.shape[0]
    

    if is_empty == False and num_data == 1:
        
        file_path = exist_reports_df.iloc[i,2]
        
        EXIST_REPORT_PATH = f"D:\\Run Analysis\\waste_reports\\current_waste_reports\\{file_path}"

        wb = xw.Book(EXIST_REPORT_PATH)

        ws = wb.sheets['Data - CM']

        waste = info.iloc[0,2]

        cardboard = info.iloc[0,3]

        comingle = info.iloc[0,4]

        organics = info.iloc[0,5]

    # ============================================

        row = 4

        date = '\'Aug 2021'

        date_x = f'a{row}'

        cardboard_x = f'c{row}'

        comingle_x = f'd{row}'

        waste_x = f'e{row}'

        organics_x = f'f{row}'

    # ============================================

        ws.range(date_x).value = date

        ws.range(cardboard_x).value = cardboard

        ws.range(comingle_x).value = comingle

        ws.range(waste_x).value = waste

        ws.range(organics_x).value = organics

        wb.save(f'D:\\Run Analysis\\waste_reports\\current_waste_reports\\{file_path}')

        wb.close()
        
    else :
        print(customer_number)

