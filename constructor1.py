class item:
    def __init__(self,name,price,quantity) :
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculated(self):
        return self.price * self.quantity
        
item1=item("car",5000,3)
item2=item("Laptop",30000,4)
print(item1.calculated())
z=item2.calculated()
print(z)

