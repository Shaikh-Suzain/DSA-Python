def count_subarrays_sum_k(arr,k):
    from collections import defaultdict
    prefix=defaultdict(int)
    prefix[0]=1#base case
    
    prefix_sum=0
    count = 0
    
    for num in arr:
        prefix_sum+=num
        count+=prefix[prefix_sum-k]
        prefix[prefix_sum]+=1
        
    return count

arr=[2,3,1,2,4,3]
k=7
print(count_subarrays_sum_k(arr,k))