#!/usr/bin/env python

# program2.py

"""
Description: This script checks if an integer is a palindrome
Author: Jason Burns
Date Created: January 24, 2024
"""


import unittest


class Integer:
    """This class takes an integer and sees if it is a palindrome"""
    def __init__(self, integer):
        self.integer = integer

    def __repr__(self):
        return f"n=Integer({self.integer})"

    def palindrome_check(self):
        """Check if integer is a palindrome"""
        if str(self.integer) == str(self.integer)[::-1]:
            result = f"{self.integer} is a palindrome"
        else:
            result = f"{self.integer} is NOT a palindrome"
        print(result)
        return result


def run_program2(integer):
    """
    Creates an Integer class object and checks if the
    integer is a palindrome
    """
    my_int = Integer(integer)
    return my_int.palindrome_check()


class Program2Tests(unittest.TestCase):
    """Unit tests class"""
    def test_palindrome(self):
        self.assertEqual(run_program2(121),
                         "121 is a palindrome")

    def test_not_a_palindrome(self):
        self.assertEqual(run_program2(1234),
                         "1234 is NOT a palindrome")


# this will run a unit test on Program 2
if __name__ == '__main__':
    unittest.main(verbosity=2)
