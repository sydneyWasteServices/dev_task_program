import pandas as pd
import numpy as np
from datetime import date 

RPATH = "C:\\Users\\Gordon.Tang\\Desktop\\dataManagement\\ds\\corrigo\\"


CWO_PATH = f"{RPATH}CorrigoPlatform-Corrigo_CompletedWO.xlsx"
CLIST_PATH = f"{RPATH}CorrigoPlatform-CustomerList.xlsx"
SHAREDR_PATH = f"{RPATH}ShareDrive-Corrigo-CustomerLvl.xlsx"

df_cwo = pd.read_excel(CWO_PATH)
df_clist = pd.read_excel(CLIST_PATH)
df_shdr = pd.read_excel(SHAREDR_PATH)

# Clean 
df_cwo["Due Date"] = df_cwo["Due Date"].fillna("1900-01-01 00:00:00")
df_cwo["Date/Time Created"] = df_cwo["Date/Time Created"].fillna("1900-01-01 00:00:00")
df_cwo["Date/Time Completed - Last"] = df_cwo["Date/Time Completed - Last"].fillna("1900-01-01 00:00:00")



df_cwo.to_csv(OCWO_PATH)
df_clist.to_csv(OCLIST_PATH)
df_shdr.to_csv(OSHAREDR_PATH)