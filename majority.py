def majorityElement( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z=0
        max=0
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for k,j in d.items():
            if(j>=max):
                max=j
                z=k
        return z
k=majorityElement( [1,1,1,2,2])
print(k)