import unittest
from assignment_four import format_cost
from assignment_four import get_cost


class MyTestCase(unittest.TestCase):
    def test_get_cost(self):
        self.assertEqual(70, get_cost(50, "H"))
        self.assertEqual(-1, get_cost(-2, "Mont"))

    def test_format(self):
        self.assertEqual("60.00", format_cost(60))
        self.assertEqual("66.00", format_cost(66))
        self.assertEqual("9.00", format_cost(9))
        self.assertEqual("5.80", format_cost(5.8))
        self.assertEqual("42.86", format_cost(42.86))
        self.assertEqual("0.55", format_cost(0.559))
        self.assertEqual("0.55", format_cost(0.5585098702384759))
        self.assertEqual("0.00", format_cost(0))

