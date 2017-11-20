import unittest
from beakerx.utils import *


class ColorTest(unittest.TestCase):
    def test_getColor_white(self):
        value = getColor(Color.white)
        self.assertEqual(value, "#ffffffff")

    def test_getColor_WHITE(self):
        value = getColor(Color.WHITE)
        self.assertEqual(value, "#ffffffff")

    def test_getColor_lightGray(self):
        value = getColor(Color.lightGray)
        self.assertEqual(value, "#ffc0c0c0")

    def test_getColor_LIGHT_GRAY(self):
        value = getColor(Color.LIGHT_GRAY)
        self.assertEqual(value, "#ffc0c0c0")

    def test_getColor_gray(self):
        value = getColor(Color.gray)
        self.assertEqual(value, "#ff808080")

    def test_getColor_GRAY(self):
        value = getColor(Color.GRAY)
        self.assertEqual(value, "#ff808080")

    def test_getColor_darkGray(self):
        value = getColor(Color.darkGray)
        self.assertEqual(value, "#ff404040")

    def test_getColor_DARK_GRAY(self):
        value = getColor(Color.DARK_GRAY)
        self.assertEqual(value, "#ff404040")

    def test_getColor_black(self):
        value = getColor(Color.black)
        self.assertEqual(value, "#ff000000")

    def test_getColor_BLACK(self):
        value = getColor(Color.BLACK)
        self.assertEqual(value, "#ff000000")

    def test_getColor_red(self):
        value = getColor(Color.red)
        self.assertEqual(value, "#ffff0000")

    def test_getColor_red(self):
        value = getColor(Color.red)
        self.assertEqual(value, "#ffff0000")


class DateTest(unittest.TestCase):
    def test_is_date_valid(self):
        test_string = is_date("10-10-2017 13:45")
        self.assertIs(test_string, True)

    def test_is_date_not_valid(self):
        test_string = is_date("10_10_2017 13:45")
        self.assertIs(test_string, False)