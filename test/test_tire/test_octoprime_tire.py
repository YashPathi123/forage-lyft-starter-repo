import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        current_tire_wear = [0.7, 0.8, 0.9, 0.6]
        tire = OctoprimeTire(current_tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        current_tire_wear = [0.2, 0.3, 0.4, 0]
        tire = OctoprimeTire(current_tire_wear)
        self.assertFalse(tire.needs_service())



