import unittest
from simple_calculator import SimpleCalculator # type: ignore


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 7), -2)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(3, -3), -9)
    
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(3, 0), None)


if __name__ == '__main__':
    unittest.main()