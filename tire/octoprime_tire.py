from tires import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        tire_wear_sum = 0
        for x in self.sensor:
            tire_wear_sum = tire_wear_sum + x

        if tire_wear_sum >= 3:
            return True

        return False
