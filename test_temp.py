import unittest
from temp import celsius_to_far

class TestTemp(unittest.TestCase):

    def test_tests_work(self):
        self.assertEqual(2+2, 4)

    def test_c_to_f_happy(self):
        self.assertEqual(celsius_to_far(0), 32)
        self.assertEqual(celsius_to_far(-40), float(-40))
        self.assertEqual(celsius_to_far(100), 212)

    def test_c_to_f_unhappy(self):
        self.assertNotEqual(celsius_to_far(0), 35)
        self.assertNotEqual(celsius_to_far(-40), float(40))
        self.assertNotEqual(celsius_to_far(100), 12)

if __name__ == "__main__":
    unittest.main()
