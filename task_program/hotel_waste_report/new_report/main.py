import pandas as pd
import numpy as np
import xlwings as xw

def clean_df(df : object):
    df['Address_1'] = df.Address_1.str.replace(r'\/','-',regex=True)
    return df

TEMPLATE_REPORT_PATH = "D:\\Run Analysis\\Hotel_waste_reports\\template\\template_Waste_report.xlsx"

DATA_PATH = 'D:\\Run Analysis\\Hotel_waste_reports\\data\\Sept_NEW.csv'

df = pd.read_csv(DATA_PATH)

df = clean_df(df)

recycle_rate_df = clean_df(df)

ton_data = (
    df
    .sort_values(by='Customer_Number')
    .groupby(['Customer_Number', 'Address_1', 'Waste_type'])['Total_volume']
    .sum()
)

price_data = (
    df
    .sort_values(by='Customer_Number')
    .groupby(['Customer_Number', 'Address_1', 'Waste_type'])['Total_price']
    .sum()
)

customers_number = ton_data.index.get_level_values(0).unique()

# ==================================================================================================================================
# Recycle Rate
# ==================================================================================================================================

def recycle_rate_by_state(x):
        
        if  x.STATE == 'NSW' and x.Waste_type == 'General Waste' :
            
            return x.Total_volume / 3.394 * 0.6 

        elif x.STATE == 'ACT' and x.Waste_type == 'General Waste' :
            
            return x.Total_volume / 3.394 * 0.15 
        
        elif x.STATE == 'VIC' and x.Waste_type == 'General Waste' :
            
            return x.Total_volume / 3.394 * 0.1
            
        elif x.STATE == 'WA' and x.Waste_type == 'General Waste':
            
            return x.Total_volume / 3.394 * 0.12
            
        elif (x.STATE == 'NT' or x.STATE == 'DARWIN') and x.Waste_type == 'General Waste' :
            
            return x.Total_volume / 3.394 * 0.9
            
        elif (x.STATE == 'TAS' or x.STATE == 'HOBART') and x.Waste_type == 'General Waste' :
            
            return x.Total_volume / 3.394 * 0.1
    # =====================================================================================            
        elif  (x.STATE == 'NSW' or x.STATE == 'ACT') and x.Waste_type == 'Comingle' :
            
            return x.Total_volume / 7.645 * 0.85
        
        elif x.STATE == 'VIC' and x.Waste_type == 'Comingle' :
            
            return x.Total_volume / 7.645 * 0.97
            
        elif x.STATE == 'WA' and x.Waste_type == 'Comingle':
            
            return x.Total_volume / 7.645 * 0.85
            
        elif (x.STATE == 'NT' or x.STATE == 'DARWIN') and x.Waste_type == 'Comingle' :
            
            return x.Total_volume / 7.645 * 0.85
            
        elif (x.STATE == 'TAS' or x.STATE == 'HOBART') and x.Waste_type == 'Comingle' :
            
            return x.Total_volume / 7.645 * 0.9
    # =====================================================================================            
        elif  (x.STATE == 'NSW' or x.STATE == 'ACT') and x.Waste_type == 'Cardboard' :
            
            return x.Total_volume / 9.224 * 0.85
        
        elif x.STATE == 'VIC' and x.Waste_type == 'Cardboard' :
            
            return x.Total_volume / 9.224 * 0.98
            
        elif x.STATE == 'WA' and x.Waste_type == 'Cardboard':
            
            return x.Total_volume / 9.224 * 0.98
            
        elif (x.STATE == 'NT' or x.STATE == 'DARWIN') and x.Waste_type == 'Cardboard' :
            
            return x.Total_volume / 9.224 * 0.85
            
        elif (x.STATE == 'TAS' or x.STATE == 'HOBART') and x.Waste_type == 'Cardboard' :
            
            return x.Total_volume / 9.224 * 0.9
    # =====================================================================================            
        elif  (x.STATE == 'NSW' or x.STATE == 'ACT') and x.Waste_type == 'Organics' :
            
            return x.Total_volume / 3.394 * 0.95
        
        elif x.STATE == 'VIC' and x.Waste_type == 'Organics' :
            
            return x.Total_volume / 3.394 * 0.98
            
        elif x.STATE == 'WA' and x.Waste_type == 'Organics':
            
            return x.Total_volume / 3.394 * 0.95
            
        elif (x.STATE == 'NT' or x.STATE == 'DARWIN') and x.Waste_type == 'Organics' :
            
            return x.Total_volume * 0
            
        elif (x.STATE == 'TAS' or x.STATE == 'HOBART') and x.Waste_type == 'Organics' :
            
            return x.Total_volume / 3.394 * 0.95

