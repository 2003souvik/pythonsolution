def findLongestSublist(l):
    n = len(l)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[l[0]] = 0
    for i in range(1, n):
        if l[i] not in pos:
            pos[l[i]] = i
 
        else:
            
            if pos[l[i]] >= st:
 
              
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
 
                st = pos[l[i]] + 1
             

            pos[l[i]] = i
         

    if maxlen < i - st:
        maxlen = i - st
        start = st
     
    return l[start : start + maxlen]
 
 
l=[2,4,5,2,4,5,7,8,9,10,11,4,8,6]
print(findLongestSublist(l))