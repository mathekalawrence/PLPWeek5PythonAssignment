#A program which demonstrates polymorphism in Vehicles with same action

class Car:
    """The car moves by driving"""
    def move(self):
        #Prints the message
        print("Driving")
        
class Boat:
    """Represents a boat which moves by sailing"""
    def move(self):
        print("Sailing")
        
class Plane:
    """A plane moves by flying"""
    def move(self):
        print("Flying")
        
#A function that takes a vehicle object and calls its move() method
def make_it_move(vehicle):
    vehicle.move()
    
if __name__== "__main__":
    #Creating instances of each class
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()
    
    print("Illustrating polymorphism:")
    
    #Calling the move() directly on each object
    print("\n Calling move() directly:")
    my_car.move()
    my_boat.move()
    my_plane.move()
        
        