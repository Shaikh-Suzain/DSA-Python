for i in range(1,10):
    if i ==5:
        print("Stopping at", i)
        break
    print(i)

for i in range(1,6):
    if i %2==0:
        continue
    print("Odd number:", i)