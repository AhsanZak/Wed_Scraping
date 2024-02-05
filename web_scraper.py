import schedule
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import dbconnect as db

# Function to extract data using Requests and Beautiful Soup
def scrape_with_requests(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data (modify as needed)
    title = soup.title.text
    paragraphs = soup.find_all('p')

    return title, paragraphs

def scrape_tech():
    url = 'https://www.imdb.com/chart/top/'
    
    print(scrape_with_requests(url))

    imdb_movie_list = main_scraping_process(url)
    res = db.insert_movies_rows(imdb_movie_list)
    return "success"


# Function to extract data using Selenium
def main_scraping_process(url):
    # This function get the movie data from the imdb site.

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    driver.get(url)

    movie_elements = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
    
    empty_list = {}

    for movie_element in movie_elements:
        movie_name = movie_element.find_element(By.CLASS_NAME, 'ipc-title__text').text.split('.')[1].strip()
        release_date = movie_element.find_elements(By.CLASS_NAME, 'sc-be6f1408-8')[0].text
        empty_list[movie_name] = release_date

    driver.quit()
    return empty_list

# Schedule the scraping task every day at a specified time
schedule.every().day.at("12:00").do(scrape_tech)
# Run the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

