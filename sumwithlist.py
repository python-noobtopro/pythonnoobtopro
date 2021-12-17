a = list()
print('Enter done when done with giving numbers')
while (True):
    x = input('Enter a number:\n>>')
    if x == 'done': break
    try:
        fx = float(x)
    except:
        print('Errrr...Please enter only digits')
        continue
    a.append(fx)
print('Sum of all numbers:\n>>',sum(a))
print('Average of all numbers:\n>>',sum(a)/len(a))
