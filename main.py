# This is the main script which calls both programs

import program1
import program2
import json


if __name__ == '__main__':
    # read inputs file
    input_file = "config/inputs.json"
    with open(input_file) as input_data:
        inputs = json.load(input_data)
    result1 = program1.program1(inputs["binary_sequence"])
    print(f"Binary Sequence = {result1}")
    my_integer = program2.Integer(inputs["palindrome_check"])
    result2 = my_integer.palindrome_check()
    print(result2)
