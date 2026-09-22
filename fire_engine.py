import vehicle as v

class fire_engine(v.Vehicle):
    def __init__(self,ID,status="active"):
        super().__init__(ID,status="active")
        self.water_level=100
        self.fuel_level=100

    def service_provided(self):
        if self.status == "active":
            print("fire engine is on the way")
        else:
            print("unavailable")        

    def charging(self):
        if self.fuel_level<= 50:
            print("fire engine needs to recharge")
        else:
            print("no need")    
    def maintainance(self):
        if self.status == "inactive":
            print("Currently on maintainance")
    
    def spray_water(self):
        if self.status =="active":
            if self.water_level>=25 and self.fuel_level>=25:
                print("Water can be sprayed")
                water=print(input("How much water needed:"))
                self.water_level-=water
                fuel=print(input("How much fuel needed: "))
                self.fuel_level-=fuel
            else:
                print("INSUFFICENT WATER OR FUEL LEVEL")
        else:
            print("Fire Engine is on another route.")

