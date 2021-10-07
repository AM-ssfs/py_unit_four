import unittest

import grades
from triangles import is_triangle
from grades import points
from rock_paper_scissors import who_wins


class MyTestCase(unittest.TestCase):
    def test_is_triangle(self):
        self.assertTrue(is_triangle(7, 11, 16))
        self.assertFalse(is_triangle(20, 7, 11))
        self.assertFalse(is_triangle(4, 9, 3))
        self.assertFalse(is_triangle(9, 13, 22))

    def test_points_1(self):
        self.assertEqual(2, points(80, False))

    def test_points_2(self):
        self.assertEqual(0.2, points(64, True))

    def test_points_3(self):
        self.assertEqual(3, points(88, False))

    # Your additional tests go below this line


    def test_rps(self):
        self.assertEqual("win", who_wins(3, 2))
        self.assertEqual("tied", who_wins(1, 1))

        # Put the rest of the rps tests below this line. There should be 9 in total.

    def test_grades(self):
        self.assertEqual(4.2, grades.points(95, True))
        self.assertEqual(3, grades.points(94.9, False))
        self.assertEqual(3.2, grades.points(87.654321, True))
        self.assertEqual(2, grades.points(78.2, False))
        self.assertEqual(0, grades.points(66.66666666, False))

if __name__ == '__main__':
    unittest.main()
