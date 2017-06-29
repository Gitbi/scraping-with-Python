import urllib
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='111111', charset='utf8', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

def getLinks(articleURL):
    html = urllib.urlopen("http://en.wikipedia.org"+articleURL)
    bsObj = BeautifulSoup(html, 'lxml')
    title = bsObj.find('h1').get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print newArticle
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()