# ==================================================================================================================================
# exclude GST income
# ==================================================================================================================================

def excl_gst_price(x):
    return x.Total_price / 11 * 10

# ==================================================================================================================================
# Convert to ton
# ==================================================================================================================================

def convert2_ton(x):
    if x.Waste_type == 'Cardboard':
        return x.Total_volume / 9.224
    elif x.Waste_type == 'Comingle':
        return x.Total_volume / 7.645
    elif x.Waste_type == "General Waste":
        return x.Total_volume / 3.394
    elif x.Waste_type == "Organics":
        return x.Total_volume / 3.394
    elif x.Waste_type == "Security Paper":
        return x.Total_volume / 9.224

recycle_rate_df['recycle_ton'] = recycle_rate_df.apply(recycle_rate_by_state, axis=1)
recycle_rate_df['excl_gst_price'] = recycle_rate_df.apply(excl_gst_price, axis=1)
recycle_rate_df['ton'] = recycle_rate_df.apply(convert2_ton, axis=1)

# ========================================================================
# Open workbook
wb = xw.Book(TEMPLATE_REPORT_PATH)

cpws = wb.sheets['MonthlySummary']

# ========================================================================

# ===========================================================
# State Dataframes 
# ===========================================================
state_waste_ton_df = recycle_rate_df.groupby(['STATE' ,'Waste_type'])['ton'].sum().reset_index()

state_recycle_df = recycle_rate_df.groupby(['STATE' ,'Waste_type'])['recycle_ton'].sum().reset_index()

state_price_df = recycle_rate_df.groupby(['STATE' ,'Waste_type'])['excl_gst_price'].sum().reset_index()


# ======================================================================================================================
STATES = ['ACT', 'NSW', 'VIC', 'NT', 'TAS']

def by_state_monthly_summary(state : str):

    sheetname = f"{state}_MonthlySummary"

    lastSheet = wb.sheets[-1]
    
    cpws.copy(after=lastSheet, name=sheetname)

    ws = wb.sheets[sheetname]

    ws.range('c3').value = state_price_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Cardboard')].excl_gst_price.values[0]

    ws.range('c16').value = state_waste_ton_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Cardboard')].ton.values[0]


    ws.range('c4').value = state_price_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Comingle')].excl_gst_price.values[0]

    ws.range('c17').value = state_waste_ton_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Comingle')].ton.values[0]


    ws.range('c5').value = state_price_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('General Waste')].excl_gst_price.values[0]

    ws.range('c18').value3 = state_waste_ton_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('General Waste')].ton.values[0]

# =======================================================    
# No Security Paper at the moment

    # ws.range('c6').value =

    # ws.range('c19').value
# =======================================================    
    organic_price  = state_price_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Organics')].excl_gst_price.values

    if organic_price != [] :
    
        ws.range('c11').value = state_price_df[state_price_df.STATE.eq(state) & state_price_df.Waste_type.eq('Organics')].excl_gst_price.values 

    organic_ton = state_waste_ton_df[state_waste_ton_df.STATE.eq(state) & state_waste_ton_df.Waste_type.eq('Organics')].ton.values

    if organic_ton != []:

        ws.range('c24').value = state_waste_ton_df[state_waste_ton_df.STATE.eq(state) & state_waste_ton_df.Waste_type.eq('Organics')].ton.values[0]

    ws.range('c33').value = state_recycle_df[state_recycle_df.STATE.eq(state) & state_recycle_df.Waste_type.ne('Organics')].recycle_ton.sum()

    ws.range('c37').value = state_recycle_df[state_recycle_df.STATE.eq(state) & state_recycle_df.Waste_type.eq('Organics')].recycle_ton.sum()

[by_state_monthly_summary(state) for state in STATES]


