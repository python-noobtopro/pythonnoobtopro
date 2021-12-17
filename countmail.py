'''
Chapter-9
Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
'''

fi = input('Enter the filename:\n>>')
fh = open(fi)

a = dict()
b = list()

for line in fh:
    words = line.split()
    if len(words)<2 or words[0] != 'From': continue
    else:
        # print(words[1])   # check to capture email
        b.append(words[1])

for mail in b:
    a[mail] = a.get(mail, 0) + 1

print(a)
