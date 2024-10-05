import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    
    def test_add(self):
        result = SimpleCalculator()
        self.assertEqual(result.add(3, 5), 8)
    
    def test_subtract(self):
        result = SimpleCalculator()
        self.assertEqual(result.subtract(8, 4), 4)

    def test_multiply(self):
        result = SimpleCalculator()
        self.assertEqual(result.multiply(5, 3), 15)

    def test_divide(self):
        result = SimpleCalculator()
        self.assertEqual(result.divide(21, 7), 3)


if __name__ == '__main__':
    unittest.main()