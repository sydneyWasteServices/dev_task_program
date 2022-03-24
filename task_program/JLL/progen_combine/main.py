import pandas as pd
import numpy as np
import glob
from datetime import date

# Company_Entity
def clean_df(PATH):
    df = pd.read_excel(PATH)
    df['Bank Guarantee Amount'] = df['Bank Guarantee Amount'].fillna(0)
    df['Corrigo Customer Number'] = df['Corrigo Customer Number'].fillna(0)
    df['OVCP_ID - JLL Interface'] = df['OVCP_ID - JLL Interface'].fillna(0)
    df['Version'] = df['Version'].fillna(0)
    df['Suite Group'] = df['Suite Group'].fillna(0)
    df['Option'] = df['Option'].fillna("no")
    df['Bond Amount'] = df['Bond Amount'].fillna(0)


    df['Start Date'] = df['Start Date'].fillna("01/01/1900")
    df['Stop Date'] = df['Stop Date'].fillna("01/01/1900")
    
    df['Occupancy'] = df['Occupancy'].fillna("01/01/1900")
    df['Vacated Date'] = df['Vacated Date'].fillna("01/01/1900")
    df['Bond Received'] = df['Bond Received'].fillna("01/01/1900")
    

    df['Occupancy'] = pd.to_datetime(df['Occupancy'], format="%d/%m/%Y")
    df['Vacated Date'] = pd.to_datetime(df['Vacated Date'], format="%d/%m/%Y")
    df['Bond Received'] = pd.to_datetime(df['Bond Received'], format="%d/%m/%Y")

    # Occupancy
    df.Version = pd.to_numeric(df.Version, downcast="integer")
    df['Suite Group'] = pd.to_numeric(df['Suite Group'], downcast="integer")
    df['SAP Company Code'] = pd.to_numeric(df['SAP Company Code'], downcast="integer")
    

    df.astype({
        "Bank Guarantee Amount" : float, 
        "Corrigo Customer Number" : float,
        "OVCP_ID - JLL Interface" : int,
        "Version" : int,
        "Suite Group" : int
        })

    
    return df

def clean_dash(df):
    if "Imaging" in df["Owner Group Name"]:
        result = df["Owner Group Name"].replace("–","")
        return result
    else:
        return df["Owner Group Name"]

    
if __name__ == "__main__":

    todayDate = date.today().strftime("%d-%m-%Y")

    IPATH = "C:\\Users\\Gordon.Tang\\Desktop\\dataManagement\\ds\\progens_healius\\*.xlsx"
    OPATH_X = f"C:\\Users\\Gordon.Tang\\OneDrive - JLL\\Progen_Site_List\\progen{todayDate}.xlsx"
    OPATH_CSV = f"C:\\Users\\Gordon.Tang\\OneDrive - JLL\\Progen_Site_List\\csv\\progen{todayDate}.csv"

    df = pd.concat(map(clean_df, glob.glob(IPATH))).sort_values(by="Lease")
    
    df["Owner Group Name"] = df.apply(clean_dash,axis=1)
    df['Lease Group Name'] = df.apply(clean_dash,axis=1)
    
    df.to_excel(OPATH_X, index_label="ID")
    df.to_csv(OPATH_CSV, index_label="ID")



