def min_subarray_len(target, arr):
    start=0
    total=0
    min_len=float("inf")
# min_len — tracks the smallest window length found so far.
# Initialized to infinity so any real length will be smaller.

    for end in range(len(arr)):
        total+=arr[end]
        
        while total>=target:
            min_len=min(min_len,end-start+1)
            total-=arr[start]
            start+=1
    return min_len if min_len != float('inf') else 0

arr = [2,3,1,2,4,3]
target = 7
print(min_subarray_len(target,arr))