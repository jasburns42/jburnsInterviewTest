# This is the main script which calls both programs

import program1
import program2


if __name__ == '__main__':
    result1 = program1.program1("101010,1010,11001")
    print(result1)
    my_integer = program2.Integer(1234321)
    result2 = my_integer.palindrome_check()
    print(result2)

