# Conditional Execution

h = float(input("Enter hours: "))
r = float(input("Enter the rate: "))
if h>40:
  r1=r*1.5
  h1=h-40
  print()
else:
  print(h*r)