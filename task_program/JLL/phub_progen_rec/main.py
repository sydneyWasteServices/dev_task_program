import pandas as pd 
import numpy as np
from datetime import date



if __name__ == "__main__":

    PROGEN_FILENAME = "" 

    IPATH = ""

    dateStr = ""

    OPATH = f"C:\\Users\\Gordon.Tang\\OneDrive - JLL\\Progen_Site_List\\send2Lyndy\\Progen_list_to_update_{dateStr}.xlsx"

    

    ['Lease', 'Name', 'Owner', 'Building', 
    'Building Group Name', 'Type', 'Status', 
    'Lease a/c Name', 'Start Date', 'Stop Date',
    'Rent - Annual', 'SAP Company Code', 
    'Gross / Net', 'Site Type', 
    'Cost Centre', 'Corrigo Customer Number'
    'Corrigo Status', 'OVCP_ID - JLL Interface'
    'Comments', 'Archived'
    ]


    df.to_excel(OPATH, index=False)


