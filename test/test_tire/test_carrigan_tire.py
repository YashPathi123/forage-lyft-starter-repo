import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        current_tire_wear = [0.2, 0.9, 1, 0]
        tire = CarriganTire(current_tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        current_tire_wear = [0.2, 0.3, 0.4, 0]
        tire = CarriganTire(current_tire_wear)
        self.assertFalse(tire.needs_service())
