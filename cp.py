t=int(input())
for i in range(t):
    N=int(input())
    s=input()
    mini=1000
    for i in range(N):
        if(s[i]=='1'):
            for j in range(i+1,N,1):
                if(s[j]=='1'):
                    k=j-i
                    if(k<=mini):
                        mini=k
    print(mini)
    