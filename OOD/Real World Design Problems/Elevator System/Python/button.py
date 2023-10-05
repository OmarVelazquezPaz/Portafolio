from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, status):
        self.__status = status

    def press_down(self):
        pass

    @abstractmethod
    def is_pressed(self):
        pass


class HallButton(Button):
    def __init__(self, status, button_sign):
        super().__init__(status)
        self.__button_sign = button_sign

    def is_pressed(self):
        pass


class ElevatorButton(Button):
    def __init__(self, status, destination_floor_number):
        super().__init__(status)
        self.__destination_floor_number = destination_floor_number

    def is_pressed(self):
        pass
