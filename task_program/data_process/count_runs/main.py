import pandas as pd
import numpy as np


if __name__ == "__main__":

    WEEK ="42th_2021"
    PATH = f"D:\\Run Analysis\\blob_storage\\roster\\{WEEK}.xlsx"
    COMPLETEPATH = f"D:\\Run Analysis\\blob_storage\\roster\\run_counts\\{WEEK}.csv"

    df = pd.read_excel(PATH)

    df_1 = df.Primary_route.value_counts().reset_index().rename(columns={"index": "route", "Primary_route" : "counts"})

    df_2 = df.Satellite_Route_1.value_counts().reset_index().rename(columns={"index": "route", "Satellite_Route_1" : "counts"})

    df_3 = (df
    .apply(lambda x: x['Satellite_Route_2']
    .split('/') if type(x['Satellite_Route_2']) == str else 0,axis=1)
    .explode()
    .value_counts()
    .reset_index()
    .rename(columns={"index" : "route", 0 : "counts"}) 
    )


    df_t = pd.concat([df_1,df_2,df_3])


    df_t.groupby('route')["counts"].sum().reset_index().to_csv(COMPLETEPATH,index=False)