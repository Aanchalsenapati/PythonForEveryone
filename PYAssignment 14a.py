import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
print('Retrieving', url)
js = urllib.request.urlopen(url).read()
print('Retrieved', str(len(js)), 'characters')

info = json.loads(js)
info = info["comments"]
print ('count:', len(info))

sum = 0
for item in info:
		sum += int(item["count"])
print("sum: ", str(sum))
