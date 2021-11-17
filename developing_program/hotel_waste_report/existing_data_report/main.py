import pandas as pd
import numpy as np
import xlwings as xw



def clean_df(df : object):
    df['Address_1'] = df.Address_1.str.replace(r'\/','-',regex=True)
    return df

if __name__ == '__main__':

    EXISTING_REPORT = 'D:\\Run Analysis\\blob_storage\\waste_report_ds\\Sept2021.csv'

    DATA_PATH = "D:\\Run Analysis\\Hotel_waste_reports\\data\\Oct.csv"

    df = pd.read_csv(DATA_PATH)

    df = clean_df(df)
    
    
# ========================================================================
# Open workbook
    wb = xw.Book(EXISTING_REPORT)

    cpws = wb.sheets['MonthlySummary']

# ========================================================================
    

# ton_data = (
#     df
#     .sort_values(by='Customer_Number')
#     .groupby(['Customer_Number', 'Address_1', 'Waste_type'])['Total_volume']
#     .sum()
# )

# price_data = (
#     df
#     .sort_values(by='Customer_Number')
#     .groupby(['Customer_Number', 'Address_1', 'Waste_type'])['Total_price']
#     .sum()
# )

# customers_number = ton_data.index.get_level_values(0).unique()



# def fill_excel_by_cus(price_data: object, ton_data: object, customer_number: float, idx : int):

#     print(customer_number)

#     ws_summary = wb.sheets["Spend by site summary"]
    
#     address = ton_data.xs(customer_number).index.get_level_values(0).unique()
    
#     sheetname = f"{address[0]}_{customer_number}"

#     lastSheet = wb.sheets[-1]

#     waste_types = ton_data.xs(customer_number).index.get_level_values(1).unique()

#     customer_price_data = price_data.xs(customer_number)   

#     customer_ton_data = ton_data.xs(customer_number)

#     cpws.copy(after=lastSheet, name=sheetname)

#     ws = wb.sheets[sheetname]

#     cardboard_price = 0
#     comingle_price = 0
#     general_waste_price = 0
#     security_paper_price = 0
#     organics_price = 0


#     cardboard_ton = 0
#     comingle_ton = 0
#     general_waste_ton = 0
#     security_paper_ton = 0
#     organics_ton = 0
    
#     general_waste_og_ton = 0 

#     # Row Number , Column Number
#     # range((row, col))
    
#     for waste_type in waste_types:

#         if waste_type == 'Cardboard':
#             ws.range('c3').value = customer_price_data[address[0]][waste_type] /11*10
#             ws.range('c16').value = customer_ton_data[address[0]][waste_type] / 9.224

#             cardboard_price = customer_price_data[address[0]][waste_type] /11*10
#             cardboard_ton = customer_ton_data[address[0]][waste_type] / 9.224

#         elif waste_type == "Comingle":

#             ws.range('c4').value = customer_price_data[address[0]][waste_type] /11*10
#             ws.range('c17').value = customer_ton_data[address[0]][waste_type] / 7.645

#             comingle_price = customer_price_data[address[0]][waste_type] /11*10
#             comingle_ton = customer_ton_data[address[0]][waste_type] / 7.645

#         elif waste_type == "General Waste":

#             ws.range('c5').value = customer_price_data[address[0]][waste_type] /11*10
#             ws.range('c18').value = customer_ton_data[address[0]][waste_type] / 3.394

#             general_waste_price = customer_price_data[address[0]][waste_type] /11*10
#             general_waste_og_ton = customer_ton_data[address[0]][waste_type] / 3.394
#             general_waste_ton = customer_ton_data[address[0]][waste_type] / 3.394 * .75

#         elif waste_type == "Security Paper":

#             ws.range('c6').value = customer_price_data[address[0]][waste_type] /11*10
#             ws.range('c19').value = customer_ton_data[address[0]][waste_type] / 9.224

#             security_paper_price = customer_price_data[address[0]][waste_type] /11*10
#             security_paper_ton = customer_ton_data[address[0]][waste_type] / 9.224

#         elif waste_type == "Organics":
            
#             ws.range('c11').value = customer_price_data[address[0]][waste_type] /11*10
#             ws.range('c24').value = customer_ton_data[address[0]][waste_type] / 3.394
#             organics_price = customer_price_data[address[0]][waste_type] /11*10
#             organics_ton = customer_ton_data[address[0]][waste_type] / 3.394
# # =============================================================================================
#     # Aggregate data and fill to summary sheet 

#     ws_summary_rowIdx = 3 + idx

#     avg_price = (cardboard_price + comingle_price + general_waste_price + security_paper_price + organics_price) / (cardboard_ton + comingle_ton + general_waste_og_ton + security_paper_ton + organics_ton)

#     ws_summary.range((ws_summary_rowIdx, 1)).value = address[0]

#     ws_summary.range((ws_summary_rowIdx, 2)).value = avg_price

#     ws.range('c33').value =  cardboard_ton + comingle_ton + general_waste_ton + security_paper_ton

#     ws.range('c37').value = organics_ton

# # =============================================================================================
# [fill_excel_by_cus(price_data, ton_data, cus_num, idx) for idx, cus_num in enumerate(customers_number)]

# # for idx, val in enumerate(ints):
# #     print(idx, val)

# # =============================================================================================
# # Monthly Summary
# # =========================================================

# summary_df = df.groupby('Waste_type')['Total_price','Total_volume'].sum()

# cpws.range('c3').value = summary_df.iloc[0,0] /11*10
# cpws.range('c16').value = summary_df.iloc[0,1] / 9.224 

# cpws.range('c4').value = summary_df.iloc[1,0] /11*10
# cpws.range('c17').value = summary_df.iloc[1,1] / 7.645 

# cpws.range('c5').value = summary_df.iloc[2,0] /11*10 
# cpws.range('c18').value = summary_df.iloc[2,1] / 3.394 * .75

# cpws.range('c6').value = summary_df.iloc[4,0] /11*10
# cpws.range('c19').value = summary_df.iloc[4,1] / 9.224 

# cpws.range('c11').value = summary_df.iloc[3,0] /11*10
# cpws.range('c24').value = summary_df.iloc[3,1] / 3.394

# cpws.range('c33').value = (summary_df.iloc[0,1] / 9.224 ) + (summary_df.iloc[1,1] / 7.645 ) + (summary_df.iloc[2,1]/ 3.394 * .75)  + summary_df.iloc[3,1]  / 3.394
# cpws.range('c37').value = summary_df.iloc[3,1] / 3.394

             
# # =============================================================================================


# wb.save(f"D:\\Run Analysis\\waste_reports_accor\\Sept2021_hotel.xlsx")

# wb.close()





