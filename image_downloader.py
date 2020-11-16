
from selenium import webdriver
import time
import os

###PATHS########
download_path = r'Downloads'
chromedriver_path = r'chromedriver_win32\chromedriver.exe'
################

# Initialize Chrome Driver
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chromeOptions)

#Support Functions
def download_page(driver):
    i = 1
    while(True):
        try:
            driver.find_elements_by_xpath(f'/html/body/div[1]/div[4]/div/div/ul/li[{i}]/div[3]/label[4]/a')[0].click()
            i+=1
        except:
            break
    return i

def change_page(driver,curr_page):
    try:
        curr_page = driver.find_element_by_xpath(f'/html/body/div[1]/div[4]/div/div/div[2]/div[{curr_page+1}]/a').click()
        time.sleep(3)
        return 1
    except:
        return 13

##Visit the website
base_link = 'https://www.bigboytoyz.com/wallpaper'
driver.maximize_window()
driver.get(base_link)

#Start Downloading
curr_page = 1
while(curr_page<= 12):
    download_page(driver)
    change_page(driver,curr_page)
    curr_page+=1

# Remove duplicates
all_paths = os.listdir('Downloads')
all_paths = [i for i in all_paths if '(' in i]
for i in all_paths:
    os.remove(f'Downloads/{i}')
    