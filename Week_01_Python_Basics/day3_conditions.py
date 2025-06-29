age=int(input("Enter your age: "))

if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote yet.")
    
#Elif

marks=int(input("Enter your marks (out of 100): "))

if marks>=90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >=60:
    print("Grade: C")
else:
    print("Grade: D or Fail")