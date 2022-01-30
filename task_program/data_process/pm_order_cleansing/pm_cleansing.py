import pandas as pd 
import numpy as np
import re

class PM_data_cleansing:
    def __init__(self):
        pass
    
    def unbundle_address(self, df):
        if df.Description.startswith('PRY'):
            return df.Description.split("-",3)
        else:
            return df.Description.split("-",2)
        
    def select_state(self, df):
        states = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'VIC', 'TAS', 'WA']
        if df.address_1[0].strip() in states: 
            return df.address_1[0].strip()
        elif df.address_1[0].strip().startswith('PRY'):
            return df.address_1[1].strip()
        else:
            return ""

    def select_bulkBill(self, df):
        if df.address_1[0].strip().startswith('PRY'):
            return df.address_1[0].strip()
        else:
            return ""

    def select_location(self, df):
        states = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'VIC', 'TAS', 'WA']
        if df.address_1[0].strip() in states: 
            return df.address_1[1].strip()
        elif df.address_1[0].strip().startswith('PRY'):
            return df.address_1[2].strip()
        else:
            return "null"

    def extra_bracket_items(self, df):
        pattern = "\(\d\)\.?\s(.*?)\."
        results = re.findall(pattern, df.Description)
        
        if results != []:
            return results
        else: 
            count = re.findall(" / ", df.Description)
            resultsArr = df.Description.split(" / ", len(count))
            if resultsArr != []:
                return resultsArr
            else:
                return np.nan

    def identify_month_key(self, df):
        monthPattern = "(monthly)|(month)"
        results = re.findall(monthPattern, df.Description)
        return len(results) 

    def identify_annual_key(self, df):
        annualPattern = "(annually)|(annual)"
        results = re.findall(annualPattern, df.Description)
        return len(results) 

    def identify_quarter_key(self, df):
        quarterPattern = "(quarterly)|(quarter)"
        results = re.findall(quarterPattern, df.Description)
        return len(results) 

    def identify_week_key(self, df):
        weekPattern = "(weekly)|(week)"
        results = re.findall(weekPattern, df.Description)
        return len(results)