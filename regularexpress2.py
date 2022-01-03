'''
Chapter 11
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
'''
a = []
fi = input('Enter the filename:\n>>>')
try:
    fo = open(fi)
except:
    print('Invalid Filename. Quitting.')

import re
for line in fo:
    num = re.findall('^New Revision: ([0-9]+)', line)   # starting from New Revision: and a space then extracting only digits at least one
    if len(num) == 0: continue
    else:
        for i in num:
            a.append(int(i))

print('Average of all the required numbers is:',int(sum(a)/len(a)))
