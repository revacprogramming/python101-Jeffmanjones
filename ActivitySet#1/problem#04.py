# Conditional Execution

hrs = input("Enter hours: ")
h=float(hrs)
rate = input("Enter the rate: ")
r=float(rate)
if h>40:
  pay1=40*r
  r=r*1.5
  h1=h-40
  pay2=r*h1
  pay=pay1+pay2
else:
  pay=h*r

print("pay: ",pay)