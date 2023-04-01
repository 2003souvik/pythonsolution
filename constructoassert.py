class item:
    payrate=0.8
    def __init__(self,name:str,price:int,quantity:int) :
        #asserting 
        assert price>=0,f"price {price} is not greater than zero"
        assert quantity>=0,f"quantity {quantity} is not greater than zero"


        self.name=name
        self.price=price
        self.quantity=quantity
    def calculated(self):
        return self.price * self.quantity
        
item1=item("phone",5000,2)
item2=item("Laptop",30000,3)
print(item1.calculated())
z=item2.calculated()
print(z)
print(item.__dict__)
print(item1.__dict__)

