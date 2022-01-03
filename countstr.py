# Making count as a function for counting string length
def count(s):
    count = 0
    for letter in s:
            count = count + 1
    print('Counting letters(including whitespaces)...\n>>>\n>>>')
    print('Result:',count)

count(input('Enter the word:\n>>'))
