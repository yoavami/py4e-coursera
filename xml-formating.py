import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for a URL to use as XML source data
url = input("Enter location: ")

# Read the XML data
fhand = urllib.request.urlopen(url, context=ctx)
data = fhand.read()

# Print confirmation that webpage is being retrieved including the amount of characters in the page
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

# Forming a data tree from the webpage contents
tree = ET.fromstring(data)

# Create a list of all commentinfo/comments/comment
lst = tree.findall('.//comment')

# Create sum variable to sum up all the numbers and count to give the amount of characters
sum = 0
count = 0

# Extract /comments/comment/count from XML file
for item in lst:
    sum = sum + int(item.find('count').text)
    count += 1

# Print the sum of all the numbers in the file and amount of numbers
print('Count:', count)
print('Sum:', sum)
