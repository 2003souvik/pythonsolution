a=input("Enter the string")

maxx=0
c=0
z=""
for i in a:
    c=0
    for j in a:
        if i==j:
            c=c+1
    if(c>=maxx):
        maxx=c
        z=i
print("The maximum string is ",z)

