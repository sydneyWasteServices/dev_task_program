import pandas as pd
import numpy as np

ROOT = "C:\\Users\\Gordon.Tang\\OneDrive - JLL\\reconcilation\\Progen_Corrigo_rec\\"
INPUT_PATH = f"{ROOT}4.May.2022_Progen_vs_corrigo_v1.xlsx"
OUTPUT_PATH = f"{ROOT}4.May.2022_Progen_vs_corrigo_v1.csv"

def bitify(data):
        if data == 1:
            return True
        else:
            return False

def clean_df(PATH):

    df = pd.read_excel(PATH)

    # Clean Numbers
    # ==============================================================
    # ==============================================================
    df["PROGEN_CORRIGO_NUMBER"] = df["PROGEN_CORRIGO_NUMBER"].fillna(0)
    df["CORRIGO_NUMBER"] = df["CORRIGO_NUMBER"].fillna(0)
    df["PROGEN_OVCP_ID"] = df["PROGEN_OVCP_ID"].fillna(0)
    df["Correct_Corrigo_For_Progen"] = df["Correct_Corrigo_For_Progen"].fillna(0)

    df["PROGEN_CORRIGO_NUMBER"] = df["PROGEN_CORRIGO_NUMBER"].astype(int)
    df["CORRIGO_NUMBER"] = df["CORRIGO_NUMBER"].astype(int)
    df["PROGEN_OVCP_ID"] = df["PROGEN_OVCP_ID"].astype(np.int64)
    df["Correct_Corrigo_For_Progen"] = df["Correct_Corrigo_For_Progen"].astype(int)

    df = df.astype(object).where(pd.notnull(df), None)

    df["PROGEN_CORRIGO_NUMBER"] = pd.to_numeric(df["PROGEN_CORRIGO_NUMBER"], errors='coerce')
    df["CORRIGO_NUMBER"] = pd.to_numeric(df["CORRIGO_NUMBER"], errors='coerce')
    df["PROGEN_OVCP_ID"] = pd.to_numeric(df["PROGEN_OVCP_ID"], errors='coerce')
    df["Correct_Corrigo_For_Progen"] = pd.to_numeric(df["Correct_Corrigo_For_Progen"], errors='coerce')
    # ==============================================================
    # ==============================================================

    # Bitify  turn True / False 
    # ==============================================================
    df["V_STATE"] = df["V_STATE"].apply(bitify)
    df["V_CITY"] = df["V_CITY"].apply(bitify)
    df["V_STREET"] = df["V_STREET"].apply(bitify)
    
    df = df.astype(object).where(pd.notnull(df), None)
    return df


if __name__ == "__main__":
    
    df = clean_df(INPUT_PATH)
    
    df.to_csv(OUTPUT_PATH, index=True, index_label="ID")
    
    
    