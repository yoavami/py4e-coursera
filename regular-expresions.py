import re

fname = input("Enter the file name: ")

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened", fname)
    quit()

sum = 0

for line in fhand:
    num = re.findall('[0-9]+', line)
    if len(num) >= 1:
        for i in range(len(num)):
            sum = sum + int(num[i])
    else:
        continue

print(sum)