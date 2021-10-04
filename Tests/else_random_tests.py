import unittest
from divisible import is_divisible
from exams import gets_a_zero
from maximum import max


class MyTestCase(unittest.TestCase):

    # In the space below, create a series of tests that will test the max function. Use the directions
    # as a guide for which tests to write. Instead of assertTrue or assertFalse, all of the tests will
    # be assertEqual. Make sure to import the appropriate information at the top of this file.

    def test_max(self):
        self.assertEqual(4, max(4, 2.53))
        self.assertEqual(70, max(70, 41.23))
        self.assertEqual(2.3, max(2.3, -7.53))
        self.assertEqual(-1.4, max(-1.4, -59.4))
        self.assertEqual(103, max(103, 103))

    def test_is_divisible(self):
        self.assertTrue(is_divisible(6, 3))
        self.assertFalse(is_divisible(19, 5))
        self.assertFalse(is_divisible(3, 6))
        self.assertTrue(is_divisible(5, 5))

    def test_exams(self):
        self.assertTrue(gets_a_zero(25, 10))
        self.assertTrue(gets_a_zero(32, 8))
        self.assertFalse(gets_a_zero(20, 0))
        self.assertFalse(gets_a_zero(32, 7))


if __name__ == '__main__':
    unittest.main()
