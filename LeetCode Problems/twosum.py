def twoSum(nums, target):
        s={}
        for i in range(len(nums)):
            num= nums[i]
            compl=target-num
            if compl in s:
                return [s[compl],i]
            else:
                s[num]=i

        return []
    
l=[2,7,11,15]
print(twoSum(l,9))