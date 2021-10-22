import pandas as pd 
import numpy as np

# salary timesheet Naming problem
#  Burgess, Leigh has issues 
#  NaN	 Bejamin edwards	bejamin => correct salary timesheet  => to Benjamin
#  NaN	Fei , Xia  xia => Xiaohua => correct salary timesheet  => to Xiaohua
# NaN	Dean, Zac  Zac => zaheer => correct salary timesheet  => to zaheer 
# NaN	Ruhr, John => johann => correct salary timesheet  => to johann
# Dinh, Viet Hong Phuoc /  Do , Albertran  are duplicate


# EmployeeID list issue
# NaN	Roberts , Garry => correct Employee ID => to Garry
#  NaN	Fei , Xia  xia => EmpID


# Remember to change file name 
PATH_SAL = 'D:\\Run Analysis\\BLOB_STORAGE\\Driver_weekly_timesheet\\to_process_timesheet\\15th_2021.xlsx'

PATH_EMP = 'D:\\Run Analysis\\BLOB_STORAGE\\EmployeeID.csv'

PATH_COMPLETED = 'D:\\Run Analysis\\BLOB_STORAGE\\Driver_weekly_timesheet\\processed_timesheet\\15th_2021.csv'


df = pd.read_excel(PATH_SAL)
df_emp = pd.read_csv(PATH_EMP)
# df.pop('Unnamed: 26')

df = df.rename(columns={'Employee ID' : 'EmployeeID'})

df['Employee Name'] = df['Employee Name'].str.replace('*','')

df['EmployeeID'] = df['EmployeeID'].str.lower()

df[['lastname', 'firstname']] = df['Employee Name'].str.lower().str.split(",", 1, expand=True)

df['lastname'] = df['lastname'].str.strip()
df['firstname'] = df['firstname'].str.strip()

df['lastname'] = [lastname.split(" ")[1] if len(lastname.strip().split(" ")) > 1 else lastname for lastname in df.lastname]

df['middlename'] = [middlename.split(" ")[1] if len(middlename.split(" ")) > 1 else 'nomiddlename' for middlename in df.firstname]

df['firstname'] = [firstname.split(" ")[0] if len(firstname.split(" ")) > 1 else firstname for firstname in df.firstname]

df['lastname'] = df['lastname'].str.strip()
df['firstname'] = df['firstname'].str.strip()

df_empID_sal = pd.merge(df, df_emp, on=['firstname', 'lastname'], how='left')

df_empID_sal = df_empID_sal[['EmployeeID_y', 'Employee Name','lastname','firstname','middlename_x','Total']]

df_empID_sal = df_empID_sal.rename(columns={'Total' : 'Total_hour'})

df_empID_sal = df_empID_sal.drop_duplicates(subset='EmployeeID_y',keep='first')

df_empID_sal.to_csv(PATH_COMPLETED, index=False)



# 1. TO_csv transformed Salary timesheet => 
# 2. and then merge it with employee ID
# 3. remove Salary Timesheet employee ID 
