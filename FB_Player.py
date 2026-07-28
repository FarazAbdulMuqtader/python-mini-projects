class FB_Player:
    def __init__(self,name,team,position):
        self.name = name
        self.team = team
        self.position = position
        self.score=0
    def update_score(self,score):
        self.score += score
    def show_info(self):
        print(f"{self.name} is the player of Team {self.team}. Play at a Position: {self.position} and has scored: {self.score}")

def compare(p1,p2):
    if p1.score>p2.score:
        print(f"{p1.name} has scored more than {p2.name}")
    elif p1.score<p2.score:
        print(f"{p2.name} has scored more than {p1.name}")
    else:
        print(f"{p1.name} and {p2.name} have scored the same points")            

p1=FB_Player("Rodri","Spain","CDM")
p2=FB_Player("Neymar","Brazil","LW")
p3=p1
p3=FB_Player("messi","Argentina","MRW")
print(hex(id(p1)))
print(hex(id(p2)))

if(hex(id(p1))==hex(id(p3))):
    print("Both have the same memory address")
else:
    print("Both have different memory address")

p1.update_score(5)
p2.update_score(3)

p1.show_info()
p2.show_info()

print(p1.show_info())
compare(p1,p2)