#Following Links in HTML Using BeautifulSoup
#In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1

for i in range(count):
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  url = tags[position].get('href',None)
  print (url)

