from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Function to extract data using Selenium
def scrape_with_selenium(url):

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    driver.get(url)

    title = driver.title
    movie_title = driver.find_elements(By.XPATH, '//h3[@class="ipc-title__text"]')
    for i in movie_title:
        print("i in movie title", i.text)

    driver.quit()

    return title

url_to_scrape = 'https://www.imdb.com/chart/top/'

# Scrape data using Selenium
title_selenium = scrape_with_selenium(url_to_scrape)

print("\nTitle (Selenium):", title_selenium)
