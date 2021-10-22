import pandas as pd
import numpy as np
import xlwings as xw
# Revenue is done

# Split Salary Cost
# Split any toll Cost
# Split any fuel Cost


PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\booking_weekly\\17th_2021.csv'

COMPLETE_PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\UOS_Split\\17th_2021.xlsx'


df = pd.read_csv(PATH, dtype={"Schd Time Start": str, "PO": str})
UOS = ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']
df['Route number'] = df['Route number'].str.split('-', 1, expand=True)[0]
df_UOS = df[df['Route number'].isin(UOS)]

route_occurence = df_UOS.groupby(['Date','Route number'])['Job No'].count().reset_index()
route_total = df_UOS.groupby(['Date'])['Job No'].count()


df_uos_counts = pd.merge(route_occurence, route_total, how='left', on='Date')

df_uos_counts['portion'] = df_uos_counts.pipe(lambda data : data['Job No_x']/ data['Job No_y'])

df_uos_counts = df_uos_counts.rename(columns={'Job No_x' : 'occurrence' , 'Job No_y' : 'total' })


df_uos = df_uos_counts[df_uos_counts['Route number'].str.startswith('UOS')] 

df_cum = df_uos_counts[df_uos_counts['Route number'].str.startswith('CUM')]

df_nep = df_uos_counts[df_uos_counts['Route number'].str.startswith('NEP')] 

df_cmd = df_uos_counts[df_uos_counts['Route number'].str.startswith('CMD')]


df_uos['Route_initial'] = 'uos'

df_cum['Route_initial'] = 'cum'

df_nep['Route_initial'] = 'nep'
 
df_cmd['Route_initial'] = 'cmd'


df_split_route = pd.concat([df_uos, df_cum, df_nep, df_cmd])

df_split_route_cb = df_split_route[df_split_route['Route number'].str.endswith('CB')]

df_split_route_gw = df_split_route[df_split_route['Route number'].str.endswith('GW')]

df_split_route_co = df_split_route[df_split_route['Route number'].str.endswith('CO')]

df_split_route_cb['Route_type'] = 'cb'

df_split_route_gw['Route_type'] = 'gw'

df_split_route_co['Route_type'] = 'co'

# Nathan usually drive Cardboard
# Rob Drive General Waste

df_ds = pd.concat([df_split_route_cb, df_split_route_gw, df_split_route_co]).sort_values('Route_initial')

df_count_total = df_ds.groupby(['Route_initial'])['occurrence'].sum().reset_index()

df_uos_split_count = df_ds.groupby(['Route_initial','Route_type'])['occurrence'].sum().reset_index()

df_com = pd.merge(df_uos_split_count, df_count_total , how='left', on='Route_initial')

df_com['portion'] = df_com.pipe(lambda data : data['occurrence_x'] / data['occurrence_y'] )

df_com = df_com[['Route_initial', 'Route_type' ,'portion']]


wb = xw.Book()

wb.sheets[0].name = 'UOS_split'

wb.sheets[1].name = 'dataSet'

wb.sheets[0].range('A1').value = df_com

wb.sheets[1].range('A1').value = df_ds

wb.save(COMPLETE_PATH)
wb.close()