'''
Chapter-9
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has
'''




fi = input('Enter the filename:\n>>')

try:
    fh = open(fi)
except:
    print('No such file exists in the directory. Thank You.')
    quit()

a = dict()
b = list()

for line in fh:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    else:
        # print(words[1])   # check to capture email
        b.append(words[1])

for mail in b:
    a[mail] = a.get(mail, 0) + 1

# print(a)

mostsender = None
mostmail = None
for k,v in a.items():
    if mostmail is None or v > mostmail:
        mostmail = v
        mostsender = k

print(mostsender, mostmail)
