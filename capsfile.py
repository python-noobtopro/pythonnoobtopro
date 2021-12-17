fname = input('Enter the filename:\n')
fhand = open(fname)
for line in fhand:
    a = line.upper()
    print(a)
