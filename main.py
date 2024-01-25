#!/usr/bin/env python

# program1.py

"""
Description: This script reads inputs from config/inputs.json
and passes them to program1 and program2, which are run multithreaded.

Author: Jason Burns
Date Created: January 24, 2024
"""


import program1
import program2
import json
import threading


if __name__ == '__main__':
    """
    Calls both program1 and program2 in separate threads.
    Takes inputs from config/inputs.json
    """
    # read inputs file
    input_file = "config/inputs.json"
    with open(input_file) as input_data:
        inputs = json.load(input_data)
    # create threads
    t1 = threading.Thread(target=program1.run_program1,
                          args=(inputs["binary_sequence"],))
    t2 = threading.Thread(target=program2.run_program2,
                          args=(inputs["palindrome_check"],))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Both program1 and program2 have finished")
