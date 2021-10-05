"""
CS3435 Data Collection & Visualization
@Sydney Magee
Final Project webscraper

This program gathers data from StartboxScoring.
Output: JSON file with data
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import json
import csv

driver = webdriver.Firefox()

url = 'https://eventing.startboxscoring.com/archives.php?Year=2019' 
driver.get(url)

time.sleep(5)

lst = []
shows = driver.find_elements_by_css_selector('a[href^="http://eventingscores.com/eventsu/"]')
for show in shows[:10]:
    href = show.get_attribute('href')
    if href is not None:
        lst.append(href)
        #print(href)

lst2 = []
for link in lst:
    driver.get(link)
    final_scores = driver.find_elements_by_xpath('//a[contains(@href, "division=")]')
    for result in final_scores:
        href2 = result.get_attribute('href')
        if href2 is not None:
            lst2.append(href2)
            print(lst2) 

#print the page
final_lst = []
for page in lst2:
    driver.get(page)
    dictionary = {}
    try:
        dictionary['division_title'] = driver.find_element_by_css_selector('td[class="division"] h1').text
        #print(division_title.text)
    except NoSuchElementException:
        pass
    
    try:    
        dictionary['division_num'] = driver.find_element_by_css_selector('tr[class="drawdata1"] td').text
        #print(division_num.text)
    except NoSuchElementException:
                pass
    try:
        dictionary['rider'] = driver.find_element_by_css_selector('.drawdata1 > td:nth-child(2)').text
        #print(rider.text)
    except NoSuchElementException:
                pass
    
    try:
        dictionary['horse'] = driver.find_element_by_css_selector('.drawdata1 > td:nth-child(3)').text
        #print(horse.text)
    except NoSuchElementException:
                pass

    try:
        dictionary['score'] = driver.find_element_by_class_name('center').text
        #print(score.text)
    except NoSuchElementException:
                pass

    try:
        dictionary['place'] = driver.find_element_by_css_selector('td[class="center place"]').text
        #print(place.text)
    except NoSuchElementException:
        pass
    final_lst.append(dictionary)

with open('results.json', 'a') as fp:
    json.dump(final_lst, fp)

driver.close()


