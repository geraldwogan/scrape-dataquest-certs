# Scraping certificates from DataQuest 
import profile
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
links = driver.find_elements_by_tag_name("a")
# traverse list
for elem in links:
    # get_attribute() to get all hrefs
    href = elem.get_attribute('href')
    if 'view_cert' in str(href):
        cert_links.append(href)
print(len(cert_links), 'certificate links found')

## For each cert
    ## Open link
    ## Click Download
