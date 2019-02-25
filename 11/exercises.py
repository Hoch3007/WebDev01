class Robot(object):
    def __init__(self, model, mission):
        self.model = model
        self.mission = mission

    def print_attributes(self):
        print("The mission of " + str(self.model) + " is to " + str(self.mission) + ".")

# create 1 instance of Robot
# give it a the model "HAL9000"
# give it the mission "protect humans"
# print its model
# print its mission


hal9000 = Robot(model="HAL9000", mission="protect humans")
iamlegend = Robot(model="Terminator", mission="destroy humans")

# print(hal9000.model)
# print(hal9000.mission)
# print("The mission of " + str(hal9000.model) + " is to " + str(hal9000.mission)+".")

hal9000.print_attributes()
iamlegend.print_attributes()


# Read the 2 exercises.
# If you can develop the functionality with test driven development
#
# Part 1)
# add 2 methods to the class Car:
# a) decrease energy, this method decreases the battery status by 1
# b) increase energy, this method increases the battery status by 1
# Part 2)
# create an instance of Car
# demonstrate the functioning of the methods
# by always printing the battery status after applying the methods


class Car(object):
    def __init__(self):
        self.battery_status = 100

    def decrease_battery(self):
        self.battery_status -= 1
        return self

    def increase_battery(self):
        self.battery_status += 1
        return self


golf = Car()

print(golf.battery_status)
print("Driving........")
golf.decrease_battery()
print(golf.battery_status)


def check_battery():
    car = Car()
    assert (car.battery_status == 100)
    car.decrease_battery()
    assert (car.battery_status == 99), "Battery decrease does not work."
    car.increase_battery()
    assert (car.battery_status == 100), "Battery increase does not work."
    assert (car.decrease_battery().battery_status == 99)
    assert (car.increase_battery().battery_status == 100)


check_battery()
