import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calulator = Calculator()
        self.assert_IsInstance(calulator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator
        self.assertSetEqual(calculator.result, 4)
if __name__== '__main__':
    unittest.main()