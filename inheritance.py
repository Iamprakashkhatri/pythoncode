class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)
class PhysicianRobot(Robot): #Inheriting Robot Properties
    pass
x = Robot("Marvin")
x.say_hi()
y = PhysicianRobot("James")
y.say_hi()
