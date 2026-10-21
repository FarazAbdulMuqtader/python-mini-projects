class A:
    def __init__(self):
        print("A")
        super().__init__()

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

class E(C):
    def __init__(self):
        print("E") 
        super().__init__()

class F(D,E):
    def __init__(self):
        print("F")
        super().__init__()

class G(E):
    def __init__(self):
        print("G")
        super().__init__()

class X(F,G):
    def __init__(self):
        print("X")
        super().__init__()  

obj=X()     