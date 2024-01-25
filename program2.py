import unittest


class Integer:

    def __init__(self, integer):
        self.integer = integer

    def __repr__(self):
        return f"n=Integer({self.integer})"

    def palindrome_check(self):
        if str(self.integer) == str(self.integer)[::-1]:
            return f"{self.integer} is a palindrome"
        else:
            return f"{self.integer} is NOT a palindrome"


class Program2Tests(unittest.TestCase):
    def test_palindrome(self):
        integer = Integer(121)
        self.assertEqual(integer.palindrome_check(),
                         "121 is a palindrome")

    def test_not_a_palindrome(self):
        integer = Integer(1234)
        self.assertEqual(integer.palindrome_check(),
                         "1234 is NOT a palindrome")


# this will run a unit test on Program 2
if __name__ == '__main__':
    unittest.main(verbosity=2)
