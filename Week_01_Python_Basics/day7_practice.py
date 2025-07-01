input_str = input("Enter numbers separated by commas: ")
num_list=[]
for x in input_str.split(","):
    num_list.append(int(x))
unique=set(num_list)
print("Unique values:", list(unique))
    



items = [1, 2, 2, 3, 4, 4, 5, 1, 2]
print("Original list:", items)

unique=list(set(items))
print("After removing duplicates:", unique)