#-*-coding:utf-8 -*-
import unittest
import os
import time
from macaca import WebDriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '9.3.3',
    'deviceName': 'iPhone 5s',
    'reuse': '2',
    'autoAcceptAlert': True,
    'autoDismissAlert': True,
    'udid': 'f3691dd8403b4f685efdf85771850e1e98cb7e64',
    'bundleId': 'com.ucbrowser.iphone.ws7',
    # 'bundleId': 'com.uc.ucnews.int.dev1',
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_TestConfig(self):
        self.driver \
            .element_by_name("id_menuBtn") \
            .click()
        time.sleep(1)
        self.driver \
            .element_by_name("Test Config") \
            .click()
        time.sleep(1)
        self.driver \
            .element_by_name(u"进入业务功能参数配置") \
            .click()
        time.sleep(1)
        self.driver \
            .element_by_name(u"配置信息流服务器下发内容") \
            .click() 
        time.sleep(1)
        self.driver \
            .element_by_name("Test") \
            .click()  
        time.sleep(1)
        self.driver \
            .element_by_name("一键修改") \
            .click()   
        time.sleep(1)
        self.driver \
            .element_by_name("功能参数") \
            .click()
        time.sleep(1)
        self.driver \
            .element_by_name("测试配置") \
            .click()  
        time.sleep(1)
        self.driver \
            .element_by_name("关闭") \
            .click()      


        # time.sleep(3)
        # self.driver.save_screenshot('./webView.png')
        # self.driver.element_by_xpath('//XCUIElementTypeButton[1]')
            

   

if __name__ == '__main__':
    unittest.main()