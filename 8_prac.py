def prime(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=[20,25,30]
d={}
l=[]
p=0
s=1
for i in n:
    
    p=0
    s=1
    for j in range(1,i):
        
        if(i%j==0):
            if(prime(j)):
                p=p+1
                s=s*j
        if(p==3 and s==i):
            l.append(i)
            break
print(l)




