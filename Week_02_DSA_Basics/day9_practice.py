arr = [1, 12, -5, -6, 50, 3]
k = 4

window_sum=sum(arr[:-k])
max_avg= window_sum/k
for i in range(k,len(arr)):
    window_sum+=arr[i]-arr[i-k]
    max_avg=max(window_sum/k,max_avg)
    
print("Max average:", max_avg)


arr = [1, 2, 3, 4, 5]
prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]


queries=[(0,2),(1,3),(2,4)]

for l,r in queries:
    range_sum=prefix[r]-(prefix[l-1] if l>0 else 0)
    print(f"Sum from {l} to {r}:", range_sum)
