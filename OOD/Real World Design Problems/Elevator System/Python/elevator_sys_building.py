"""
The final class of an elevator system is the ElevatorSystem class which will be
a Singleton class, which means that the entire system will have only one instance
of this class. Moreover, there is a Building class that contains the instances
of Floor and ElevatorCar.
"""


class __ElevatorSystem(object):
    __instances = None

    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__ElevatorSystem, cls).__new__()
        return cls.__instances


class ElevatorSystem(metaclass=__ElevatorSystem):
    def __init__(self, building):
        self.__building = building

    def monitoring(self):
        pass

    def dispatcher(self):
        pass


class __Building(object):
    __instances = None

    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__Building, cls).__new__(cls)
        return cls.__instances


class Building(metaclass=__Building):
    def __init__(self):
        self.__floor = []
        self.__elevator = []
