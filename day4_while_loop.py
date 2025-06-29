count = 1
while count <= 5:
    print("Count is:",count)
    count+=1
    
num=int(input("Enter a number to reverse: "))
rev=0
while num > 0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reversed number is:", rev)