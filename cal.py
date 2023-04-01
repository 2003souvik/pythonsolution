def calu(x):
    if(x<=10):
        print(3*x**2+5)
    elif(x>10 and x<=20):
        print(5*x)
    else:
        print(2*x**2-x+9)
x=int(input("Enter the value of x"))
calu(x)
