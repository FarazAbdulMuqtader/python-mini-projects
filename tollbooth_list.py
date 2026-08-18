class TollBooth:
    def __init__(self):
        self.car_count = 0
        self.amount = 0
        self.collection_of_reg = []
    def car_passed(self,paid):
        if paid==True:
            print("Car can pass")  
            self.collection_of_reg.append("Car passed with payment")
            reg1 = input("Enter registration number of the car: ")
            self.collection_of_reg.append(reg1) 
        else:
            self.amount += 100
            self.car_count += 1
            self.collection_of_reg.append("Car passed without payment")
            reg2 = input("Enter registration number of the car: ")
            self.collection_of_reg.append(reg2)
            
            #if regestration number is already in the list, then do not add it again instead give reluncy of 5 times then stop the car from passing
            if reg2 in self.collection_of_reg[:-1]:
                print("Car with registration number", reg2, "has already passed more than ",self.car_count ," times without payment.")
                self.car_count += 1
                self.amount += 100
                self.collection_of_reg.pop()

    def defaulters(self):
        for i in range(len(self.collection_of_reg)):
            if self.collection_of_reg[i] == "Car passed without payment":
                return "Defaulter registration number:", self.collection_of_reg[i+1]

toll1=TollBooth()