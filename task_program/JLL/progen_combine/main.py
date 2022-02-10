import pandas as pd
import numpy as np
import glob


def clean_df(PATH):
    df = pd.read_excel(PATH, dtype={
        "Bank Guarantee Amount" : np.float64,
        "Corrigo Customer Number" : np.float64,
        "OVCP ID JLL Interface" : np.float64,
        "Version" : int})
    return df

def clean_dash(df):
    if "Imaging" in df["Owner Group Name"]:
        result = df["Owner Group Name"].replace("–","")
        return result
    else:
        return df["Owner Group Name"]

    
if __name__ == "__main__":

    IPATH = "C:\\Users\\Gordon.Tang\\Desktop\\dataManagement\\ds\\progens_healius\\*.xlsx"
    OPATH = "C:\\Users\\Gordon.Tang\\Desktop\\dataManagement\\csv_ds\\progen.csv"

    df = pd.concat(map(clean_df, glob.glob(IPATH))).sort_values(by="Lease")
    
    df["Owner Group Name"] = df.apply(clean_dash,axis=1)
    # print(df["Owner Group Name"].unique())
    df.to_csv(OPATH)



