import hiker 
import unittest


class TestHiker(unittest.TestCase):
    # 1
    def test_global_function(self):
        self.assertEqual(42, hiker.global_answer())
    # 2
    def test_add_one(self):
        self.assertEqual("11", hiker.add_one(10))
    # 3
    def test_check_even(self):
        self.assertEqual("even", hiker.check_even_odd(10))

    def test_check_odd(self):
        self.assertEqual("odd", hiker.check_even_odd(11))
    # 4
    def test_fizz3(self):
        self.assertEqual("Fizz", hiker.fizz(3))

    def test_fizz4(self):
        self.assertEqual("4", hiker.fizz(4))

    # 5
    def test_fizzbuzz3(self):
        self.assertEqual("Fizz", hiker.fizzbuzz(3))

    def test_fizzbuzz5(self):
        self.assertEqual("Buzz", hiker.fizzbuzz(5))
    
    def test_fizzbuzz15(self):
        self.assertEqual("FizzBuzz", hiker.fizzbuzz(15))    

    def test_fizzbuzz7(self):
        self.assertEqual("7", hiker.fizzbuzz(7))

    # 6
    def test_fizzbuzz_not_int(self):
        with self.assertRaises(ValueError):
            hiker.fizzbuzz_with_numcheck("abc")
            
    def test_fizzbuzz_minus(self):
        with self.assertRaises(ValueError):
            hiker.fizzbuzz_with_numcheck(-1)
 
    def test_fizzbuzz_numcheck3(self):
        self.assertEqual("Fizz", hiker.fizzbuzz_with_numcheck(3))

    def test_fizzbuzz_numcheck5(self):
        self.assertEqual("Buzz", hiker.fizzbuzz_with_numcheck(5))
    
    def test_fizzbuzz_numcheck15(self):
        self.assertEqual("FizzBuzz", hiker.fizzbuzz_with_numcheck(15))    

    def test_fizzbuzz_numcheck7(self):
        self.assertEqual("7", hiker.fizzbuzz_with_numcheck(7))

    # 7
    def test_fizzbuzzplus3(self):
        self.assertEqual("Fizz", hiker.fizzbuzzplus(3))

    def test_fizzbuzzplus5(self):
        self.assertEqual("Buzz", hiker.fizzbuzzplus(5))
    
    def test_fizzbuzzplus15(self):
        self.assertEqual("FizzBuzz", hiker.fizzbuzzplus(15))    

    def test_fizzbuzzplus7(self):
        self.assertEqual("7", hiker.fizzbuzzplus(7))
        
    def test_fizzbuzzplus31(self):
        self.assertEqual("Fizz", hiker.fizzbuzzplus(13))

    def test_fizzbuzzplus52(self):
        self.assertEqual("Buzz", hiker.fizzbuzzplus(52))
    
    def test_fizzbuzzplus253(self):
        self.assertEqual("FizzBuzz", hiker.fizzbuzzplus(253))    
        


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
