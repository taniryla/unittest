import unittest

def sum(x, y):
    result = x + y
    return result

class SampleTest(unittest.TestCase):
    def test_sum_pos_int(self):
        self.assertEqual(sum(4, 6), 10)

if __name__ == '__main__':
    unittest.main()