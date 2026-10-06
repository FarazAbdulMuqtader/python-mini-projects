class shape:
    def __init__(self,side,area):
        self.sides=side
        self.area=area
    def __mul__(self,other):
        return self.side*other
    def __ge__(self,other):
        return self.area>=other.area

class square(shape):
    def __init__(self,side,area):
        super().__init__(side,area)
    def show_info(self):
        print(self.side)

class rectangle(shape):
   def show_info(self):
       print(self.side)

sq=square(4,5)
rect=rectangle(8,4)
nsh=sq >=rect
print(nsh)