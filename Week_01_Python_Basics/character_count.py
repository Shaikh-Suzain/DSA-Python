char_count={}
text=input("Enter the string: ")

for char in text:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
        
print("Character Count: ")
for key,value in char_count.items():
    print(key," : ",value)