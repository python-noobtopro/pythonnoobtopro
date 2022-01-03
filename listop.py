#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements

t = list()
n = 0
while (True):
    n = n + 1
    if n == 1:
        inp = input('Enter the data to be entered in list. Type done when completed:\n>>')
    else:
        inp = input('Enter the data to be entered in list:\n>>')
    if inp == '':
        print('Input cannot be blank')
    if inp == 'done': break
#t = ['a',1,2,'c']
    if inp != '':
        t.append(inp)

def chop(t):
    def del_first():
        del t[0]
    def del_last():
        del t[-1]
    del_first()
    del_last()
    #print(t) #Not needed

p = chop(t)
#print(p) # To check that None is returned
print('Printing the final list after removing first and last entry...')
print(t)
