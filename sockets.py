import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_1550906.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve numbers and sum them
count = 0
sum = 0
tags = soup('tr')
for tag in tags:
    num = re.findall('>([0-9]+)<', tag.decode())
    if len(num) >= 1:
        for i in range(len(num)):
            sum = sum + int(num[i])
            count += 1
    else:
        continue

print("Count", count)
print("Sum", sum)

