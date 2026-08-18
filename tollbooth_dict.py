class TollBooth:
    def __init__(self):
        self.car_count = 0
        self.amount = 0
        self.collection_of_reg = {}
        
    def car_passed(self, paid):
        if paid == True:
            print("Car can pass")  
            reg1 = input("Enter registration number of the car: ")
            self.collection_of_reg = {"status": "Car passed with payment", "reg": reg1}
        else:
            self.amount += 100
            self.car_count += 1
            reg2 = input("Enter registration number of the car: ")
            self.collection_of_reg = {"status": "Car passed without payment", "reg": reg2}  

    def defaulters(self):
        defaulters_dict = {}
        if self.collection_of_reg.get("status") == "Car passed without payment":
            reg_number = self.collection_of_reg["reg"]
            status_value = self.collection_of_reg["status"]
            defaulters_dict["reg"] = reg_number
            defaulters_dict["status"] = status_value
            return "Defaulter registration numbers:", defaulters_dict


toll1 = TollBooth()