import pandas as pd
import numpy as np
from pathlib import Path
import re

waste_sd = {
    "General Waste": {
        "0.12": 12.6,
        "0.24": 25.2,
        "0.66": 69.3,
        "1.1": 115.5,
        "1.5": 157.5,
        "3": 315.0,
        "4.5": 472.5
    },
    "Dry Waste": {
        "0.12": 8.4,
        "0.24": 16.8,
        "0.66": 46.2,
        "1.1": 77,
        "1.5": 105,
        "3": 210,
        "4.5": 315
    },
    "Comingle": {
        "0.12": 7.2,
        "0.24": 14.4,
        "0.66": 39.6,
        "1.1": 66.0,
    },
    "Paper/Cardboard": {
        "0.12": 6,
        "0.24": 12,
        "0.66": 33,
        "1.1": 55,
        "1.5": 75,
        "3": 150,
        "4.5": 225,
        "0.05": 0
    },
    "Paper": {
        "0.12": 10.8,
        "0.24": 21.6,
        "0.66": 59.4
    },
    "Glass": {
        "0.12": 24,
        "0.24": 48,
        "0.66": 132
    },
    "Organics": {
        "0.12": 33.6,
        "0.24": 67.2
    }
}


PATH = "D:\\Run Analysis\\BLOB_STORAGE\\Nabour_report_ds\\Sep_2021.csv"

df = pd.read_csv(PATH, dtype={
    "Customer_Number": np.float64,
    "Schd Time Start": str,
    "PO": str,
    "Bin_Volume": np.float64,
    "PostCode": str})
# ==============================
# Set Up filter for the df

# ==============================
df['Customer_Number'] = df['Customer_Number'].round(3)

all_naber_report = df.groupby('Customer_Number')

customers_numbers = list(all_naber_report.indices.keys())


for customer_number in customers_numbers:

    address = ''
    naber_df = all_naber_report.get_group(customer_number).reset_index()
    naber_df['Address_1'] = naber_df.Address_1.str.replace(
        '[^a-zA-Z0-9]+', '_', regex=True)

    nuni_address = naber_df.Address_1.nunique()

    if nuni_address != 1:
        print(customer_number)
    else:
        address = naber_df.Address_1.unique()[0]

    def cal_weight(status, waste_type, qty_serviced, bin_volume, weight):

        if weight == 0:
            if status == 'C':
                if waste_type == 'Food Waste':
                    return qty_serviced * waste_sd['Organics'][str(bin_volume)]

                elif waste_type == 'Cardboard' or waste_type == 'Paper/Cardboard':
                    if str(bin_volume) == '3.0':
                        return qty_serviced*waste_sd['Paper/Cardboard']['3']
                    else:
                        return qty_serviced*waste_sd['Paper/Cardboard'][str(bin_volume)]
                elif waste_type == 'Secure Bin':
                    return qty_serviced*waste_sd['Paper'][str(bin_volume)]
                elif waste_type == 'Glass Bin':
                    return qty_serviced*waste_sd['Glass'][str(bin_volume)]
                elif waste_type == 'Loose':
                    return np.nan

                return qty_serviced*waste_sd[waste_type][str(bin_volume)]
            else:
                return np.nan
        else:
            return weight

    naber_df['Total weight picked up - kg (if available)'] = (naber_df.apply(
        lambda df: cal_weight(
            df['Status'],
            df['Waste_Type'],
            df['Qty_Serviced'],
            df['Bin_Volume'],
            df['Weight']
        ),
        axis=1
    ))

    def facility(waste_type):
        facility = {
            'General Waste': 'Veolia Waste Centre Clyde',
            'Dry Waste': 'Veolia Waste Centre Clyde',
            'Food Waste': 'Eathpower Technologies',
            'Organics': 'Eathpower Technologies',
            'Paper/Cardboard': 'Grima Recycling',
            'Cardboard': 'Grima Recycling',
            'Comingle': 'Visy Recycling',
            'Secure Bin': 'Grima Recycling',
            'Glass Bin': 'Grima Recycling',
            'Glass': 'Grima Recycling'
        }
        return facility[waste_type]

    naber_df["Processing Facility sent to (Optional)"] = naber_df['Waste_Type'].transform(
        facility)

    naber_df["Equipment"] = "Mobile bin"

    naber_df["Bin Rejected due to contamination (Optional)"] = np.nan

    naber_df['Dock (can omit if only 1)'] = np.nan

    naber_df['Version:3'] = np.nan

    naber_df['Site Address (StreetNumber Street Name, Suburb, State, Postcode)'] = naber_df[[
        'Address_1', 'City', 'State', 'PostCode']].agg(','.join, axis=1)


    # naber_df['Date'] = pd.to_datetime(naber_df['Date'], format='%Y-%m-%d')

    naber_df['Date'] = pd.to_datetime(naber_df['Date'], format='%d/%m/%Y')


    naber_df = naber_df.sort_values(by="Date", ascending=True)


    naber_df["Processing Facility sent to (Optional)"] = naber_df['Waste_Type'].transform(
        facility)

    def standardize_waste_type(waste_type):
        if waste_type == 'Food Waste':
            return 'Organics'
        elif waste_type == 'Cardboard' or waste_type == 'Paper/Cardboard':
            return 'Paper & Cardboard'
        elif waste_type == 'Comingle':
            return 'Mixed recycling'
        elif waste_type == 'Glass' or waste_type == 'Glass Bin':
            return 'Mixed recycling'
        return waste_type

    naber_df['Waste Type'] = (naber_df.apply(
        lambda df: standardize_waste_type(df['Waste_Type']), axis=1))

    naber_df["Equipment"] = "Mobile bin"
    naber_df["Bin Rejected due to contamination (Optional)"] = np.nan

    naber_df['Dock (can omit if only 1)'] = np.nan
    naber_df['Version:3'] = np.nan

    # City	State	PostCode

    naber_df['Site Address (StreetNumber Street Name, Suburb, State, Postcode)'] = naber_df[[
        'Address_1', 'City', 'State', 'PostCode']].agg(','.join, axis=1)

    naber_df['Date'] = pd.to_datetime(naber_df['Date'], format='%Y-%m-%d')

    naber_df = naber_df.sort_values(by="Date", ascending=True)

    naber_df['Pick-up Date (dd/mm/yyyy)'] = naber_df['Date'].dt.strftime('%d/%m/%Y')

    def is_fut_bin(status, served_bins):
        if status == 'F' or status == 'V':
            return 0
        return served_bins

    naber_df['Units Collected'] = naber_df.apply(
        lambda df: is_fut_bin(df['Status'], df['Qty_Serviced']), axis=1)

    
    naber_df = naber_df.rename(columns={'Bin_Volume': 'Size (m3)'})
                

    fileExt = ".xlsx"
    
    naber_df.to_excel(Path(str(address)+"_"+str(customer_number)+fileExt), sheet_name=str(customer_number), columns=[
        'Pick-up Date (dd/mm/yyyy)',
        'Site Address (StreetNumber Street Name, Suburb, State, Postcode)',
        'Dock (can omit if only 1)',
        'Waste Type',
        'Equipment',
        'Size (m3)',
        'Units Collected',
        'Total weight picked up - kg (if available)',
        'Processing Facility sent to (Optional)',
        'Bin Rejected due to contamination (Optional)',
        'Version:3'
    ], index=False)
