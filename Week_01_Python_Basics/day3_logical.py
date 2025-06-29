username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
     print("✅ Login successful!")
else:
    print("❌ Login failed.")
    
age=int(input("Enter age: "))
has_id = input("Do you have a valid ID (yes/no)? ")

if age >= 18 or has_id=="yes":
    print("✅ You can enter the club.")
else:
    print("❌ Entry denied.")
    
is_logged_in = False
if not is_logged_in:
    print("You need to log in first.")