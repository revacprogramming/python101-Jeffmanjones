d=dict()
class Menu:
  #fill in class definition here
  def __init__(self,item,price):
    self.item=item
    self.price=price
    
  def add(self,item,price):
    d[self.item]=self.price
  def show(self):
    print(d)

n=int(input("Number of items in the menu:\n"))
i=0
while i<n:
  item=input("Enter an item: ")
  price=float(input("Enter the price: "))
  m=Menu(item,price)
  m.add(item,price)
  i=i+1
m.show()

#m.add("idly", 10) 
#m.add("vada", 20)