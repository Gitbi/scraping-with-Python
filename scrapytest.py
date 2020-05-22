from bs4 import BeautifulSoup
import urllib


def getTitle(url):
    try:
        html = urllib.urlopen(url)
    except() as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title_list = bsObj.find_all("a")
    except AttributeError as e:
        return None
    return title_list

title = getTitle("http://www.ecnu.edu.cn")
if title == None:
    print "Title is not found"
else:
    for child in title:
        print child
