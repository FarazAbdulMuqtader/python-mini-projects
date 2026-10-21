from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def calc_area():
        pass

class Square(Shape):
    def __init__(self,name,len):
        super().__init__(name)
        self.len=len

    def calc_area(self):
        print("HI")

obj=Square(input("Enter shape name: "),input("Enter size: "))
obj.calc_area()