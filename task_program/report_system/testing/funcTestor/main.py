# os.path.dirname(__file__) just gives you the directory that your current python file is in,
#  and then we navigate to 'Common/' the directory and import 'Common' the module.

import sys, os
# C:\\Users\\gordon\\Desktop\\codeVault\\report_system\\
# sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\', 'revenue'))
# import Revenue as rev
# sys.path.append(os.path.join(os.path.dirname(__file__), 'C:\\Users\\gordon\\Desktop\\codeVault\\report_system\\revenue', 'revenue_by_type.py'))
# print(os.path)

# from revenue_by_type import Revenue_by_type
# revenue.
from ..revenue import Revenue
# revenue_by_type  Revenue
# Revenue_by_type  

import pandas as pd 
import numpy as np


path = '../../../../ubuntuShareDrive/Datasets/booking/17.2.2021_24.2.2021.csv'
df = pd.read_csv(path)

df1 = df.head(2)
print(df1)
 