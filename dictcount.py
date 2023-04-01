def vowel(str):
    l=str.split()
    c=0
    d={}
    for i in l:
        c=0
        for j in i:
            if j in "aeiouAEIOU":
                c=c+1
        d[i]=c  
    for a,b in d.items():
        print(a,":",b)
x=input("Enter the words")
vowel(x)
