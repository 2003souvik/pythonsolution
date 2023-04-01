class Item:
    payrate=0.8
    all=[]
    def __init__(self,name:str,price:int,quantity:int) :
        #asserting 
        assert price>=0,f"price {price} is not greater than zero"
        assert quantity>=0,f"quantity {quantity} is not greater than zero"


        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def calculated(self):
        self.price= self.price * self.quantity
    def paydis(self):
        self.price=self.price*self.payrate  
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
for i in item1.all:
    print(i.price)
