num=[10,5,8,21,3]

num.append(100)
num.insert(2,50)

print(num)

num.remove(5)
# removes last element
last = num.pop()
print(num)

num.sort()
print(num)

num.reverse()
print(num)

print("Modified list:", num)
print("Popped element:", last)

# Check if item exists
if 21 in num:
    print("21 is in the list!")

