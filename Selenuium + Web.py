from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from bs4 import BeautifulSoup
import keyboard
overall = []
driver = webdriver.Chrome()
url = 'https://topai.tools/browse'
driver.get(url)
time.sleep(5)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    current_scroll_position = driver.execute_script("return window.pageYOffset;")
    total_page_height = driver.execute_script("return document.body.scrollHeight;")
    if keyboard.is_pressed('q'):
        break

# SOUP
soup = BeautifulSoup(driver.page_source, 'html.parser')
all_links = soup.find_all('div', class_='tool-image')
for i in all_links:
    var = i.find('a', target='_blank')
    var1 = var.get('href')
    if var1 != '#':
        overall.append(var1)
csv_file_path = 'Result_Link1.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for value in overall:
        csv_writer.writerow([value])
driver.quit()