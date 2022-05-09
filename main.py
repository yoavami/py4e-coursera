fname = input("Enter the file name: ")
fname = fname + ".txt"

try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened", fname)
    quit()

counts = dict()

for line in fhand:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        words = line.split()
        hours = words[5].split(':')
        time = hours[0]
        counts[time] = counts.get(time, 0) + 1

lst = list()

for k, v in counts.items():
    lst.append( (k, v) )

lst.sort()

for k, v in lst:
    print(k, v)















