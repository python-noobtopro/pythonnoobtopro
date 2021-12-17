#Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.

inp = input('Enter a word:')
if inp == 'exit':
    quit()
sinp = str(inp)
a = len(sinp)
n = 1
print('Printing backwards...')
while n <= a:
    print(sinp[-(n)])
    n = n +1


#print(sinp[(a-2)-a])
#print(sinp[(a-3)-a])
