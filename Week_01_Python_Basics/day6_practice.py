word=input("Enter a word: ")
reversed_word=word[::-1]#Reversing through slicing

if word== reversed_word:
     print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
    
#Take full name as input and print initials
name=input("Enter full name: ").strip()
names=name.split()
initials=""

for n in names:
    initials+= n[0].upper()+"."
print("Initials:", initials)