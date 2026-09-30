# Aggregation part (exists independently, passed INTO the Car)
class Wheels:
    def __init__(self, count=4):
        self.count = count
 
    def rotate(self):
        print(f"{self.count} wheels rotating")