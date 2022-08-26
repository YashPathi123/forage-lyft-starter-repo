from abc import abstractmethod


class Serviceable:
    @abstractmethod
    def needs_service(self, car):
        pass
