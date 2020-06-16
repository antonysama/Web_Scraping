import requests
from bs4 import BeautifulSoup
import lxml
import csv

url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?start=&typ=newsreleases&end=&idx={}&dprtmnt=fisheriesoceans"
i=1
with open(r'C:\Users\antony.samarawickrem\projects\dfo\canada.csv', 'w',newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for x in range(0,671,10):
        response = requests.get(url.format(x))
        soup = BeautifulSoup(response.content, 'lxml')
        soup = soup.find("div", class_="mwsharvest section")
        data = soup.find_all('a')
        if x < 670:
            for link in data[:10]:
                writer.writerow([link.get("href"),link.text])
        else:
            for link in data[:1]:
                writer.writerow([link.get("href"),link.text])