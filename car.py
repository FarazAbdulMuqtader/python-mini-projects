import vehicle as v
import wheels as w
import gps 
import sound as s
import engine as e

class Car(v.Vehicle): 
    def __init__(self, reg, color, model, wheels):
        self.reg = reg
        self.color = color
        self.model = model
        self.engine = e.Engine(1500, "Petrol")  # Composition
        self.audiosys = s.AudioSystem()         # Composition
        self.gps = gps.GPS()                    # Composition
        self.wheels = wheels                    # Aggregation
 
    def start(self):
        print(f"\n{self.color} {self.model} ({self.reg}) starting...")
        self.engine.start()
        self.wheels.rotate()
        self.audiosys.play_sound()
        self.gps.show_location()
 
    def stop(self):
        print("\nStopping car...")
        self.audiosys.stop_sound()
        self.engine.stop()