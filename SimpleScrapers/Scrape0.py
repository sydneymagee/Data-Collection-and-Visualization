"""
First look into Project website
2/8/21

Edited to work in new environment 10/15/21

Struggled to find a website but landed on WEC's site.
https://worldequestriancenter.com/

This script ethically scrapes the website listed above for all links.
"""

from bs4 import BeautifulSoup
import requests
import urllib.robotparser
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Check robots file
bot = 'https://worldequestriancenter.com/robots.txt'
rp = urllib.robotparser.RobotFileParser()
rp.set_url(bot)
rp.read()

url1 = 'https://worldequestriancenter.com/ocala-fl/equestrian-events/members-and-exhibitors/results/'
url2 = 'https://worldequestriancenter.com/wilmington-oh/equestrian-events/members-and-exhibitors/results/'
print('First step, check the robots file')
print(rp.can_fetch("*", url1))
print(rp.can_fetch("*", url2))  
print('If above values are True, the robots file allows scraping')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}

r1 = requests.get(url1, headers=headers)
r2 = requests.get(url2, headers=headers)

html1 = r1.text
html2 = r2.text

bs1 = BeautifulSoup(html1, 'html.parser')
bs2 = BeautifulSoup(html2, 'html.parser')

print('LINK1')
for link in bs1.find_all('a'):
   if 'href' in link.attrs:
        print(link.attrs['href'])
print("-------------------------------------------------------------------------------")
print('LINK2')
for link in bs2.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

