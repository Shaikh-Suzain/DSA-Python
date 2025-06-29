marks=[]
for i in range(5):
    mark=int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average=sum(marks)/len(marks)
print(" Average:", average)
print(" Highest:", max(marks))
print(" Lowest:", min(marks))