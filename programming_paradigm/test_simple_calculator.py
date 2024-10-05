import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(10, 11), 21)
        self.assertEqual(self.calc.add(-18, 90), 72)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(8, 3), 5)
        self.assertEqual(self.calc.subtract(12, 6), 6)
        self.assertEqual(self.calc.subtract(-1, 6), -7)
        self.assertEqual(self.calc.subtract(15, 11), 4)
        self.assertEqual(self.calc.subtract(-18, 90), -108)        

    def test_multiply(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(28, 6), 168)
        self.assertEqual(self.calc.multiply(-8, 3), -24)
        self.assertEqual(self.calc.multiply(18, 5), 90)
        self.assertEqual(self.calc.multiply(10, 11), 110)
        self.assertEqual(self.calc.multiply(-18, 90), -1620)
       
    def test_divide(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(30, 10), 3)
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(90, 0), None)