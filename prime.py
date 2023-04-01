def primefac(a):
    d={}
    c=2
    l=[]
    for i in a:
        c=2
        p=i
        while(i>1):
            if(i%c==0):
                l.append(c)
                i=i/c
            else:
                c=c+1
        d[p]=list(set(l))
        l=[]
    print(d)


    


a=eval(input("enter the list of integers"))
primefac(a)