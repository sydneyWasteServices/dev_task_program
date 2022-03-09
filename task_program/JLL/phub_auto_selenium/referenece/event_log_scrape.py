from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd 
import numpy as np 


DRIVER_PATH = '/home/gordon-workspace/local_workspace/web_scrape/chromedriver'

driver = webdriver.Chrome(DRIVER_PATH)

data = {}
time_arr = []
controller_arr = []
direction_arr = []
site_arr = []
credentials_arr = []
group_arr = []
staff_arr = []
event_arr = []

all_rows = []

driver.get("https://login1.ironlogic.com.au/login")


webLoginjs = open('./js.txt', "r")
webLogin = webLoginjs.read()

driver.execute_script(webLogin)

time.sleep(3)


clickWebPortalJs = open('./web_portal.txt', "r")

clickWebPortal = clickWebPortalJs.read()

driver.execute_script(clickWebPortal)


for x in range(200):

    html = driver.find_element_by_xpath('//*')

    html_doc = html.get_attribute('innerHTML')

    soup = bs(html_doc, 'html.parser')

    tb = soup.table

    rows = tb.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        rows_array = []

        for col in cols: 
            rows_array.append(col.text)
        
        all_rows.append(rows_array)
        
    next = "var next = document.querySelector('[aria-label=\"Next\"]'); next.click()"

    driver.execute_script(next)

all_rows = [x for x in all_rows if x != []]


df = pd.DataFrame(all_rows,columns=['Time', 'Controller', 'Direction', 'Site', 'Credentials', 'Group', 'Staff', 'Event'])


df.to_csv("./boomgate_event_log.csv", index=False)




# for r in :
#     if len(r) == 0

    # time_arr.append(cols[0].td.text)
    # controller_arr.append(cols[1].text)
    # direction_arr.append(cols[2].text) 
    # site_arr.append(cols[3].text)
    # credentials_arr.append(cols[4].text)
    # group_arr.append(cols[5].text)
    # staff_arr.append(cols[6].text)
    # event_arr.append(cols[6].text)



    
# data['time'] =  time_arr
# data['controller'] = controller_arr
# data['direction'] = direction_arr
# data['site'] = site_arr
# data['credentials'] = credentials_arr
# data['group'] = group_arr
# data['staff'] = staff_arr
# data['event'] = event_arr

# table_doc = soup.find('table')

# table_doc

# print(table_doc)


# var next = document.querySelector('[aria-label="Next"]'); next.click();



# var burger = document.querySelector('[data-target="#headerMenuCollapse"]');

# burger.click();

# var eventLog = document.querySelector('[routerlink="events_log/-1"]');

# eventLog.click();

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()


