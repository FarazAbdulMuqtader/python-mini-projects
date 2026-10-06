import car as c
import wheels as w

my_wheels = w.Wheels(4)  #created outside the Car (aggregation)
car = c.Car("ABC-123", "Red", "Civic", my_wheels)
 
car.move()   # inherited from Vehicle
car.start()
car.stop()
 
# Wheels still exist even without the car
del car
print("Car deleted, but wheels still exist:", my_wheels.count)