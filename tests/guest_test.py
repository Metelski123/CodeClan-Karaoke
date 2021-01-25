import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.name_1 = Guest("Jan", 35)
        self.name_2 = Guest("Jessica", 31)
        self.name_3 = Guest("Timmy", 69)

    def test_guest_has_name(self):
        self.assertEqual("Jan", self.name_1.name)
        self.assertEqual("Jessica", self.name_2.name)
        self.assertEqual("Timmy", self.name_3.name)