import json
import urllib.request, urllib.parse, urllib.error
from links import ctx

address = input('Enter location: ')

while True:
    if len(address) < 1: break

    print('Retrieving', address)

    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)

    print('Count:', len(info))

    sum = 0

    for item in info:
        sum += item['count']

    print('Sum:', sum)


