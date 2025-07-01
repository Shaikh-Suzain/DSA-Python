#Sets - Unique Unordered Collections
unique_numbers = {1, 2, 3, 3, 2, 1}
print("Unique set:", unique_numbers)#Duplicate removed

unique_numbers.add(4)
unique_numbers.remove(2)

# Membership test
print("Is 3 in set?",3 in unique_numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))       
print("Intersection:", set1.intersection(set2))  
print("Difference:", set1.difference(set2))      