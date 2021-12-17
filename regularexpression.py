'''
Chapter-11
Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression
'''
fo = open('mbox.txt')
inp = input('Enter a regular expression:\n>>')

import re
a = dict()
for line in fo:
    x = re.findall(inp, line)
    if len(x) == 0: continue
    else:
        for i in x:
            a[i] = a.get(i, 0)+1

for key in a:      # looping and dictionary chapter 9
    print('mbox.txt had',a[key],'lines that matched',inp)
