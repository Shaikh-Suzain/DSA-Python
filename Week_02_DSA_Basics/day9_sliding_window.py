arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

n=len(arr)
max_sum= sum(arr[:k])
window_sum=max_sum

for i in range(k,n):
    window_sum += arr[i]-arr[i-k]
    max_sum=max(max_sum,window_sum)

print("Max sum of subarray of size", k, "is:", max_sum)