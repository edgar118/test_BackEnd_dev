import unittest
from test_backend import is_palindrome, is_not_valid_transaction
from test_backend import UndergroundSystem

class TestIsPalindromo(unittest.TestCase):
    
    #is_palindrome True
    def test_palindromo(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))

    #is_palindrome False
    def test_no_palindromo(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
    
    #is_palindrome case_insensitive
    def test_palindromo_case_insensitive(self):
        self.assertTrue(is_palindrome("Radar"))
        self.assertTrue(is_palindrome("Level"))

class TestInvalidTransaction(unittest.TestCase):
    #test_fraudulent_transactions
    def test_fraudulent_transactions(self):
        transactions = [
            [1, 1000, 500.00, "Vadodara", 0],
            [2, 1000, 500.00, "Mumbai", 5],
            [3, 1001, 500.00, "Mumbai", 10],
            [4, 1001, 10000.00, "Mumbai", 10]
        ]
        expected = [2, 4]
        result = is_not_valid_transaction(transactions)
        self.assertEqual(result, expected)
    
    def test_fraudulent_transactions(self):
        transactions = [
            [1, 1000, 15000.00, "Vadodara", 0],
            [2, 1001, 500.00, "Mumbai", 5],
            [3, 1000, 200.00, "Mumbai", 15],
            [4, 1000, 7000.00, "Vadodara", 45],
            [5, 1001, 10000.00, "Mumbai", 50]
        ]
        expected = [1, 3, 4, 5]
        result = is_not_valid_transaction(transactions)
        self.assertEqual(result, expected)

class TestAverageTime(unittest.TestCase):
    #test_average_time
    def test_average_time(self):
        undergroundSystem = UndergroundSystem()
        undergroundSystem.check_in(1, "A", 3)
        undergroundSystem.check_out(1, "B", 8)

        undergroundSystem.check_in(2, "B", 4)
        undergroundSystem.check_out(2, "A", 10)

        expected = 5.0
        result =  undergroundSystem.get_average_time("A", "B")
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()