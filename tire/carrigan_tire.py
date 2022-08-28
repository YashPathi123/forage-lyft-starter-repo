from abc import ABC

from tires import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        for x in self.sensor:
            if x >= 0.9:
                return True

        return False

