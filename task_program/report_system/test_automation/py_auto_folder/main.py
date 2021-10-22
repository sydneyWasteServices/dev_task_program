import time
import ast
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time 
import _datetime
import os
import schedule
import typing

# print time

start_time = time.strftime('%X').replace(":",".")

# =ReadStock code=========
f_stock_list = open("./stock_code.txt", "r")
usa_stock_list= f_stock_list.readlines()[0]
usa_stock_list = ast.literal_eval(usa_stock_list)
# =ReadStock code=========

# shareCode = f{sharecode}
# ===============================================================
# Retain the state
class State:
    def __init__(self,num:int):
        self.num = int(num)

n = State(0)
print(n.num)
# ===============================================================

# =============================================================================
# Fetch stock data
def fetch_stock_data(x : int = 0, stock_list : list =usa_stock_list, num_of_run:int=3):

    for i in range(num_of_run):
        
        today = _datetime.date.today()
        share_code = stock_list[n.num]

        # =Web_Drive=======
        PATH = './chromedriver'
        driver = webdriver.Chrome(PATH)
        wait = WebDriverWait(driver, 60)
#  /c/Users/gordon/Desktop/codeVault/report_system/test_automation/py_auto_folder/test_sharecode_infor
        filename = f"./test_sharecode_infor/{today}_{start_time}_{share_code}.txt"
        f = open(filename, "w+")


        try:
            api_url = f"https://api.nasdaq.com/api/quote/{share_code}/option-chain?assetclass=stocks&limit=99999&fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all"
            driver.get(api_url)    
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
            content = "return document.querySelector('pre').innerHTML"
            html = driver.execute_script(content)
            f.write(html)

        except Exception as ex:
            if hasattr(ex, 'message'):
                f.write(ex.message)
                f.close()
                error_time = time.strftime('%X').replace(":",".")
                os.rename(f"{filename}", f"./error_report/{filename}_{error_time}_error.txt")
            else:
                f.write(ex)
                f.close()
                error_time = time.strftime('%X').replace(":",".")
                os.rename(f"{filename}", f"./error_report/{filename}_{error_time}_error.txt")

            print("not working")
            driver.quit()
            
        finally:
            driver.quit()
            f.close()
            n.num += 1
            print(n.num)
            if(n.num > 3650):
                print("hello")
                exit()
# =============================================================================

# Scheduling
# =============================================================================
schedule.every(1).to(3).seconds.do(fetch_stock_data)

while True: 
    schedule.run_pending() 
    time.sleep(1) 
    # Checks whether a scheduled task  
    # is pending to run or not 
   
# =============================================================================

# unit_test
# correct share_code
# time being scheduled
#  

# log report
