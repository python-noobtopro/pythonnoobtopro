'''
Chapter 10
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
'''

fi = input('Enter the filename:\n>>')
fh = open(fi)

a = dict()
b = list()
c = list()

for line in fh:
    words = line.split()
    if len(words)<2 or words[0] != 'From': continue
    else:
        # print(words[1])   # check to capture email
        b.append(words[1])

for mail in b:
    a[mail] = a.get(mail, 0) + 1

for k,v in list(a.items()):
    c.append((v,k))

c.sort(reverse=True)
print('\nPrinting in descending order...')
print('\n',c,'\n')

for k,v in c[:1]:
    print('Printing the maximum occurrence\n')
    print(v,k)
