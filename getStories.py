import urllib.request
import xml.etree.ElementTree as ET
import sys

get contents from website
r = urllib.request.urlopen('http://www.cbc.ca/cmlink/rss-topstories')
tree = ET.parse(r)

#get titles
root = tree.getroot()
for child in root:
    for item in child.findall('item'):
        titles = item.find('title').text
        sys.stdout.write(titles)
        #print(titles)
