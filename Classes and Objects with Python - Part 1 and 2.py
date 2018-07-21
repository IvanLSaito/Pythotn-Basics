class Robot:
    #constructor
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

    def introduce_self(self):
        print("My name is: ", self.name, "bip bop")#self == this in java
class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    def sit_down(self):
        if self.isSitting == False:
            self.isSitting = True
            print("You just seated down")
        elif self.isSitting:
            print("You are already seated down.")

    def stand_up(self):
        if self.isSitting:
            self.isSitting = False
            print("You stood up")
        elif self.isSitting == False:
            print("You are not seated down")

"""r1 = Robot()
r1.name = "Ivan"
r1.color = "Red"
r1.weight = 30

r2 = Robot()
r2.name = "Jenkins the redneck robot"
r2.color = "Damn red son"
r2.weight = 80 """

r1 = Robot("Ivan", "Red", 30)
r2 = Robot("Wally", "Red", 20)

human1 = Person("Alice", "agressive", False)#, r1
human1.robot_owned = r2
#human1 now has r2 as an argument called robot_owned, it's just other way of define an attribute
human1.sit_down()
human1.sit_down()
human2 = Person("Becky", "talkative", True)#, r1
human2.robot_owned = r1
human2.stand_up()
human2.stand_up()

human2.robot_owned.introduce_self()
human1.robot_owned.introduce_self()