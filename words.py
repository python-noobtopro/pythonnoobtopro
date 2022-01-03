"""
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""

count = 0
a = dict()
#y = list()    #long cut
fopen = open('words.txt')

for line in fopen:
    words = line.split()
    for i in words:
        count += 1
        a[i] = count

#print(a) #just to check

inp = input('Please enter the word to search:\n>>')

#for x in a:        #long cut
    #y.append(x)        #long cut
if inp in a:
    print('Found:',inp)
else:
    print('Err...Not Found:',inp)
