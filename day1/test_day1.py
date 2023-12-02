import unittest
from day1 import check_line 

class Test_AoC_Day1(unittest.TestCase):

    def test_(self):
        self.assertEqual(check_line("ab"), 0)

    def test_2(self):
        self.assertEqual(check_line("1"), 2)
    
    def test_3(self):
        self.assertEqual(check_line("a1a"), 2)
    
    def test_4(self):
        self.assertEqual(check_line("12"), 3)
    
if __name__ == '__main__':
    unittest.main()