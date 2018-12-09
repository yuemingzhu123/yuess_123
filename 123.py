import unittest
import HTMLTestRunner
from selenium import webdriver
class Baidu(unittest.TestCase):
    url = "https://www.baidu.com"
    dr = webdriver.Firefox()
    def test_baidu_search(self):
        self.dr.get(self.url)
        self.assertIn("百度一下", self.dr.title, "不是百度")
        self.dr.quit()
        print("2")

    def test_baidu_set(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("1111111111111111")
# def mysuite():
#     suite = unittest.TestSuite()
#     suite.addTest(Baidu("test_baidu_search"))
#     # suite.addTest(MyFirstUnit("test_case_num"))
#     suite.addTest(Baidu("test_baidu_set"))
#     return suite

if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    testunit.addTest(Baidu("test_baidu_set"))
    filename = 'D:\\python test\\work\\20181202\\pyunittest\\BaiduResult1.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='百度搜索测试报告',
    description='用例执行情况：')
    runner.run(testunit)






