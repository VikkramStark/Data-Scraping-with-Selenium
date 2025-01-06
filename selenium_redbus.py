# !pip install selenium
#importing libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
#open the browser for KERALA

driver=webdriver.Chrome()

#load the webpage

driver.get("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile")

time.sleep(3)

driver.maximize_window()
#retrive  bus links and route
wait = WebDriverWait(driver, 20)
def Kerala_link_route(path):   
    LINKS_KERALA=[]
    ROUTE_KERALA=[]
    # retrive the route links 
    for i in range(1,3):
        paths=driver.find_elements(By.XPATH,path)
        
        for links in paths:
            d = links.get_attribute("href")
            LINKS_KERALA.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_KERALA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_KERALA,ROUTE_KERALA

LINKS_KERALA,ROUTE_KERALA=Kerala_link_route("//a[@class='route']")
df_k=pd.DataFrame({"Route_name":ROUTE_KERALA,"Route_link":LINKS_KERALA})
df_k
# change dataframe to csv
path=r"./redbus/df_k.csv"
df_k.to_csv(path,index=False)
#open the browser for ANDHRA

driver_A=webdriver.Chrome()

#load the webpage
driver_A.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")

time.sleep(3)

driver_A.maximize_window()

#retrive  bus links and route
wait = WebDriverWait(driver_A, 20)
def Andhra_link_route(path):   
    LINKS_ANDHRA=[]
    ROUTE_ANDHRA=[]
    # retrive the route links 
    for i in range(1,5):
        paths=driver_A.find_elements(By.XPATH,path)
        
        for links in paths:
            d = links.get_attribute("href")
            LINKS_ANDHRA.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_ANDHRA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_ANDHRA,ROUTE_ANDHRA

LINKS_ANDHRA,ROUTE_ANDHRA=Andhra_link_route("//a[@class='route']")
df_A=pd.DataFrame({"Route_name":ROUTE_ANDHRA,"Route_link":LINKS_ANDHRA})
df_A
# change dataframe to csv
path=r"./redbus/df_A.csv"
df_A.to_csv(path,index=False)
#open the browser for TELUNGANA

driver_T=webdriver.Chrome()

#load the webpage
driver_T.get("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile")

time.sleep(3)

driver_T.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_T, 20)
def Telugana_link_route(path):   
    LINKS_TELUGANA=[]
    ROUTE_TELUGANA=[]
    
    for i in range(1,4):
        paths=driver_T.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_TELUGANA.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_TELUGANA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_TELUGANA,ROUTE_TELUGANA

LINKS_TELUGANA,ROUTE_TELUGANA=Telugana_link_route("//a[@class='route']")
df_T=pd.DataFrame({"Route_name":ROUTE_TELUGANA,"Route_link":LINKS_TELUGANA})
df_T
# change dataframe to csv
path=r"./redbus/df_T.csv"
df_T.to_csv(path,index=False)
#open the browser for GOA

driver_G=webdriver.Chrome()

#load the webpage
driver_G.get("https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile")

time.sleep(3)

driver_G.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_G, 20)
def Kadamba_link_route(path):   
    LINKS_KADAMBA=[]
    ROUTE_KADAMBA=[]
    
    for i in range(1,4):
        paths=driver_G.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_KADAMBA.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_KADAMBA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_KADAMBA,ROUTE_KADAMBA

LINKS_KADAMBA,ROUTE_KADAMBA=Kadamba_link_route("//a[@class='route']")
df_G=pd.DataFrame({"Route_name":ROUTE_KADAMBA,"Route_link":LINKS_KADAMBA})
df_G
# change dataframe to csv
path=r"./redbus/df_G.csv"
df_G.to_csv(path,index=False)
#open the browser for RAJASTHAN

driver_R=webdriver.Chrome()

#load the webpage
driver_R.get("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile")

time.sleep(3)

driver_R.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_R, 20)
def Rajastan_link_route(path):   
    LINKS_RAJASTAN=[]
    ROUTE_RAJASTAN=[]
    
    for i in range(1,4):
        paths=driver_R.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_RAJASTAN.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_RAJASTAN.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_RAJASTAN,ROUTE_RAJASTAN

LINKS_RAJASTAN,ROUTE_RAJASTAN=Rajastan_link_route("//a[@class='route']")
df_R=pd.DataFrame({"Route_name":ROUTE_RAJASTAN,"Route_link":LINKS_RAJASTAN})
df_R
# change dataframe to csv
path=r"./redbus/df_R.csv"
df_R.to_csv(path,index=False)
#open the browser for SOUTHBENGAL

driver_SB=webdriver.Chrome()

#load the webpage

driver_SB.get("https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile")

time.sleep(3)

