# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import re
import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input("Enter position: ")

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
links = list()

# Prints the first link
print('Retrieving:', url)

for i in range(int(count)):

    if i == 0:
        html = urllib.request.urlopen(url, context=ctx).read()
    else:
        html = urllib.request.urlopen(newurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links.clear()

    for tag in tags:
        if len(links) == (int(position)):
            print("Retrieving:", links[(int(position)-1)])
            links.append(tag.get('href', None))
            newurl = links[(int(position) - 1)]
            break
        else:
            links.append(tag.get('href', None))
