from abc import ABC,abstractmethod
import random
class Vehicle(ABC):
    def __init__(self,ID,status="active"):
        self.ID=ID or random.randint(1000, 2000)
        list_of_vehicles=[]

    @abstractmethod
    def service_provided(self):
        pass  
    def charge(self):
        pass
    def maintainance(self):
        pass
