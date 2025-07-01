#List - Ordered,Mutable collection that can hold elements of any data type

fruits=["apple","banana","mango","grape"]
# Indexing
print("First Fruit: ",fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First two fruits:",fruits[0:2])
print("All except last:",fruits[:-1])

for fruit in fruits:
    print(fruit)