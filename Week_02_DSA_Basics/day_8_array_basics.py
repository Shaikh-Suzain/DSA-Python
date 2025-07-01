arr=[3,5,1,7,9]

print("Length:",len(arr))
print("First:",arr[0])
print("Last:",arr[-1])

for i in arr:
    print("Value:",i)
    
total=sum(arr)
print("Sum:", total)

print("Max Value: ",max(arr))
print("Reversed: ",arr[::-1])