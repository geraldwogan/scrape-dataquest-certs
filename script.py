# Scraping certificates from DataQuest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

## Navigate to Dataquest. 

# Selenium Web Driver specifically for chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# Link to dataquest
link = "https://app.dataquest.io/profile/gerald.wogan"
# Open webpage
driver.get(link)

# Sign-In
# Navigate to Certificates page: https://app.dataquest.io/profile/gerald.wogan
# Scrape list of links to certs


# For each cert
    # Open link
    # Click Download