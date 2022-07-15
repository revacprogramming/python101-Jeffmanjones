class Menu:
  #fill in class definition here
  def __init__(self,item,price):
    self.item=item
    self.price=price
  def add(self,item,price):
    
  def show(self,item,price):
    for i in item,price:
      print(item,price)
      
m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada". 20)
m.show()