def fill_excel_by_cus(price_data: object, ton_data: object, customer_number: float, idx : int):

    print(customer_number)

    ws_summary = wb.sheets["Spend by site summary"]
    
    address = ton_data.xs(customer_number).index.get_level_values(0).unique()
    
    sheetname = f"{address[0]}_{customer_number}"

    lastSheet = wb.sheets[-1]

    waste_types = ton_data.xs(customer_number).index.get_level_values(1).unique()

    customer_price_data = price_data.xs(customer_number)   

    customer_ton_data = ton_data.xs(customer_number)

    cpws.copy(after=lastSheet, name=sheetname)

    ws = wb.sheets[sheetname]

    cardboard_price = 0
    comingle_price = 0
    general_waste_price = 0
    security_paper_price = 0
    organics_price = 0


    cardboard_ton = 0
    comingle_ton = 0
    general_waste_ton = 0
    security_paper_ton = 0
    organics_ton = 0
    
    # Row Number , Column Number
    # range((row, col))
    
    for waste_type in waste_types:

        if waste_type == 'Cardboard':
            ws.range('c3').value = customer_price_data[address[0]][waste_type] /11*10
            ws.range('c16').value = customer_ton_data[address[0]][waste_type] / 9.224

            cardboard_price = customer_price_data[address[0]][waste_type] /11*10
            cardboard_ton = customer_ton_data[address[0]][waste_type] / 9.224

        elif waste_type == "Comingle":

            ws.range('c4').value = customer_price_data[address[0]][waste_type] /11*10
            ws.range('c17').value = customer_ton_data[address[0]][waste_type] / 7.645

            comingle_price = customer_price_data[address[0]][waste_type] /11*10
            comingle_ton = customer_ton_data[address[0]][waste_type] / 7.645

        elif waste_type == "General Waste":

            ws.range('c5').value = customer_price_data[address[0]][waste_type] /11*10
            ws.range('c18').value = customer_ton_data[address[0]][waste_type] / 3.394

            general_waste_price = customer_price_data[address[0]][waste_type] /11*10
            general_waste_ton = customer_ton_data[address[0]][waste_type] / 3.394

        elif waste_type == "Security Paper":

            ws.range('c6').value = customer_price_data[address[0]][waste_type] /11*10
            ws.range('c19').value = customer_ton_data[address[0]][waste_type] / 9.224

            security_paper_price = customer_price_data[address[0]][waste_type] /11*10
            security_paper_ton = customer_ton_data[address[0]][waste_type] / 9.224

        elif waste_type == "Organics":
            
            ws.range('c11').value = customer_price_data[address[0]][waste_type] /11*10
            ws.range('c24').value = customer_ton_data[address[0]][waste_type] / 3.394
            organics_price = customer_price_data[address[0]][waste_type] /11*10
            organics_ton = customer_ton_data[address[0]][waste_type] / 3.394
# =============================================================================================
    # Aggregate data and fill to summary sheet 

    ws_summary_rowIdx = 3 + idx

    avg_price = (cardboard_price + comingle_price + general_waste_price + security_paper_price + organics_price) / (cardboard_ton + comingle_ton + general_waste_ton + security_paper_ton + organics_ton)

    ws_summary.range((ws_summary_rowIdx, 1)).value = address[0]

    ws_summary.range((ws_summary_rowIdx, 2)).value = avg_price
# =============================================================================================
    # Recycle Rate by State per Customer Number
    
    ws.range('c33').value =  recycle_rate_df[recycle_rate_df.Customer_Number.eq(customer_number) & recycle_rate_df.Waste_type.ne('Organics')].recycle_ton.sum()

    ws.range('c37').value = recycle_rate_df[recycle_rate_df.Customer_Number.eq(customer_number) & recycle_rate_df.Waste_type.eq('Organics')].recycle_ton.sum()

# =============================================================================================
[fill_excel_by_cus(price_data, ton_data, cus_num, idx) for idx, cus_num in enumerate(customers_number)]

# ====================================================================================================================================================================================================
# Monthly Summary 
# ====================================================================================================================================================================================================

summary_df = df.groupby('Waste_type')['Total_price','Total_volume'].sum()

cpws.range('c3').value = summary_df.iloc[0,0] /11*10
cpws.range('c16').value = summary_df.iloc[0,1] / 9.224 

cpws.range('c4').value = summary_df.iloc[1,0] /11*10
cpws.range('c17').value = summary_df.iloc[1,1] / 7.645 

cpws.range('c5').value = summary_df.iloc[2,0] /11*10 
cpws.range('c18').value = summary_df.iloc[2,1] / 3.394 * .75

# cpws.range('c6').value = summary_df.iloc[4,0] /11*10
# cpws.range('c19').value = summary_df.iloc[4,1] / 9.224 

cpws.range('c11').value = summary_df.iloc[3,0] /11*10
cpws.range('c24').value = summary_df.iloc[3,1] / 3.394


cpws.range('c33').value = (summary_df.iloc[0,1] / 9.224 ) + (summary_df.iloc[1,1] / 7.645 ) + (summary_df.iloc[2,1]/ 3.394 * .75)  + summary_df.iloc[3,1]  / 3.394  
cpws.range('c37').value = summary_df.iloc[3,1] / 3.394


             
# =============================================================================================

wb.save(f"D:\\Run Analysis\\Hotel_waste_reports\\Sept2021_hotel.xlsx")

wb.close()
