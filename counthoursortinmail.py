'''
Chapter-10
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
'''

hrscount = dict()
hrslisttup = []

fi = input('Enter the filename:\n>>')
try:
    fh = open(fi)
except:
    print('The filename entered is Invalid. Quitting.')
    quit()

for line in fh:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        a = words[5].split(':')    # this is important (shortcut) rather than using other list, see list is autocreated
        hrscount[a[0]] = hrscount.get(a[0], 0) + 1  # dict can be counted like this also

for k,v in list(hrscount.items()):
    hrslisttup.append((k,v))

hrslisttup.sort()   # for sorting you have to make a new list of tuples from the existing dictionary 

for k,v in hrslisttup:
    print(k,v)
