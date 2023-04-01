def firstAndLastPosition(arr, n, k):

    # Write your code here
    p=-1
    s=-1
    for i in range(n):
        if(arr[i]==k):
            p=i
            break
    for i in range(n-1,-1,-1):
        if(arr[i]==k):
            s=i
            break
    return p,s
	
	
arr=[7,1,4,1,5]
z=firstAndLastPosition(arr, 5, 1)
print(z)
