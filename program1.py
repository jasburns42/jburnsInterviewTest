import unittest


def program1(binary_string):
    bin_seq_list = binary_string.split(",")
    divisible_by_five = []
    for seq in bin_seq_list:
        # print(seq, type(seq))
        if int(seq, 2) % 5 == 0:
            divisible_by_five.append(seq)
    return divisible_by_five


class Program1Tests(unittest.TestCase):
    def test_divisible(self):
        self.assertEqual(program1("111,1010,10111"), ["1010"])


# this will run a unit test on Program 1
if __name__ == '__main__':
    unittest.main()
