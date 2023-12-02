import unittest
from day1 import check_line 

class Test_AoC_Day1_1(unittest.TestCase):

    def test_(self):
        self.assertEqual(check_line("ab"), 0)

    def test_2(self):
        self.assertEqual(check_line("1"), 11)
    
    def test_3(self):
        self.assertEqual(check_line("a1a"), 11)
    
    def test_4(self):
        self.assertEqual(check_line("12"), 12)
    
    #def test_5(self):
    #    self.assertEqual(check_line("12"), 3)

thisdict = {
  "one": "1",
  "two": "2",
  "three": "3"
}

def prepare(input):
    return thisdict[input]
    if input == "three":
        return "3"
    if input == "two":
        return "2"
    return "1"

class Test_AoC_Day1_2(unittest.TestCase):

    def test_(self):
        self.assertEqual(prepare("one"), "1")

    def test_2(self):
        self.assertEqual(prepare("two"), "2")
        self.assertEqual(prepare("three"), "3")
        
if __name__ == '__main__':
    unittest.main()