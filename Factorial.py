#Take a number and print its factorial using a while loop.
num=int(input("Enter a number: "))
fact = 1
while num>0:
    fact*=num
    num-=1
print("Factorial: ",fact)