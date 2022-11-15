import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
t = 0
s = 0

print('Retrieving', url)
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    s += int(count.text)
    t += 1

print('Retrieved', len(xml), 'characters')
print('Count:', t)
print('Sum:', s)