def patt(n):
    for i in range(n):
        for k in range(i):
            print(" ",end="")
        for j in range(6-i):
            print("*",end="")
        print()
x=int(input("Enter the value of n"))
patt(x)

