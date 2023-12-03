import unittest
from day1 import check_line, prepare


class Test_AoC_Day1_1(unittest.TestCase):
    def test_(self):
        self.assertEqual(check_line("ab"), 0)

    def test_2(self):
        self.assertEqual(check_line("1"), 11)

    def test_3(self):
        self.assertEqual(check_line("a1a"), 11)

    def test_4(self):
        self.assertEqual(check_line("12"), 12)


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

    def test_prepare(self):
        self.assertEqual(prepare("oneone"), "11")
        self.assertEqual(prepare("twotwo"), "22")
        self.assertEqual(prepare("onetwo"), "12")
        self.assertEqual(prepare("1onetwo"), "112")
        self.assertEqual(prepare("1oetwo"), "1oe2")
        self.assertEqual(prepare("eightwothree"), "8wo3")


class Test_Integration_Day1_2(unittest.TestCase):
    def test_checkline_and_prepare(self):
        self.assertEqual(check_line(prepare("oneone")), 11)
        self.assertEqual(check_line(prepare("1oetwo")), 12)
        self.assertEqual(check_line(prepare("two1nine")), 29)
        self.assertEqual(check_line(prepare("eightwothree")), 83)
        self.assertEqual(check_line(prepare("twoeighthree")), 28)
        self.assertEqual(check_line(prepare("abcone2threexyz")), 13)
        self.assertEqual(check_line(prepare("xtwone3four")), 24)
        self.assertEqual(check_line(prepare("4nineeightseven2")), 42)
        self.assertEqual(check_line(prepare("zoneight234")), 14)
        self.assertEqual(check_line(prepare("7pqrstsixteen")), 76)
        
        self.assertEqual(check_line(prepare("eighthreeight")), 88)
        self.assertEqual(check_line(prepare("threeigheighthree")), 83)

collection = dict (
    nine= "9",
    eight= "8",
    seven= "7",
    six= "6",
    five= "5",
    four= "4",
    three= "3",
    two= "2",
    one = "1",
)

def prepare2(s):
    val = ""
    amount = 3000
    for k in collection.keys():
        t = s.find(k)
        if t != -1 and t < amount:
            val = k
            amount = t
    return val

class Test_Prepare2(unittest.TestCase):
    def test_checkline_and_prepare(self):
        self.assertEqual(prepare2("one"), "one")
        self.assertEqual(prepare2("onetwo"), "one")
        self.assertEqual(prepare2("three"), "three")
        self.assertEqual(prepare2("1oetwo"), "two")
        self.assertEqual(prepare2("threeigheighthree"), "three")
        self.assertEqual(prepare2("eighthreeight"), "eight")

def sumUp(data):
    count = 0
    for line in data:
        count = count + check_line(prepare(line))
    return count


class Test_Sum_Up(unittest.TestCase):
    def test_prepare(self):
        testdata = ["two1nine", "eightwothree", "abcone2threexyz"]
        expected = 125
        actual = sumUp(testdata)
        self.assertEqual(actual, expected)

    def test_prepare(self):
        testdata = ["two1nine", "eightwothree", "abcone2threexyz",
                    "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
        expected = 281
        actual = sumUp(testdata)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
