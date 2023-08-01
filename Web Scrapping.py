import requests
from bs4 import BeautifulSoup
import csv


def scrape(soup1):
    try:
        v0 = soup1.find('h1').getText().strip()
        print(soup1.find('h1').getText().strip())
        var = soup1.find_all('span', class_='btn')
        para = soup1.find_all('p', class_='py-2')
        price = soup1.find_all('span', class_='badge')
        tag = soup1.find_all('p', class_='my-2')
        use = soup1.find_all('div', class_='my-4')
        var1 = var[0].find('a')
        var2 = var1.get("href")
        li1 = use[0].find('ol')
        li2 = li1.find_all("li")
        v1 = var2
        print(var2)
        v2 = para[0].get_text().strip()
        print(para[0].get_text().strip())
        v3 = price[0].get_text().strip()
        print(price[0].get_text().strip())
        badge = []
        for i in tag:
            new = i.find_all('span', class_='badge')
            for j in new:
                badge.append(j.get_text().strip())
        v4 = badge
        print(badge)
        msg = []
        for j in li2:
            msg.append(j.get_text())
        v5 = msg
        print(msg)
        csv_file_path1 = "Final_Result.csv"
        with open(csv_file_path1, 'a', newline='') as csvfile1:
            csv_reader1 = csv.writer(csvfile1)
            csv_reader1.writerow([v0, v1, v2, v3, v4, v5])
    except Exception as e:
        csv_file_path1 = "Final_Result.csv"
        with open(csv_file_path1, 'a', newline='') as csvfile1:
            csv_reader1 = csv.writer(csvfile1)
            csv_reader1.writerow(["Null", "Null", "Null", "Null", "Null", "Null"])


csv_file_path = 'Result_Link1.csv'

path = []
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader, None)
    if header:
        print(f"Header: {header}")
    for row in csv_reader:
        path.append(row[0])

for k in path:
    url = 'https://topai.tools' + k
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
    else:
        print(f"Failed to fetch the web page. Status code: {response.status_code}")
        exit()
    scrape(soup)