driver_SB.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_SB, 20)
def Southbengal_link_route(path):   
    LINKS_SOUTHBENGAL=[]
    ROUTE_SOUTHBENGAL=[]
    
    for i in range(1,6):
        paths=driver_SB.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_SOUTHBENGAL.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_SOUTHBENGAL.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_SOUTHBENGAL,ROUTE_SOUTHBENGAL

LINKS_SOUTHBENGAL,ROUTE_SOUTHBENGAL=Southbengal_link_route("//a[@class='route']")
df_SB=pd.DataFrame({"Route_name":ROUTE_SOUTHBENGAL,"Route_link":LINKS_SOUTHBENGAL})
df_SB
# change dataframe to csv
path=r"./redbus/df_SB.csv"
df_SB.to_csv(path,index=False)
#open the browser for HARYANA

driver_H=webdriver.Chrome()

#load the webpage

driver_H.get("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile")

time.sleep(3)

driver_H.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_H, 20)
def Haryana_link_route(path):   
    LINKS_HARYANA=[]
    ROUTE_HARYANA=[]
    
    for i in range(1,6):
        paths=driver_H.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_HARYANA.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_HARYANA.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_HARYANA,ROUTE_HARYANA

LINKS_HARYANA,ROUTE_HARYANA=Haryana_link_route("//a[@class='route']")
df_H=pd.DataFrame({"Route_name":ROUTE_HARYANA,"Route_link":LINKS_HARYANA})
df_H
# change dataframe to csv
path=r"./redbus/df_H.csv"
df_H.to_csv(path,index=False)
#open the browser for ASSAM

driver_AS=webdriver.Chrome()

#load the webpage

driver_AS.get("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile")

time.sleep(3)

driver_AS.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_AS, 20)
def Assam_link_route(path):   
    LINKS_ASSAM=[]
    ROUTE_ASSAM=[]
    
    for i in range(1,5):
        paths=driver_AS.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_ASSAM.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_ASSAM.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_ASSAM,ROUTE_ASSAM

LINKS_ASSAM,ROUTE_ASSAM=Assam_link_route("//a[@class='route']")
df_AS=pd.DataFrame({"Route_name":ROUTE_ASSAM,"Route_link":LINKS_ASSAM})
df_AS
# change dataframe to csv
path=r"./redbus/df_AS.csv"
df_AS.to_csv(path,index=False)
#open the browser for UP

driver_UP=webdriver.Chrome()

#load the webpage

driver_UP.get("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile")

time.sleep(3)

driver_UP.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_UP, 20)
def UP_link_route(path):   
    LINKS_UP=[]
    ROUTE_UP=[]
    
    for i in range(1,6):
        paths=driver_UP.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_UP.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_UP.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_UP,ROUTE_UP

LINKS_UP,ROUTE_UP=UP_link_route("//a[@class='route']")
df_UP=pd.DataFrame({"Route_name":ROUTE_UP,"Route_link":LINKS_UP})
df_UP
# change dataframe to csv
path=r"./redbus/df_UP.csv"
df_UP.to_csv(path,index=False)
#open the browser for WESTBENGAL

driver_WB=webdriver.Chrome()

#load the webpage

driver_WB.get("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile")

time.sleep(3)

driver_WB.maximize_window()
#retrive bus links and route
wait = WebDriverWait(driver_WB, 20)
def Westbengal_link_route(path):   
    LINKS_WESTBENGAL=[]
    ROUTE_WESTBENGAL=[]
    
    for i in range(1,6):
        paths=driver_WB.find_elements(By.XPATH,path)
        # retrive the route links 
        for links in paths:
            d = links.get_attribute("href")
            LINKS_WESTBENGAL.append(d)
            
        # retrive names of the routes
        for route in paths:
            ROUTE_WESTBENGAL.append(route.text)
            
        try:
            # Wait for the pagination element to be present
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            time.sleep(3)
            next_button.click()
            
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
            
    return LINKS_WESTBENGAL,ROUTE_WESTBENGAL

LINKS_WESTBENGAL,ROUTE_WESTBENGAL=Westbengal_link_route("//a[@class='route']")
df_WB=pd.DataFrame({"Route_name":ROUTE_WESTBENGAL,"Route_link":LINKS_WESTBENGAL})
df_WB
# change dataframe to csv
path=r"./redbus/df_WB.csv"
df_WB.to_csv(path,index=False)
# concat all the bus link and route names in one dataframe
df=pd.concat([df_k,df_A,df_T,df_G,df_R,df_H,df_SB,df_AS,df_UP,df_WB],ignore_index=True)
df
# change dataframe to csv
path=r"./redbus/df_route.csv"
df.to_csv(path,index=False)