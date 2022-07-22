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

m=Menu("item",20)
m.add("item",20)
m=Menu("idli",10)
m.add("idli",10)
m.show()