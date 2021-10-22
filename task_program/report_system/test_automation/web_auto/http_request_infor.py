# import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium

url = 'https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999'
# url = 'https://au.finance.yahoo.com/quote/AMZN/options?p=AMZN'

# urllib.request.urlopen(url, ).read()
try:
    
    # reqURL = req.Request(url)
    # resp = requests.get(url, timeout=10)
    # resp_data = resp.text

    with open('data.txt','a') as f:
            f.write(resp_data)
            f.close()
except e:
    print(e)

# except (HTTPError, URLError) as error:
#     logging.error(
#         'Data of %s not retrieved because %s\nURL: %s', name, error, url)


# https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=60&fromdate=2021-06-18&todate=2021-06-18&excode=oprac&callput=callput&money=at&type=all
# https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999

# ALL Data from Nasdaq - change the Stock code 
# 'https://api.nasdaq.com/api/quote/AMZN/option-chain?assetclass=stocks&limit=99999&fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all'