'''
Chapter 10
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies
'''
import string       #THIS WAS FUN
countletter = dict()
lstsort = []
toplist = []

fi = input('Enter the filename:\n>>')
num = list(range(0,10))  #activated this here to use it later to remove all integer digits from file

try:
    fo = open(fi)
except:
    print('\nFilename is Invalid. Quitting.')

for line in fo:
    for i in num:
        line = line.translate(str.maketrans('','',str(i)))    # important I made this to remove all numbers from the text file. Bingo Rupesh.
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    word = line.split()      # to remove spaces and tabs in between lines, first split then join
    line = ''.join(word)    # joining without space creates stream of letters
    line = line.strip()
    letterlist = [i for i in line]  # this is used to create a list of all alphabets
    for letter in letterlist:
        countletter[letter] = countletter.get(letter, 0) + 1  # counting each letter
print('\nOpening File and reading through letters...\n')
print('Frequency Distribution of each letter are as follows:')
allfrequency = list(countletter.values())        # only taking values of all occurrence to get a sum total of occurrences
for k in countletter:
    freqperc = round(((countletter[k]/sum(allfrequency))*100), 2)       # rounding off the result to 2 decimal place

    lstsort.append((k,freqperc))
    lstsort.sort()              # sorting occurrence alphabetically

for k,v in lstsort:
    print(k,v,'%')

print('\nTop five occurrences of Alphabets are:')
for k,v in lstsort:
    toplist.append((v,k))
toplist.sort(reverse=True)

for k,v in toplist[:5]:
    print(v,k,'%')
