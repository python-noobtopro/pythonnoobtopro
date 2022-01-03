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

for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        line = line.rstrip()
        x = line.split(' ')
        print(x[1])
        count = count + 1









print('There were', count, 'lines in the file with From as the first word' )
