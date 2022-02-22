from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd 
import numpy as np 

DRIVER_PATH = "../chromedriver"

USER = "gordon.tang"
PASSWORD = "UZAevt8$"


if __name__ == "__main__":
	driver = webdriver.Chrome(DRIVER_PATH)

	driver.get("https://apps.jll.com/PortfolioTracker/OneView/Master.aspx?nClientID=6503")
	time.sleep(2)

	# input-validation-error inp inp-usr
	
	# second page 
	# Question 
	# id -> #input38

	#checkbox 
	# #input46


	# button button-primary


