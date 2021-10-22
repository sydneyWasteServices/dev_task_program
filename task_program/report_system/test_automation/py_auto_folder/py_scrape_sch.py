# import urllib.request as req

# import requests

# url = 'https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999'
# # url = 'https://au.finance.yahoo.com/quote/AMZN/options?p=AMZN'

# # urllib.request.urlopen(url, ).read()
# try:
    
#     # reqURL = req.Request(url)
#     resp = requests.get(url, timeout=10)
#     resp_data = resp.text

#     with open('data.txt','a') as f:
#             f.write(resp_data)
#             f.close()
# except e:
#     print(e)

# except (HTTPError, URLError) as error:
#     logging.error(
#         'Data of %s not retrieved because %s\nURL: %s', name, error, url)


# https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=60&fromdate=2021-06-18&todate=2021-06-18&excode=oprac&callput=callput&money=at&type=all
# https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999
# 'https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999&fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all'

# =======================================================

# chromedriver.exe --verbose --log-path=chromedriver.log
# 87.0.4280.141

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time 
import _datetime
import os
today = _datetime.date.today()

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 60)

share_code = "AMZN"

filename = f"{today}_{share_code}.txt"
f = open(filename, "w")

# os.rename(r'C:\Users\Ron\Desktop\Test\Products.txt',
# r'C:\Users\Ron\Desktop\Test\Shipped Products_' + str(Current_Date) + '.txt')


try:
    api_url = f"https://api.nasdaq.com/api/quote/{share_code}/option-chain?assetclass=stocks&limit=99999&fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all"
    driver.get(api_url)
# find_element_by_tag_name
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
    content = "return document.querySelector('pre').innerHTML"
    html = driver.execute_script(content)
    f.write(html)
    


except Exception as ex:
    if hasattr(ex, 'message'):
        f.write(ex.message)
        f.close()
        os.rename(f"{filename}.txt", f"{filename}_error.txt")
    else:
        f.write(ex)
        f.close()
        os.rename(f"{filename}.txt", f"{filename}_error.txt")

    print("not working")
    driver.quit()
    

finally:
    time.sleep(5)
    driver.quit()
    f.close()




# PATH = '/home/gordon/workplace/scrape/chromedriver'
# driver = webdriver.Chrome(PATH)
# wait = WebDriverWait(driver, 60)
# driver.get("https://www.pwc.com.au/careers/opportunities/results.html?wdcountry=AUS&wdjobsite=Global_Experienced_Careers")

# js_click_dropdown = "document.querySelector('span.caret').click()"
# js_click_all = "document.querySelector('div.dropdown-menu').children[3].click()"
# js_all_tr = "return document.querySelector('tbody').innerHTML"

# filename = f"{today}_pwcJobs.csv"
# f = open(filename, "w")
# headers = "job_id,job_title,job_title_link,location,line_of_service,specialism,industry,grade,apply_link,learn_more_link\n"
# f.write(headers)

# try:

#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "caret")))
#     spans = driver.find_elements_by_tag_name("span")
# ======================    
#     driver.execute_script(js_click_dropdown)
#     driver.execute_script(js_click_all)

#     html = driver.execute_script(js_all_tr)
        # ====================================
#     html_tr = bs(html, 'html.parser')
#     trs = html_tr.findAll("tr")
    # ====================================

#     print(f"TR len is {len(trs)}")

#     for tr in trs:
#         tds = tr.findAll("td")
        
#         job_title = tds[0].a.text.replace(",","")
#         job_title_link = tds[0].a['href']
#         location = tds[1].text.replace(",","")
#         line_of_service = tds[2].text.replace(",","")
#         specialism = tds[3].text.replace(",","")
#         industry = tds[4].text.replace(",","")
#         grade = tds[5].text.replace(",","")

#         apply_learn_links_a_tag = tds[6].findAll("a")
#         apply_link_tag = apply_learn_links_a_tag[0]
#         learn_more_tag = apply_learn_links_a_tag[1]

#         job_id = apply_link_tag.get('data-id')
#         apply_link = apply_link_tag.get('href')
#         learn_more_link = learn_more_tag.get('href')

#         # print(job_title)
#         # print(job_title_link)
#         # print(location)
#         # print(line_of_service)
#         # print(specialism)

#         if industry is not "" and "Not Applicable":
#             # print(f"{industry}")
#             write_industry = industry
#         else:
#             # print("Null")
#             write_industry = "NULL"
#         print(grade)

#         if job_id is not None:
#             # print(f"Job Id is {job_id}")
#             # print(f"Apply Link is {apply_link}")
#             write_job_id = job_id.replace(",","")
#             write_apply_link = apply_link.replace(",","")
#             # print("")
#         else:
#             # print("Job Id is empty")
#             write_job_id = "NULL"
#             write_apply_link = "NULL"
#             # print("")

#         if learn_more_link is not None:
#             # print(f"Learn More link is {learn_more_link}")
#             write_learn_more_link = learn_more_link.replace(",","")
#             # print("")
#         else:
#             # print("No link on Learn More")
#             write_learn_more_link = "NULL"
#             # print("")

#         print("")
        
#         f.write(f"{write_job_id},{job_title},{job_title_link},{location},{line_of_service},{specialism},{write_industry},{grade},{write_apply_link},{write_learn_more_link}\n")
#         print("")
        
# except Exception as ex:
#     if hasattr(ex, 'message'):
#         print(ex.message)
#     else:
#         print(ex)

#     print("not working")
#     driver.quit()
#     f.close()

# finally:
#     driver.quit()
#     f.close()


