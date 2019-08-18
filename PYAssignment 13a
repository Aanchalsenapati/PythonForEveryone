#Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to https://py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum,



import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Retrieve URL and Parse
url = input('Enter URL:')
print('Retrieving', url)
xml = urllib.request.urlopen(url).read()
print('Retrieved', str(len(xml)), 'characters')

#Count the lines and total
tree = ET.fromstring(xml)
counts =  tree.findall('.//count')
print ('Count:', str(len(counts)))

#Result
sum = 0
for count in counts:
    sum += int(count.text)
print ('Sum:', str(sum))
