a=list(map(input().split()))
b=list(set((a)))
if(len(a)==len(b)):
    print("yes")
else:
    print("no")