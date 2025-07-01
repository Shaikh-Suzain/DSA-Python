arr=[2,4,1,7,9,3]
n=len(arr)

prefix=[0]*n
prefix[0]=arr[0]

for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
    
l,r=2,4

range_sum=prefix[r]-(prefix[l] if l > 0 else 0)
print(f"Sum from index {l} to {r} is:", range_sum)