class item:
    def calculate(self,x,y):
        return x*y
item1=item()
item1.price=400
item1.quantity=4
print(item1.calculate(item1.price,item1.quantity))
