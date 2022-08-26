from cars import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.engines import Engine
from battery.nubbinbattery import NubbinBattery
from battery.spindlerbattery import SpindlerBattery


class CarFactory:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage,
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    def create_calliope(self):  # Car
        calliope = Car(
            CapuletEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage),
            SpindlerBattery(last_service_date=self.last_service_date, current_date=self.current_date))
        calliope.engine.needs_service() or calliope.battery.needs_service()

    def create_glissade(self):  # Car
        glissdade = Car(
            WilloughbyEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage),
            SpindlerBattery(last_service_date=self.last_service_date, current_date=self.current_date))
        glissdade.engine.needs_service() or glissdade.battery.needs_service()

    def create_palindrome(self):  # Car
        palindrome = Car(
            SternmanEngine(warning_light_on=self.warning_light_on),
            SpindlerBattery(last_service_date=self.last_service_date, current_date=self.current_date))
        palindrome.engine.needs_service() or palindrome.battery.needs_service()

    def create_rorschach(self):  # Car
        rorschach = Car(
            WilloughbyEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage),
            NubbinBattery(last_service_date=self.last_service_date, current_date=self.current_date))
        rorschach.engine.needs_service() or rorschach.battery.needs_service()

    def create_thovex(self):  # Car
        thovex = Car(
            CapuletEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage),
            SpindlerBattery(last_service_date=self.last_service_date, current_date=self.current_date))
        thovex.engine.needs_service() or thovex.battery.needs_service()
