import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



file = r'C:\location.csv' #declaring CSV file; Need to change 
data_file = pd.read_csv(file, encoding='gbk', header=None) #loading CSF file
max_row = data_file.iloc[-1,0] #setting max range for last input in CSV
IncidentNum=data_file.iloc[0,0] #setting start range for CSV before while loop
#only reads one column of strings
print(max_row)

windowMax=0
while IncidentNum != max_row: #while string doesnt equal last string in CSV
    print(windowMax)
    IncidentNum=data_file.iloc[windowMax,0] #loading string from CSV into variable
    try:
        driver.get("https://google.com")
        window1 = driver.window_handles[0]
        time.sleep(1)


        driver.implicitly_wait(0.5)
        time.sleep(1)


        driver.get("https://"+IncidentNum+"")
        driver.execute_script("document.body.style.zoom='75%'")
        driver.fullscreen_window()
        time.sleep(1)
        driver.save_screenshot("C:/location/" + str(windowMax) + ".png") #saving screenshot location with counter

        windowMax += 1 #increasing counter
        time.sleep(2)
    except Exception as e: #catch errors when loading websites
        print(e)
        windowMax += 1 #increasing counter















driver.quit()
