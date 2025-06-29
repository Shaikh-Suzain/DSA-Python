balance = 5000
pin= int(input("Enter your 4 digit PIN: "))
if pin == 1234:
    print("✅ Access granted.")
    amount=int(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance-=amount
        print("✅ Withdrawn:", amount)
        print("Remaining Balance:",balance)
    else:
        print("Insufficient balance!")
else:
    print("❌ Incorrect PIN.")