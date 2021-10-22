import pandas as pd
import numpy as np


PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\tanda\\20th_2021.xlsx'
# PATH_EMPID
COMPLETE_PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\tanda\\processed\\20th_2021_processed.csv'



dfs = pd.read_excel(PATH, sheet_name=None,header=0, engine='openpyxl')

all_sheetnames = list(dfs.keys())[1:]



def tanda_pc_manual(input_dfs : object, sheetname : int):
    
    df = input_dfs[sheetname]

    current_df_date = df.columns[0].replace(" ","/").lower()

    # rename columns to second row
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    

    # Change years if current year change
    # day, months and year to new column
    df['Date'] = f"{current_df_date}/2021"

# ===============================================
    # Drop unncessary column 
    # drop_cols = ['Locations', 
    #          'Teams',
    #          'Base Hourly',
    #         #  'Clerks - Base Hourly', 
    #         #  'Clerks - Casual Base',             
    #         #  'Clerks - OT x1.5', 
    #         #  'Clerks - OT x2.0', 
    #         #  'NOR1', 
    #         #  'NOR1.25', 
    #         #  'NOR1.3',
    #          'OT1.5', 
    #         #  'OT1.6', 
    #         #  'OT2', 
    #         #  'OT2.1', 
    #          'Transport Allowance'
    #          ] 

    # df = df.drop(drop_cols, axis=1)
# ===============================================

    df['tanda_start_time'] = pd.to_datetime(df['Date'] + " " + df['Start'], format="%d/%B/%Y %I:%M %p")
    df['Breaks'] = pd.to_numeric(df['Breaks'], errors='coerce')
    df['tanda_end_time'] = df['tanda_start_time']+ pd.to_timedelta(df.Length, unit='h') + pd.to_timedelta(df.Breaks, unit='T')

    # can user  .dt  to limit return format 

    # Process Name
    df[['firstname', 'lastname']]= df.Name.str.strip().str.lower().str.split(" ", 1, expand=True)

    df['middlename'] = [middlename.strip().rsplit(" ", 1)[0] if len(middlename.strip().rsplit(" ")) > 1 else 'nomiddlename' for middlename in df.lastname]
    df['lastname'] = [lastname.strip().rsplit(" ", 1)[1] if len(lastname.strip().rsplit(" ")) > 1 else lastname for lastname in df.lastname]

    # end time reformat
    df['tanda_end_time'] = df['tanda_end_time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['tanda_end_time'] = pd.to_datetime(df['tanda_end_time'], format="%Y-%m-%d %H:%M:%S")

    return df

# Join df together , if not first element


concat_dfs = pd.concat([tanda_pc_manual(dfs, sheet) for sheet in all_sheetnames])

concat_dfs = concat_dfs.sort_values(['firstname', 'tanda_start_time'], ascending=(True, True))

# remove unnecessary column one by one 


# ===============================================
    # Drop unncessary column 
drop_cols = [
            'Locations', 
            'Teams',
            'Base Hourly',
            'Clerks - Base Hourly', 
            'Clerks - Casual Base',             
            'Clerks - OT x1.5', 
            # 'Clerks - OT x2.0', 
            'NOR1', 
            'NOR1.25', 
            'NOR1.3',
            'OT1.5', 
            'OT1.6', 
            'OT2', 
            'OT2.1', 
            'Transport Allowance'
        ] 

concat_dfs = concat_dfs.drop(drop_cols, axis=1)
# ===============================================

# clean the names and employee ID
concat_dfs['lastname'] = concat_dfs['lastname'].str.strip()
concat_dfs['firstname'] = concat_dfs['firstname'].str.strip()


# Filter Non-Drivers

ROSTER_DRIVERS = [
        'ir02', 'ir12', 'ir20', 'irdeaz','subcon1',
        'swaklado','swbaichr','swbranat', 'swburlei',
        'swdinvie','swdoalb','swedwben','swfiejih',
        'swhearay','swhewg','swjusjoh','swkuma',
        'swlip','swliqi','swlocbra','swmittai',
        'swmoylou','swnevpj','swrigda','swrobg',
        'swrobgar','swshekev','swsinvic','swtaujul',
        'swtubjoh','swtupfek','swwarrob','swwhinei','swhopdam'
        ]




concat_dfs.to_csv(COMPLETE_PATH, index=False)



