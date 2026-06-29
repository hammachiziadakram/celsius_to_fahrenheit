import unittest
from converter import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):

    # NORMAL CASES
    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_40(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    # FLOAT CASE
    def test_float_input(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)

    # BOUNDARY CASE
    def test_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)

    # INVALID INPUT TYPES
    def test_string_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("hot")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit([10])

    # DOMAIN ERROR
    def test_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(-300)

if __name__ == "__main__":
    unittest.main()