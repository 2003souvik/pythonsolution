a=input("Enter the sentence")
z=a.split(" ")
c=0
d={}
for i in z:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
          c=c+1
    d[i]=c
for x,y in d.items():
    print(x," ",y)

