a=input("Enter the string")
b=input("Enter the string to search")
c=0

a=a.split(" ")
for i in a:
    if i==b:
        c=c+1
print("The frquency of ",b,"is",c)

