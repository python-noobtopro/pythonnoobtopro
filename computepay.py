def computepay(h, r):
    if h > 40 :
        return ((h-40)*1.5*r+(40*r))
    else :
        return (h*r)

hrs = input("Enter Hours:")
h = float (hrs)
rate = input("Enter Rate:")
r = float (rate)

p = computepay(h, r)
print("Pay", p)
