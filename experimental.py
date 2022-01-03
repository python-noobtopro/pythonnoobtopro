filename = input('Enter the filename: ')

count = 0
#sum = 0

#if filename =='na na boo boo':
    #print("NA NA BOO BOO TO YOU - You've been punk'd!")
    #quit()

try:
    fhand = open(filename)
except:
    print('Filename entered is Invalid:', filename)
    quit()
a = list()
b = list()
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        line = line.rstrip()
        x = line.split(' ')

        #count = count + 1
        #print(x[1])
        a.append(x[1])

for i in a:
    if i not in b:
        b.append(i)
        count = count +1


for j in b:
    print(j)

#print(a)










#print('There were', count, 'lines in the file with From as the first word' )
print('There were', count, 'non repeatable lines in the file with From as the first word' )
