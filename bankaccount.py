class My_Account:
    def __init__(self,title,pin):
        self.title = title
        self.pin = pin
        self.__balance = 0

    def withdraw(self,amount):
        if amount > self.__balance:
            return "Insufficient balance"
        elif amount<0:
            return "Invalid amount"
        else:
            self.__balance -= amount
            return f"Withdrawn: {amount}"

    def deposit(self,amount):
        if amount < 0:
            return "Invalid amount"
        else:
            self.__balance += amount
            return f"Deposited: {amount}"

    def show_balance(self):
        return f"Account Title: {self.title}, Balance: {self.__balance}"

ac1=My_Account("Mike", 1234)
print(ac1._My_Account__balance)
for i in range(2):
    print(ac1.deposit(float(input("Enter amount to deposit: "))))
    print(ac1.withdraw(float(input("Enter amount to withdraw: "))))
    print(ac1.show_balance())
