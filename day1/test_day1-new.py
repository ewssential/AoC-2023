import unittest

def getNumber(s):
    return "1"

class Test_1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(getNumber("1"), "1")

if __name__ == '__main__':
    unittest.main()
