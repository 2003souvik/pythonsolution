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
        self.price= self.price * self.quantity
    def paydis(self):
        self.price=self.price*self.payrate  
item1=item("phone",5000,2)
item2=item("Laptop",30000,3)
item1.calculated()
print(item1.price)
item1.paydis()
print(item1.price)
item2.payrate=0.7
item2.paydis()
print(item2.price)
