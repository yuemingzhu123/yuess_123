import unittest
import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
class Baidu(unittest.TestCase):
    url = "https://www.baidu.com"
    def setUp(self):
        self.dr = webdriver.Firefox()
        print("sf")
        self.dr.get(self.url)

    def test_baidu_search(self):
        self.dr.find_element_by_id("kw").send_keys("testfan")
        self.dr.find_element_by_id("su").click()

    def test_baidu_set(self):
        mouse = self.dr.find_element_by_link_text("设置")
        ActionChains(self.dr).move_to_element(mouse).perform()  # 移动到  “设置‘
        self.dr.find_element_by_link_text("搜索设置").click()
        # 二次定位：第一种写法

        s = self.dr.find_element_by_id("nr")
        s.find_element_by_xpath("//option[@value='50']").click()
        sleep(2)

        self.dr.find_element_by_link_text("保存设置").click()
        sleep(2)
        self.dr.switch_to.alert.accept()

    def tearDown(self):
        sleep(2)
        self.dr.quit()

if __name__ == "__main__":
    unittest.main()






