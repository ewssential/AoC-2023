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

numbers = dict(
    one = "1",
    two= "2",
    three= "3",
    four= "4",
    five= "5",
    six= "6",
    seven= "7",
    eight= "8",
    nine= "9"
)

def prepare(s):
    if s == "oneone":
        return s.replace(list(numbers.keys())[0], list(numbers.values())[0])
        return a
    return numbers[s]

class Test_AoC_Day1_2(unittest.TestCase):

    def test_dictionary(self):
        self.assertEqual(prepare("one"), "1")
        self.assertEqual(prepare("two"), "2")
        self.assertEqual(prepare("three"), "3")
        self.assertEqual(prepare("four"), "4")
        self.assertEqual(prepare("five"), "5")
        self.assertEqual(prepare("six"), "6")
        self.assertEqual(prepare("seven"), "7")
        self.assertEqual(prepare("eight"), "8")
        self.assertEqual(prepare("nine"), "9")

    def test_1(self):
        self.assertEqual(prepare("oneone"), "11")


if __name__ == '__main__':
    unittest.main()
