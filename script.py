# Scraping certificates from DataQuest 
from selenium import webdriver

## Navigate to Dataquest. 

# Selenium Web Driver specifically for chrome, download from here: https://chromedriver.chromium.org/downloads
driver =  webdriver.Chrome('chromedriver.exe')


# Sign-In
# Navigate to Certificates page: https://app.dataquest.io/profile/gerald.wogan
# Scrape list of links to certs

# For each cert
    # Open link
    # Click Download