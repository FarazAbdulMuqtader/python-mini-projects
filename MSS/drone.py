import vehicle as v

class Drone(v.Vehicle):
    def __init__(self,ID,status="active"):
        super().__init__(ID,status="active")
        self.charge_level=100

    def service_provided(self):
        if self.status == "active":
            print("drone is on the way")
        else:
            print("unavailable")    
        

    def charging(self):
        if self.charge_level<= 50:
            print("drone needs to recharge")
        else:
            print("no need")    
    def maintainance(self):
        if self.status == "inactive":
            print("Currently on maintainance")
    def monitor(self):
        print("monitoring the area")
