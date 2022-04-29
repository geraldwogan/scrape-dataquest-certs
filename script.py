# Scraping certificates from DataQuest 
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## Navigate to Dataquest. 

# Selenium Web Driver specifically for chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# Link to dataquest
link_to_profile = "https://app.dataquest.io/profile/gerald.wogan"
# Open webpage
driver.get(link_to_profile)

## Scrape list of links to certs
cert_links = []
# identify elements with tagname <a>
anchors = driver.find_elements(by=By.TAG_NAME, value='a') 

# traverse list
for elem in anchors:
    # get_attribute() to get all hrefs
    href = elem.get_attribute('href')
    if 'view_cert' in str(href): 
        cert_links.append(href)
certs_found = len(cert_links)
print(certs_found, 'certificate links found')

# For each cert
# for link in cert_links:
#     ## Open link
#     driver.get(link)
driver.get(cert_links[0])
    # Click Download
b = driver.find_elements(by=By.TAG_NAME, value='button') 
dl = b[-1]
dl.click()
time.sleep(3)

# Find downloaded certs
downloads_path = str(Path.home() / "Downloads")
get_files = []
for filename in os.listdir(downloads_path):
    if (filename.split('--'))[0] == 'Gerald-Wogan' and (filename.split('.'))[-1] == 'pdf':
        get_files.append(filename)
# print(len(get_files))

# Create directory to store certs together
dq_dir = downloads_path + "\DQ"
if not os.path.exists(dq_dir):
    os.makedirs(dq_dir)
    print('Creating directory:', dq_dir)
else:
    print('Directory already exists:', dq_dir)

# Move certs to directory
for g in get_files:
    os.replace(downloads_path + '\\' + g, dq_dir + '\\' + g) 

# Check the correct number of certs have been downloaded
if certs_found == len(os.listdir(dq_dir)):
    print(f'All {certs_found} have been downloaded and saved in the {dq_dir} directory!')