import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "christmas@pythonscraping.com"
    msg['to'] = "ftian@pythonscraping.com"

    s= smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urllib.urlopen("https://isitchristmas.com/"))
while bsObj.find('a', {"id":"answer"}).attrs['title']=='NO':
    print "It is not christmas yet."
    time.sleep(3600)
bsObj = BeautifulSoup(urllib.urlopen("https://isitchristmas.com/"))
sendMail("It is Christmas!", "According to https://isitchristmas.com, it is christmas!")