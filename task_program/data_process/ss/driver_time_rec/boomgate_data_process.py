import pandas as pd
import numpy as np

# Boomgate Last, first and middle name are not accurates 
# use ID
# use Groupby name make sure IDs are correct



PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\boomgate\\18th_2021.xlsx'
COMPLETE_PATH = 'D:\\Run Analysis\\BLOB_STORAGE\\boomgate\\processed\\18th_2021_processed.csv'
ROSTER_DRIVERS = [
        'ir02', 'ir12', 'ir20', 'irdeaz','subcon1',
        'swaklado','swbaichr','swbranat', 'swburlei',
        'swdinvie','swdoalb','swedwben','swfiejih',
        'swhearay','swhewg','swjusjoh','swkuma',
        'swlip','swliqi','swlocbra','swmittai',
        'swmoylou','swnevpj','swrigda','swrobg',
        'swrobgar','swshekev','swsinvic','swtaujul',
        'swtubjoh','swtupfek','swwarrob','swwhinei'
        ]


df = pd.read_excel(PATH, header=1, engine='openpyxl')

# drop mutiple columns
df = df.drop(['Location','Duration','Rate','Total'], axis=1)


# Extract ID
df['EmployeeID'] = (df[df.Employee.str.contains('_',regex=False)]
                    .Employee
                    .str.split("_",1,expand =True)[0])

# split string by underscore 
# not useful yet 
# print(df.Employee.str.extract(r'^(.*)(_.*?)$', expand=True))

# split string by _ if no _ use orginal string
df['Employee'] = [x.split("_")[1] if len(x.split("_")) > 1 else x.split("_")[0] for x in df.Employee]

# Remove the number at the end
df['Employee']= df.Employee.str.rsplit(" ",1,expand=True)[0]


df['Employee'] = df.Employee.str.lower().str.strip()

# process first name / last name
df[['lastname','firstname']] = df.Employee.str.split(" ", 1, expand=True)

# ===================================================================
df['lastname'] = df['lastname'].str.strip()

df['firstname'] = df['firstname'].str.strip()
# ===================================================================


# Fill nan to empty cell in firstname
df['firstname'] = df['firstname'].fillna('nofirstname')


# Split middlename from last name
df['middlename'] = [middlename.split(" ")[1] if len(middlename.split(" ")) > 1 else 'nomiddlename' for middlename in df.firstname]

# Split last name  from middle name 
df['firstname'] = [firstname.split(" ")[0] if len(firstname.split(" ")) > 1 else firstname for firstname in df.firstname]


# to select Operations only

df['Department'] = df.Department.str.lower()
df['Department'] = df['Department'].fillna(' ')
df = df[df.Department.str.lower().str.startswith('operations')]
df.pop('#')



# remove entry event string and put it in Time In

df['Time In'] = [entryEvent.split("at")[1].strip().rsplit(":", 1)[0] if entryEvent.lower().startswith('entry') else entryEvent for entryEvent in df['Time In']]

# remove exit event string and put it in Time Out
df['Time Out'] = [exitevent.split("at")[1].strip().rsplit(":", 1)[0] if exitevent.lower().startswith('exit') else df['Time Out'].iloc[i] for i, exitevent in enumerate(df['Time In'])]

# remove all exit event in Time In Column 
df['Time In'] = [np.nan if entryEvent.lower().startswith('exit') else entryEvent for entryEvent in df['Time In']]


# Convert Time In  String  to date time 
df['Time In']= pd.to_datetime(df['Time In'], format='%d/%m/%Y %H:%M')

# Convert Time Out  String  to date time 
df['Time Out']= pd.to_datetime(df['Time Out'], format='%d/%m/%Y %H:%M')

# Sort by firstname and Time In
df = df.sort_values(["firstname", "Time In"], ascending = (True, True))

# lowercase ID
df['EmployeeID'] = df['EmployeeID'].str.lower()

# ===================================================================
df['lastname'] = df['lastname'].str.strip()

df['firstname'] = df['firstname'].str.strip()
# ===================================================================

# df = df[df.EmployeeID.isin(ROSTER_DRIVERS)]

df.to_csv(COMPLETE_PATH, index=False)

# np.nan won't make to-datetime crash


