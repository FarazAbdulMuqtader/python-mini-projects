class Shape:
    def __init__(self,color,is_filled=False):
        self.color=color
        self.is_filled=is_filled

    def fill_color(self):
        if self.is_filled==False:
            self.is_filled=True

class circle(Shape):
    def __init__(self,radius,color,is_filled=False):
        super().__init__(color,is_filled)
        self.radius=radius

    def calc_area(self):
        return 3.142*self.radius**2

    def show_info(self):
        print("Circle color:",self.color)
        print("Circle radius:",self.radius)
        print("Circle area:",self.calc_area())
        print("Is Circle filled:",self.is_filled)
        print("Total Area:",)

class triangle(Shape):

    def __init__(self,breath,height,color,is_filled=False):
        super().__init__(color,is_filled)
        self.breath=breath
        self.height=height

    def calc_area(self):
        return 1/5*self.breath*self.height

    def show_info(self):
        print("Triangle color:",self.color)
        print("Triangle breath:",self.breath)
        print("Triangle height:",self.height)
        print("Triangle area:",self.calc_area())
        print("Is Triangle filled:",self.is_filled)
        print("Total Area:",)

class rectangle(Shape):
    def __init__(self,length,width,color,is_filled=False):
        super().__init__(color,is_filled)
        self.length=length
        self.width=width

    def calc_area(self):
        return self.length*self.width

    def show_info(self):
        print("Rectangle color:",self.color)
        print("Rectangle length:",self.length)
        print("Rectangle width:",self.width)
        print("Rectangle area:",self.calc_area())
        print("Is Rectangle filled:",self.is_filled)


class square(Shape):

    def __init__(self,length,color,is_filled=False):
        super().__init__(color,is_filled)
        self.length=length

    def calc_area(self):
        return self.length**2

    def show_info(self):
        print("Square color:",self.color)
        print("Square length:",self.length)
        print("Square area:",self.calc_area())
        print("Is Square filled:",self.is_filled)