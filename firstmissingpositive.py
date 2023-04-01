def firstMissing(arr, n):
    # Write your function here.
    l=list(arr.sort())
    for i in range(l[0],l[n-1]+1,1):
        if i not in l and i>0:
            return i
    pass



    

# Main Code
    arr=[-1,1,3,4]
    n=5
    ans = firstMissing(arr,n)

    print(ans)
