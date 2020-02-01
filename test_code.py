import unittest
from calculate_total import calculate_total
from amount_paid import amount_paid
from numbers_repeat import numbers_repeat
from fizz_buzz import fizz_buzz


class TestCode(unittest.TestCase):
    def test_fizz_buzz(self):
        expected = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17"
        self.assertIsInstance(fizz_buzz(17), str)
        self.assertEquals(fizz_buzz(17), expected)
        expected = "1,2,Fizz,4,Buzz,Fizz"
        self.assertEquals(fizz_buzz(6), expected)
        self.assertEquals(fizz_buzz(-1), "")
        self.assertRaises(TypeError, fizz_buzz, "12")

    def test_numbers_repeat(self):
        ip = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
        expected = "1 - 4 \n2 - 2 \n4 - 2 \n5 - 3 \n8 - 2 "
        self.assertIsInstance(numbers_repeat(ip), str)
        self.assertEquals(numbers_repeat(ip), expected)
        ip = [1, 2, 8, 0, 4, 2, 6, 6, 1, 3]
        expected = "1 - 2 \n2 - 2 \n6 - 2 "
        self.assertIsInstance(numbers_repeat(ip), str)
        self.assertEquals(numbers_repeat(ip), expected)
        self.assertRaises(TypeError, numbers_repeat, 12)
    
    def test_calculate_total(self):
        expected = "Total Score 20 \nBatsman 1 Score : 4 (1 + 3) \nBatsman 2 Score : 16 (2 + 4 + 1 + 6 + 2 + 1)"
        ip = [1, 2, 0, 0, 4, 1, 6, 2, 1, 3]
        self.assertEquals(calculate_total(ip), expected)
        expected = "Total Score 10 \nBatsman 1 Score : 1 (1) \nBatsman 2 Score : 9 (2 + 4 + 3)"
        ip = [1, 2, 0, 0, 4, 3]
        self.assertEquals(calculate_total(ip), expected)
        self.assertIsInstance(calculate_total(ip), str)
        self.assertRaises(TypeError, calculate_total, "12")
    
    def test_amount_paid(self):
        ip = {"Rick": 85, "Amit": 42,
                   "George": 53, "Tanya": 60, "Linda": 35} 
        self.assertIsInstance(amount_paid(ip), int)
        self.assertEquals(amount_paid(ip), 275)
        ip = {"Rick": 99, "Morty": 1} 
        self.assertIsInstance(amount_paid(ip), int)
        self.assertEquals(amount_paid(ip), 100)
        self.assertRaises(AttributeError, amount_paid, "12")

if __name__ == "__main__":
    unittest.main()