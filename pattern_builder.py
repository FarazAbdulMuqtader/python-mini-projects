class PatternBuilder:
    def __init__(self,symbol,size):
        self.symbol=symbol
        self.size=size
    def draw_hollow_square(self):
        for i in range(1,self.size+1):
            for j in range(1,self.size+1):
                if i==1 or i==self.size or j==1 or j==self.size:
                    print(self.symbol,end=" ")
                else:
                    print(" ",end=" ")
            print()

    def draw_number_paramid(self):
        for i in range(self.size,0,-1):
            for k in range(self.size-i):
                        print(" ",end=" ")
            for j in range(1,i+1):
                print(j,end=" ")
            for l in range(i-1,0,-1):
                print(l,end=" ")
            print()

patterns=PatternBuilder("*",4)
print("Hollow Square Pattern: ")
patterns.draw_hollow_square()
print("Number Paramid Pattern: ")
patterns.draw_number_paramid()