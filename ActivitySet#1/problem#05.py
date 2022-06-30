# Functions
def computepay(h,r):
    if h>40:
        pay1=40*r
        r=r*1.5
        h1=h-40
        pay2=r*h1
        pay=pay1+pay2
    return pay
hrs = input("Enter Hours:")
hs=float(hrs)
rate= input("Enter rate:")
rt=float(rate)
p = computepay(hs,rt)
print(p)
