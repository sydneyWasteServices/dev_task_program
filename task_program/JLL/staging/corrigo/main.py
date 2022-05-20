from cleaning import Cleaning
from sql_op import Sql_op
import pyodbc
import pandas as pd
import numpy as np
from datetime import date 
import re


ROOT = "C:\\Users\\Gordon.Tang\\OneDrive - JLL\\corrigo\\"
# CSV
FILE = "corrigo.xlsx"
IPATH = f"{ROOT}{FILE}"
clean_fn = Cleaning()
sql_op = Sql_op()
tableName = 'Corrigo'


# Clean Dataframe
# ==================================================================
def clean_df(PATH):
    # CSV , encoding = "ISO-8859-1"
    df = pd.read_excel(IPATH)
    # Address 1 fill na
    # ==================================================================
    df["Address 1"] = df["Address 1"].fillna("No address")

    # Split Company code and Cost Centre from Healius Cost Centre 
    # ==================================================================
    df["Healius Cost Centre"] = df["Healius Cost Centre"].str.strip()
    df[['company_code','cost_centre']] = df["Healius Cost Centre"].str.split("-", 1, expand=True) 

    # Make sure Customer Number as all number
    # ==================================================================
    df["Customer Number"] = pd.to_numeric(df["Customer Number"], errors='coerce')
    df = df[pd.to_numeric(df["Customer Number"], errors='coerce').notnull()]
    
    # Rename Address to Reference address
    # ==================================================================
    df = df.rename(columns={'Address' : 'ref_address'})

    # Remove Healius Cost Centre
    # ==================================================================
    df = df.drop("Healius Cost Centre", axis=1)
    
    # cleaning type
    # ==================================================================
    df["Customer Name"] = df["Customer Name"].str.lower()
    df["Customer Number"] = df["Customer Number"].astype(int)
    df["Postal Code"] = df["Postal Code"].astype(int)

    df["BU Number"] = df["BU Number"].str.strip()
    df["BU Number"] = df["BU Number"].fillna(0)
    df["BU Number"] = pd.to_numeric(df["BU Number"])
    df["BU Number"] = df["BU Number"].astype(np.int64)

    # ==================================================================
    # Closure Date
    
    # Convert Nan to Null
    # ==================================================================
    
    df['Closure Date'] = pd.to_datetime(df['Closure Date'], format='%d/%m/%Y', errors='coerce')

    df["corrigo_status"] = df.apply(clean_fn.corrigo_status, axis=1)
    df["site_comment"] = df.apply(clean_fn.site_comment, axis=1)
    df['Historical Status?'] = df.apply(clean_fn.bitify, axis=1)
    df['Historical Status?'] = df['Historical Status?'].astype(bool)
    
    df = df.astype(object).where(pd.notnull(df), None)
    return df

# Main
# ==================================================================
# ==================================================================
if __name__ == "__main__":

    df = clean_df(IPATH)

    server = "192.168.86.25,8888"
    database = "JLL"
    username = "SA"
    password = "test_password"

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    sql_op.truncateTable(cursor, tableName)
    cnxn.commit()

    selectColsName = f"EXECUTE dbo.selectColsName N'{tableName}'"
    Istatement = sql_op.get_insert_statement(cursor, selectColsName, tableName)

    sql_op.insert_data(cursor, Istatement, df)

    cnxn.commit()
    cursor.close()
    cnxn.close()


    
    