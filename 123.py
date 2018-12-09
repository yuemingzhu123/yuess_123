import random
import unittest
global num
num = random.randint(1, 9999)
class Class1(unittest.TestCase):

    def setUp(self):
        self.num = num

    def test_case1(self):
        print(self.num)

    def test_case2(self):
        print(self.num)

    def test_case3(self):
        print(self.num)

if __name__ == "__main__":
    unittest.main()
