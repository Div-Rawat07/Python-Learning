class Vechile:
    def start(self):
        print("Vechile is starting...") 

class Car(Vechile):
    def drive(self):
        print("Car is movingg...")  

c = Car()
c.start() # From parent
c.drive() # From child

