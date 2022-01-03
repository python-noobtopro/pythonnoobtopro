filename = input('Enter the filename: ')

count = 0

try:
    fhand = open(filename)
except:
    print('Filename entered is Invalid:', filename)
    quit()
a = list()
b = list()
for line in fhand:
    words = line.split()
    if len(words)<3 or words[0] != 'From': continue
    else:
        a.append(words[1])
    #count = count + 1  #updates even with repeated values

for i in a:
    if i not in b:
        count = count + 1
        b.append(i)
for j in b:
    print(j)

print('There were', count, 'non repeatable lines in the file with From as the first word' )
