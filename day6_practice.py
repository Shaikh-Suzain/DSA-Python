word=input("Enter a word: ")
reversed_word=word[::-1]#Reversing through slicing

if word== reversed_word:
     print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")