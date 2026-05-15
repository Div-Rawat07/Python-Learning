class Dog:
    def sound(self):
        print("Barkkkk...")

class Cat:
    def sound(self):
        print("Meowww...")

animals = [Dog() , Cat()]
for a in animals:
    a.sound()