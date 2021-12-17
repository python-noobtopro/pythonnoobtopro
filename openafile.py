filename = input('Enter the filename: ')

count = 0
sum = 0

if filename =='na na boo boo':
    print("NA NA BOO BOO TO YOU - You've been punk'd!")
    quit()

try:
    fhand = open(filename)
except:
    print('Filename entered is Invalid:', filename)
    quit()

for line in fhand:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    line = line.rstrip()
    count = count + 1
    pos = line.find('0')
    sum = sum + float(line[pos:pos+6])

#print(sum)
#print(count)
print('Average spam confidence: ',  sum/count)








    #print(fline)



    #print(line[pos+1:])  working
    #print(line)
