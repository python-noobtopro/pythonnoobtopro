# Using line.translate(str.maketrans(fromstr, tostr, deletestr))

import string       # to use string.punctuation

a = dict()

fh = open('romeopunc.txt')
for line in fh:
    line = line.translate(str.maketrans('','',string.punctuation)) #Important line
    line = line.lower()
    words = line.split()
    for word in words:
        a[word] = a.get(word, 0) + 1
        '''if word not in a:        # Instead of this use get()
            a[word] = 1
        else:
            a[word] += 1'''

# print(a)      #simply used to see count of each word
for i in a:     # more sophisticated count
    if a[i] > 1:
        print(i, a[i])
