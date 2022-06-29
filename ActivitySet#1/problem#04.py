# Conditional Execution

h = float(input("Enter hours: "))
r = float(input("Enter the rate: "))
if h>40:
  print((40*r)+((h-40)*(r*1.5)))
else:
  print(h*r)
