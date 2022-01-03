'''
Chapter-9
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
'''

fi = input('Enter the filename:\n>>')
fh = open(fi)

a = dict()
b = list()

for line in fh:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    else:
        # print(words[1])   # check to capture email
        atpos = line.find('@')  #can also be words[1].find('@')
        spos = line.find(' ', atpos)    #find position of first space after @  #can also be words[1].find(atpos+1:)
        domain = line[atpos+1:spos]
        b.append(domain)
    #print(domain)

for i in b:
    a[i] = a.get(i,0) + 1

print(a)
