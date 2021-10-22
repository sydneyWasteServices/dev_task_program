import pandas as pd
import numpy as np

PATH = 'D:\\Run Analysis\\WEEKLY_SUMMARY\\all_weeks_analysis.xlsx'

df = pd.read_excel(PATH)

GW = ['HOOK1','BR1','BR2','BR3','FL2','FLG','RL1','RL2','RL4','RL7','RL9','RLD','RLE','RLH','RLI','RLJ','RLK','SWG','UOSGW']             

CB = ['FLP','HYG','RED','RL5','RL6','RL8','RLP','RLR','HOOKCB' ,'UOSCB']

# CB RUNS
df = df[df.Route_number.isin(CB)]

measures = df.iloc[:,3:].columns

for measure in measures:
        df[measure] = pd.to_numeric(df[measure], errors='coerce')
        
df = df.fillna(0)

df = df.sort_values(by=['Start_date'], ascending=True)

df['Op_margin'] = (
    df.Total_income - 
    df.General_Waste_Cost - 
    df.Co_mingle_Cost + 
    df.Cardboard_rebate - 
    df.Driver_salary - 
    df.MV_Fuel - 
    df.MV_Rego - 
    df.MV_Tolls - 
    df.MV_Insurance - 
    df.Repair_Maintenance_Cab_Chassic - 
    df.Repair_Maintenance_Compactor_Body - 
    df.Repair_Maintenance_Misc_Cosumables - 
    df.Repair_Maintenance_Tyres - 
    df.Workshop_Contractor_Labour - 
    df.MV_exp_Others - 
    df.General_Administration )

# ====================================================== GW Business Intell ======================================================

df_bi = (df
    .groupby(
        ['Start_date',
         'end_date',]
    )[
    'Total_income', 
    'General_Waste_Cost', 
    'Cardboard_weight',
    'Driver_salary',
    'Workshop_Contractor_Labour',
    'General_Administration'
     ].sum().reset_index())





def prev_period_item(col_name: str):
    
    prevWk_col_name = f'prevWk_{col_name}'
    df_bi[prevWk_col_name] = df_bi[col_name].shift(1)   

measures = df_bi.columns

[prev_period_item(measure) for measure in measures]

df_bi = df_bi.iloc[1:,:]


df_bi['Start_date'] = df_bi['Start_date'].dt.strftime('%d %B %y')
df_bi['end_date'] = df_bi['end_date'].dt.strftime('%d %B %Y')

df_bi['prevWk_Start_date'] = df_bi['prevWk_Start_date'].dt.strftime('%d %B %y')
df_bi['prevWk_end_date'] = df_bi['prevWk_end_date'].dt.strftime('%d %B %Y')

df_bi['Start_date'] = df_bi.Start_date.str.rsplit(' ', 1,expand=True)[0]
df_bi['Current Period'] = df_bi.Start_date.str.cat(df_bi.end_date, sep=" to ")

df_bi['prevWk_Start_date']= df_bi.prevWk_Start_date.str.rsplit(' ', 1,expand=True)[0]
df_bi['Previous period'] = df_bi.prevWk_Start_date.str.cat(df_bi.prevWk_end_date, sep=" to ")


df_bi = df_bi[[

    'Previous period',
    'prevWk_Total_income',
    'prevWk_Cardboard_rebate',
    'prevWk_Cardboard_weight',
    'prevWk_Driver_salary',
    'prevWk_Workshop_Contractor_Labour',
    'Current Period', 
    'Total_income', 
    'Cardboard_rebate',
    'Cardboard_weight',
    'Driver_salary',
    'Workshop_Contractor_Labour',
    'General_Administration'

]]




# ====================================================== CB Business Intell ======================================================

df_bi['Changes on Income'] = df_bi.Total_income - df_bi.prevWk_Total_income
df_bi['Changes on Income%'] = (df_bi.Total_income - df_bi.prevWk_Total_income ) / df_bi.prevWk_Total_income   

df_bi['Changes on Rebate'] = df_bi.Cardboard_rebate - df_bi.prevWk_Cardboard_rebate
df_bi['Changes on Rebate%'] = (df_bi.Cardboard_rebate - df_bi.prevWk_Cardboard_rebate) / df_bi.prevWk_Cardboard_rebate

df_bi['Changes on Tip'] = df_bi.Cardboard_weight - df_bi.prevWk_Cardboard_weight
df_bi['Changes on Tip%'] = (df_bi.Cardboard_weight - df_bi.prevWk_Cardboard_weight) / df_bi.prevWk_Cardboard_weight

df_bi['Changes on Driver Salary'] = df_bi.Driver_salary - df_bi.prevWk_Driver_salary
df_bi['Changes on Driver Salary%'] = (df_bi.Driver_salary - df_bi.prevWk_Driver_salary) / df_bi.prevWk_Driver_salary     

df_bi['Changes on Workshop Labour Cost'] = df_bi.Workshop_Contractor_Labour - df_bi.prevWk_Workshop_Contractor_Labour
df_bi['Changes on Workshop Labour Cost%'] = (df_bi.Workshop_Contractor_Labour - df_bi.prevWk_Workshop_Contractor_Labour) / df_bi.prevWk_Workshop_Contractor_Labour         

df_bi = df_bi[[
    'Previous period',
    'prevWk_Total_income',
    'prevWk_Cardboard_rebate',
    'prevWk_Cardboard_weight',
    'prevWk_Driver_salary',
    'prevWk_Workshop_Contractor_Labour',
    'Current Period', 
    'Total_income',
    'Changes on Income', 
    'Changes on Income%',
    'Cardboard_rebate',
    'Changes on Rebate',
    'Changes on Rebate%',
    'Cardboard_weight',
    'Changes on Tip',
    'Changes on Tip%',
    'Driver_salary',
    'Changes on Driver Salary',
    'Changes on Driver Salary%',
    'Workshop_Contractor_Labour',
    'Changes on Workshop Labour Cost',
    'Changes on Workshop Labour Cost%',
    'General_Administration'
]]


# # df_bi = df_bi.style.format({
# #     'Changes on Income%' : "{:.2%}",
# #     'Changes on Rebate%' : "{:.2%}", 
# #     'Changes on Tip%' : "{:.2%}"  
# # })

COMPLETE_PATH = 'D:\\Run Analysis\\WEEKLY_SUMMARY\\BI_analysis\\finance_trend_analysis\\cb_income_comparsion_tableV1.xlsx'   
df_bi.T.to_excel(COMPLETE_PATH)

