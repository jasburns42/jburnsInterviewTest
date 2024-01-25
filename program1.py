#!/usr/bin/env python

# program1.py

"""
Description: This script checks if any sequence of comma-separated
4-digit binary numbers is divisible by 5

Author: Jason Burns
Date Created: January 24, 2024
"""


import unittest


def run_program1(binary_string):
    """
    Splits the binary_string and checks to see if
    it is divisible by 5. Returns a binary sequence of
    those binary numbers divisible by 5
    """
    bin_seq_list = binary_string.split(",")
    divisible_by_five_list = [
        seq for seq in bin_seq_list
        if int(seq, 2) % 5 == 0
    ]
    divisible_by_five_seq = ""
    for element in divisible_by_five_list:
        divisible_by_five_seq = divisible_by_five_seq + element + ","
    divisible_by_five_seq = divisible_by_five_seq[:-1]
    print(f"Binary Sequence = {divisible_by_five_seq}")
    return divisible_by_five_seq


class Program1Tests(unittest.TestCase):
    """Unit test class"""
    def test_divisible(self):
        self.assertEqual(run_program1(
            "0011,1010,1011"), "1010")


# this will run a unit test on Program 1
if __name__ == '__main__':
    unittest.main(verbosity=2)
