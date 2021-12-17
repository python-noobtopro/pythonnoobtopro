filename = input('Enter the filename: ')
fhand = open(filename)
fread = fhand.read()
x = fread.split()
y = []
for i in x:
    if i not in y:
        y.append(i)
        y.sort()
print(y)
