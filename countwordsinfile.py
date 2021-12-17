# Count the number of any word in a filename
import string      # to use string.punctuation

a = list()          # initiate values
b = dict()

fi = input('Enter the filename:\n>>')

try:
    fh = open(fi)
except:
    print('Invalid Filename')
    quit()

print('\nFile opened successfully...\n')

for line in fh:
        line = line.translate(str.maketrans('','',string.punctuation))  # to make every word lineraly same by removing punctuation
        line = line.lower()
        words = line.split()

        for i in words:
            b[i] = b.get(i,0)+1         # important, setting counter through dictionary

for k,v in list(b.items()):             # reversing the key value pair so that we can sort by value(number of occurrences)
    a.append((v,k))

a.sort(reverse=True)                    # sorting in descending order
for k,v in a[:5]:
    print(v,k)                          # again reversing to print in desired order
