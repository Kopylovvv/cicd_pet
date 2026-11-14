import unittest

import calc


class TestCalc(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(calc.add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
