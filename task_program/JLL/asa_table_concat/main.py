import pandas as pd
import numpy as np
import glob
import os
from datetime import date

def asa_role_id(path):
    df = pd.read_excel(path)
    filename = os.path.basename(path)
    rolename = filename.split('.', 1)[0]
    df['asa_role'] = rolename
    return df 

if __name__ == "__main__":
    todayDate = date.today()
    IPATH = "C:\\Users\\Gordon.Tang\\Desktop\\ASA\\*.xls"
    OPATH = f"C:\\Users\\Gordon.Tang\\Desktop\\ASA\\asa_summary\\asa_summary_{todayDate}.xlsx"
    df = pd.concat(map(asa_role_id, glob.glob(IPATH)))
    df.dropna().sort_values(by="User Name").to_excel(OPATH, index=False)


