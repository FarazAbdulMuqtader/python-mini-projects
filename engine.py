# Composition parts (Car creates them, they live and die with the Car)
class Engine:
    def __init__(self, power, type):
        self.power = power
        self.type = type
 
    def start(self):
        print(f"Engine ({self.power}hp, {self.type}) started")
 
    def stop(self):
        print("Engine stopped")