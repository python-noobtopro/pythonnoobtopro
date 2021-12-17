largest = None
smallest = None
while True:
    tnum = input("Enter a number: ")
    if tnum == "done":
        break
    try:
        num = int(tnum)
    except:
        print('Invalid Input')
        continue
    #print(num)
    if largest is None :
        largest = num
    elif largest < num :
        largest = num
    if smallest is None :
        smallest = num
    elif smallest > num :
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)
