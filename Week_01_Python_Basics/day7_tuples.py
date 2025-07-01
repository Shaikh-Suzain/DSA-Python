#Tuple-Ordered, immutable collection
dimensions=(10,20,30)
print("Tuple:", dimensions)

# Indexing
print("First item:", dimensions[0])
print("Last item:", dimensions[-1])

# Tuple methods
print("Count of 20:", dimensions.count(20))
print("Index of 30:", dimensions.index(30))

# dimensions[1] = 5 ERROR
