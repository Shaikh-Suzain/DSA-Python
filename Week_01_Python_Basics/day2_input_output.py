name = input("What is your name? ")
age = input("What is your age? ")
# Input is always taken as string → convert age to int
age = int(age)

# Simple formatted output
print("Hello ",name + "!" )
print("You will turn",age+1,"next year.")

# Float input + casting
temp=float(input("Enter your body temperature in Celsius: "))
print("Your temperature is:", temp)

#Boolean Logic
is_cold=temp<36.0
print("Is it cold?", is_cold)

