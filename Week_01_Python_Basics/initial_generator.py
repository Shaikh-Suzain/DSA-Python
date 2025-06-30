full_name = input("Enter full name: ").strip()
name=full_name.split()
initials=""
for word in name:
    initials+=word[0].upper()+"."

print("Initials:", initials)
