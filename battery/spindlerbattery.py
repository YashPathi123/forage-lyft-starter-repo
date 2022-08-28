from datetime import timedelta

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        nextservicedate = self.last_service_date + timedelta(3 * 365)
        if nextservicedate <= self.current_date:
            return True
        else:
            return False
