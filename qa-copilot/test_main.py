import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_non_numeric_input(self):
        with self.assertRaises(TypeError):
            add('a', 2)
        with self.assertRaises(TypeError):
            add(2, 'b')
        with self.assertRaises(TypeError):
            add('a', 'b')

if __name__ == "__main__":
    unittest.main()