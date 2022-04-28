# Scraping certificates from DataQuest 
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## Navigate to Dataquest. 

# # Selenium Web Driver specifically for chrome
# driver = webdriver.Chrome(ChromeDriverManager().install())
# # Link to dataquest
# link_to_profile = "https://app.dataquest.io/profile/gerald.wogan"
# # Open webpage
# driver.get(link_to_profile)

# ## Scrape list of links to certs
# cert_links = []
# # identify elements with tagname <a>
# links = driver.find_elements(by=By.TAG_NAME, value='a') 

# # traverse list
# for elem in links:
#     # get_attribute() to get all hrefs
#     href = elem.get_attribute('href')
#     if 'view_cert' in str(href):
#         cert_links.append(href)
# print(len(cert_links), 'certificate links found')

## For each cert
# for link in cert_links:
#     ## Open link
#     driver.get(link)
# driver.get('https://app.dataquest.io/view_cert/Z4CMFNWE9WXCKKTYMWQE')
    ## Click Download
# b = driver.find_elements(by=By.TAG_NAME, value='button') 
# dl = b[-1]
# dl.click()
# time.sleep(1.5)

# Find downloaded certs
downloads_path = str(Path.home() / "Downloads")
get_files = []
for filename in os.listdir(downloads_path):
    if (filename.split('--'))[0] == 'Gerald-Wogan' and (filename.split('.'))[-1] == 'pdf':
        get_files.append(filename)
print(len(get_files))

dq_dir = downloads_path + "\DQ"
if not os.path.exists(dq_dir):
    os.makedirs(dq_dir)

for g in get_files:
    os.replace(downloads_path + '\\' + g, dq_dir + '\\' + g) 
