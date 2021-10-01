import unittest
from abs_value import get_abs_val


class MyTestCase(unittest.TestCase):

    def test_abs_val(self):
        self.assertEqual(6.3, get_abs_val(-6.3))
        self.assertEqual(0, get_abs_val(0))
        self.assertEqual(84.53, get_abs_val(84.53))