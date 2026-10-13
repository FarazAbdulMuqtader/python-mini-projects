import bank as Bank

class HEI:
    class Emp:
        def __init__(self, name, pos):
            self.name = name
            self.pos = pos

    HEIlist = ["Lecturer", "Professor", "HOD", "Dean"]

    def __init__(self, name):
        self.name = name
        self.emp_list = []
        self.bank = Bank.Bank("UBL") 

    def add_emp(self, name, pos):
        if pos in HEI.HEIlist:
            self.emp_list.append(HEI.Emp(name, pos))
        else:
            print("Invalid position")

    def find_emp(self, name):
        for i in self.emp_list:
            if i.name == name:
                return f"{i.name} of {i.pos} is in the list"
        return "Not in the list"

    def pay_salary(self, account_no, emp_name, amount):
        slip = Bank.Bank.Payslip(account_no, emp_name)
        self.bank.transfer(slip, amount)