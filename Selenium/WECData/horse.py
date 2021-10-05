"""
CS3435 Data Collection & Visualization
@SydneyMagee
World Equestrian Center Scraper

This program gathers data from WEC
Output: JSON file with data
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import json
import re


driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = 'https://wec.orgpro-rsmh.net/horses.php'
driver.get(url)

lst = []
horses = driver.find_elements_by_css_selector('a[href^="horse.php?number="]')
for h in horses:
    href = h.get_attribute('href')
    if href is not None:
        lst.append(href)

final_lst = []
for link in lst:
    driver.get(link)
    try:
        dictionary = {}
        dictionary['horse_name'] = driver.find_element_by_tag_name('h4').text
        dictionary['section'] = driver.find_element_by_css_selector('a[href^="section.php?"]').text
        dictionary['show_class'] = driver.find_element_by_css_selector('a[href^="class.php?"]').text
        dictionary['show'] = driver.find_element_by_css_selector('a[href^="show.php?"]').text
        dictionary['rider'] = driver.find_element_by_xpath('/html/body/section/div/table/tbody/tr/td[4]').text
        dictionary['place'] = driver.find_element_by_xpath('/html/body/section/div/table/tbody/tr/td[5]').text
        dictionary['entries'] = driver.find_element_by_xpath('/html/body/section/div/table/tbody/tr/td[6]').text
        dictionary['points'] = driver.find_element_by_xpath('/html/body/section/div/table/tbody/tr/td[7]').text
        final_lst.append(dictionary)
    except NoSuchElementException:
        pass

with open('results.json', 'a') as fp:
    json.dump(final_lst, fp)


driver.close()


