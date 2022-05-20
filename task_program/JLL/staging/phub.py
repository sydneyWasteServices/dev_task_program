import pandas as pd
import numpy as np
import pyodbc
import os
import textwrap as tw

SELECTCOL = "C:\\Users\\Gordon.Tang\\OneDrive - JLL\\property_hub\\csv\\phub_og_colums.csv"
IPATH = "C:\\Users\\Gordon.Tang\\OneDrive - JLL\\property_hub\\phub.xlsx"

tableName = 'Property_hub'

def clean_df(
    PATH4COL : str, 
    IPATH : str):

    select_cols = pd.read_csv(PATH4COL, encoding='cp1252').columns

    df = pd.read_excel(IPATH)
    df = df[select_cols]
    df.iloc[:,30] = pd.to_datetime(df.iloc[:,30], format="%m/%d/%Y")
    df = df.astype(object).where(pd.notnull(df), None)
    return df


def truncateTable(
    curs : object,
    TB_name : str
):
    sqlStatement = f"TRUNCATE TABLE [JLL].[dbo].[{TB_name}]"
    curs.execute(sqlStatement)

def get_insert_statement(
    curs : object,
    sqlStatement : str,
    TB_name : str):

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

    statement = f"INSERT INTO [JLL].[dbo].[{TB_name}] ({cols_name_str}) VALUES ({q_marks_str})"
    
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
        row[33])
        

if __name__ == "__main__":

    server = "192.168.86.25,8888"
    database = "JLL"
    username = "SA"
    password = "test_password"
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    truncateTable(cursor, tableName)
    cnxn.commit()
    
    selectColsName = f"EXECUTE dbo.selectColsName N'{tableName}'"
    Istatement = get_insert_statement(cursor, selectColsName, tableName)

    df = clean_df(SELECTCOL, IPATH)
    
    insert_data(cursor, Istatement, df)

    cnxn.commit()
    cursor.close()
    cnxn.close()