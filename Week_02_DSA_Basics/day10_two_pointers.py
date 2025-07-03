arr=[1,2,4,4]
k=8

arr.sort()
left = 0
right=len(arr)-1
found= False

while left<right:
    if arr[left] + arr[right] == k:
        found=True
        break
    elif arr[left]+arr[right] < k:
        left+=1
    else:
        right-=1
        
print("Found Pair:",found)