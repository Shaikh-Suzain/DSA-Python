my_list=[]
for i in range(5):
    num=int(input(f"Enter number {i+1}: "))
    my_list.append(num)

average = sum(my_list)/len(my_list)
print("Average: ",average)