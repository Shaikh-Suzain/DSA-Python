s="hello"
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]

print("Reversed:", rev)

arr=[1,2,2,3,1,4,2]
freq={}

for num in arr:
    freq[num]=freq.get(num,0)+1

# freq.get(num, 0) tries to get the current count of num in freq. If num isn’t in freq yet, it returns 0.

# Then, +1 adds 1 to that count.
print("Frequencies:", freq)
