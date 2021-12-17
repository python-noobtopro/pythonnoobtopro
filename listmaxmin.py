a = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        x = int(inp)
    except:
        print('Please enter a valid integer value')
        continue
    a.append(x)
#print(a)
print('Maximum:',max(a))
print('Minimum:',min(a))
