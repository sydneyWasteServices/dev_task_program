import pandas as pd
import numpy as np
import pyodbc
import os
import textwrap as tw
from datetime import date
# step 1  25.2.2022
# Since they are the same table, 
# Select into  and then truncate the whole table
todayDate = date.today().strftime("%d-%m-%Y")

IROOT = "C:\\Users\\Gordon.Tang\\OneDrive - JLL\\Progen\\csv\\"

TB_NAME = f"progen{todayDate}"

IPATH = f"{IROOT}{TB_NAME}.csv"

def clean_df(PATH : str):
    df = pd.read_csv(PATH)

    # When dates are slash / 
    # ===============================================
    # df["Start Date"] = pd.to_datetime(df["Start Date"], format="%d/%m/%Y")
    # df["Stop Date"] = pd.to_datetime(df["Stop Date"], format="%d/%m/%Y")
    # df["Occupancy"] = pd.to_datetime(df["Occupancy"], format="%d/%m/%Y")
    # df["Vacated Date"] = pd.to_datetime(df["Vacated Date"], format="%d/%m/%Y")
    # df["Bond Received"] = pd.to_datetime(df["Bond Received"], format="%d/%m/%Y")
    # df["Bank Guarantee Expiry Date"].fillna("01/01/1900 00:00")
    # df["Bank Guarantee Expiry Date"] = pd.to_datetime(df["Bank Guarantee Expiry Date"], format="%d/%m/%Y %H:%M")
    # ===============================================

    # When dates are dash - 
    # ===============================================
    df["Start Date"] = pd.to_datetime(df["Start Date"], format="%Y-%m-%d")
    df["Stop Date"] = pd.to_datetime(df["Stop Date"], format="%Y-%m-%d")
    df["Occupancy"] = pd.to_datetime(df["Occupancy"], format="%Y-%m-%d")
    df["Vacated Date"] = pd.to_datetime(df["Vacated Date"], format="%Y-%m-%d")
    df["Bond Received"] = pd.to_datetime(df["Bond Received"], format="%Y-%m-%d")
    df["Bank Guarantee Expiry Date"].fillna("01/01/1900 00:00")
    df["Bank Guarantee Expiry Date"] = pd.to_datetime(df["Bank Guarantee Expiry Date"], format="%Y-%m-%d %H:%M")
    # ===============================================
# To convert Null
    df = df.astype(object).where(pd.notnull(df), None)
    return df

def cloneTableNTruncate(
    curs : object, 
    newTB_name : str):

    # USE [JLL]; GO  IF EXISTS (SELECT * FROM sys.tables WHERE SCHEMA_NAME(schema_id) = 'dbo' AND name = 'MyTable0' ) DROP TABLE [dbo].[MyTable0] 

    sqlStatement = f"SELECT * INTO [JLL].[dbo].[{newTB_name}] FROM [JLL].[dbo].[progen17-03-2022]; \
    TRUNCATE TABLE [JLL].[dbo].[{newTB_name}];"
    cursor.execute(sqlStatement)
    


def get_insert_statement(
    curs : object,
    sqlStatement : str,
    newTB_name : str):

    cols_name = []
    q_marks = []

    cursor.execute(sqlStatement)

    for row in cursor.fetchall():
        cols_name.append(row[0])
    
    cols_name = [str(tw.wrap(name)).replace("'", "") for name in cols_name]

    cols_name_str = ",".join(cols_name)

    for value in range(len(cols_name)):
        q_marks.append("?")
    
    q_marks_str = ",".join(q_marks)

    statement = f"INSERT INTO [JLL].[dbo].[{newTB_name}] ({cols_name_str}) VALUES ({q_marks_str})"
    
    return statement

def insert_data(
    curs : object,
    insert_statement : str,
    df : object 
    ):
    
    for index, row in df.iterrows():
        print(index)
        curs.execute(insert_statement, 
        row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
        row[11], row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],
        row[22], row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],
        row[33], row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],
        row[44], row[45],row[46],row[47],row[48],row[49],row[50],row[51],row[52],row[53],row[54],
        row[55], row[56],row[57],row[58],row[59],row[60],row[61],row[62],row[63],row[64],row[65],
        row[66], row[67],row[68],row[69],row[70],row[71],row[72],row[73],row[74],row[75],row[76],
        row[77]
        )


if __name__ == "__main__":

    df = clean_df(IPATH)
    
    # DB connection
    # =================================================
    server = "192.168.86.25,8888"
    database = "JLL"

    username = "SA"
    password = "test_password"

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    # =================================================
    cloneTableNTruncate(cursor, TB_NAME)
    cnxn.commit()
    selectColsName = "EXECUTE dbo.selectColsName N'progen17-03-2022'"

    Istatement = get_insert_statement(cursor, selectColsName, TB_NAME)
    
    insert_data(cursor, Istatement, df)
    
    cnxn.commit()
    cursor.close()
    cnxn.close()


# new table name must be the latest file name


# Step 2 

# Select all column name , place it into pyodbc statement

# create new statement to 


# 10256