Balance=50000
print("MENU")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")
print("4. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is: ", Balance)
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= Balance:
            Balance -= amount
            print("Withdrawal successful. Your remaining balance is: ", Balance)
        else:
            print("Insufficient balance.")        
    elif choice == 3:
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            Balance += amount
            print("Deposit successful. Your balance is: ", Balance)
        else:
            print("Invalid amount.")

    elif choice == 4:
        print("Thank you for using our ATM.")
        break
    else:
        print("Invalid choice.")