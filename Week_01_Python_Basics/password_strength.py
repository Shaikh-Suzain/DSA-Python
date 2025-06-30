password = input("Enter a password: ")

has_digit=any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if len(password)>=8 and has_digit and has_upper:
    print("✅ Strong password")
else:
    print("❌ Weak password")
