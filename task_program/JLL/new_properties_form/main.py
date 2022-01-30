import pandas as pd
import numpy as np
from datetime import date

if __name__ == "__main__":

    IPATH = "C:\\Users\\Gordon.Tang\\Desktop\\IFM\\propertyOnOffData\\on\\master_create_properties.xlsx"
    todayDate = date.today()
    OPATH = f"C:\\Users\\Gordon.Tang\\Desktop\\IFM\\propertyOnOffData\\on\\New_Properties_to_be_setup_in_JDE_and_Corrigo_{todayDate}.xlsx"
    finance_df = pd.read_excel(IPATH, sheet_name=0).iloc[:,24:]
    corrigo_df = pd.read_excel(IPATH, sheet_name=1).iloc[:,1:]

    writer = pd.ExcelWriter(OPATH, engine='xlsxwriter')

    new_finance_header = finance_df.iloc[0]
    finance_df_ds = finance_df[1:]
    finance_df_ds.columns = new_finance_header
    
    finance_df_ds.to_excel(writer, index=False, sheet_name="JDE-Finance")
    corrigo_df.to_excel(writer, index=False, sheet_name="Corrigo")

    writer.save()

# new dashboard



