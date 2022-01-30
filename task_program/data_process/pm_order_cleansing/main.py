import pandas as pd
from pm_cleansing import PM_data_cleansing

if __name__ == "__main__":
    # retain ID and description
    PATH = "C:\\gordon_localworkspace\\PM_HLS_categorise\\HLS_categories_item.xlsx"

    pmdc = PM_data_cleansing()

    df = pd.read_excel(PATH)
    df_1 = pd.read_excel(PATH)
    df_1 = df_1[["ID", "Description"]]

    # To Breakdown bracket items () 
    # Set index -> columns & rows want to retain

    df = (
        df[['ID', 'cf_PM Dashboard Schedule', 'Description']]
        .set_index(['ID', 'cf_PM Dashboard Schedule'])
        .apply(pmdc.extra_bracket_items, axis=1)
        .explode()
        .reset_index()
        .rename(columns = {0 :"items"})
    )

    df_m = pd.merge(df, df_1, how="left", on="ID")
    
    df_m = df_m[["ID","cf_PM Dashboard Schedule" ,"Description", "items"]]
    
    OPATH = "C:\\gordon_localworkspace\\PM_HLS_categorise\\PM_order_2.xlsx"
    df_m.to_excel(OPATH, index=False)

    

