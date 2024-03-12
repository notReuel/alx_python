class Robot:
    "Creating a robot"

    #Class representing the number of robots
    population = 0

    def __init__ (self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        #When this bot is created.
        Robot.population += 1

    def die (self):
        print("{}'s work is done, let's kill it".format(self.name))

        Robot.population -= 1

        if Robot == 0:
            print("{} is the last Robot".format(self.name))
        else:
            print("There are {} surving robots".format(Robot.population))

    def say_hi(self):
        print("Hello master, I am your robot, you can call me {}".format(self.name))


    @classmethod
    def Robot_population(cls):
        #print population of robots
        print("We have {:d} robots in total".format(cls.population))
        print("{}".format(Robot.population))


robot1 = Robot("R2-D2")
robot2 = Robot("GPT")
robot3 = Robot("Digital Tutor")
robot1.say_hi()

robot2.die()

robot1.Robot_population()
