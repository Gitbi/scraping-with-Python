# -*-coding: utf-8-*-
import csv
from bs4 import BeautifulSoup
import urllib


html = urllib.urlopen("https://cloud.tencent.com/act/tcc2017/agenda")
bsObj = BeautifulSoup(html, 'lxml')
table = bsObj.findAll("table", {"class": "agenda-list"})[0]
rows = table.findAll("tr")

csvFile = open("./agender.csv", "w+")
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll("td"):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
