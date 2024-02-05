import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

count = 1

# Function to extract data using Selenium
def scrape_with_selenium():
    
    url = 'https://www.imdb.com/chart/top/'

    global count
    count += 1
    
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    driver.get(url)

    movie_elements = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')

    empty_list = []

    for movie_element in movie_elements:
        movie_name = movie_element.find_element(By.CLASS_NAME, 'ipc-title__text').text.split('.')[1].strip()
        release_date = movie_element.find_elements(By.CLASS_NAME, 'sc-be6f1408-8')[0].text
        empty_list.append({"movie": movie_name, "release": release_date})

    driver.quit()
    print("Count now : ", count)
    return empty_list


# Scrape data using Selenium
# movie_list = scrape_with_selenium(url_to_scrape)

schedule.every(1).minutes.do(scrape_with_selenium)
# Run the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
