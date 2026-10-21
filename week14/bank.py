class Bank:
    class Emp:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    class Payslip:
        def __init__(self, account_no, name):
            self.account_no = account_no
            self.name = name

    bankposition = ["Manager", "Cashier", "Teller", "Guard"]

    def __init__(self, name):
        self.name = name
        self.emplist = []

    def add_emp(self, name, position):
        if position in self.bankposition:
            self.emplist.append(Bank.Emp(name, position))
        else:
            print("Invalid position")

    def find_emp(self, name):
        for i in self.emplist:
            if i.name == name:
                return f"{i.name} of {i.position} is in the list"
        return "Not in the list"

    def transfer(self, payslip, amount):
        print(f"Transferred {amount} to {payslip.name} (Acc: {payslip.account_no})")
