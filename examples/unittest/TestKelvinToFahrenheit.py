#!/usr/bin/env python

import unittest
import math

import kelvinToFahrenheitFunctions as k2f

class TestKelvinToFahrenheit (unittest.TestCase):
    # Test positive value, for instance 104 and 454
    def test_positive_value (self):
        fahr_temp = k2f.KelvinToFahrenheit(104)
        self.assertEqual(fahr_temp, -272.2)
        fahr_temp = k2f.KelvinToFahrenheit(454)
        self.assertEqual(fahr_temp, 357.8)

    # Test boundary value 273 and 0
    def test_boundary_value (self):
        fahr_temp = k2f.KelvinToFahrenheit(273)
        self.assertEqual(fahr_temp, 32)
        fahr_temp = math.ceil(k2f.KelvinToFahrenheit(255.22))
        self.assertEqual(fahr_temp, 0)

    # Test assert raises, in this case colder than absolute zero
    # something impossible.
    def test_colder_abs_zero (self):
        self.assertRaises(AssertionError,
                            k2f.KelvinToFahrenheit,
                            - 1)

if __name__ == '__main__':
    unittest.main()
