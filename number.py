 #"Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number"

count = 0
sum = 0

while True:
    inp = input('Enter a number:')
    if 'done' == inp :
        break
    try:
        s = float(inp)

    except:
        print('Anything except number is not accepted. Please try again')
        continue


    print(s)
    count = count + 1
    sum = sum + s
    print(count)

print('Total Number Entered:', count)
print('Sum of all the Numbers Entered:', sum)
print('Average of all the Numbers Entered:', sum/count)
