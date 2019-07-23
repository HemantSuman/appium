import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction

class LoginTests(unittest.TestCase):

    def setUp(self):
        # app = '/Users/a3logics/Desktop/megha/VendorCrush.app'
       # app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
        app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
        
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'deviceName': 'iPhone 7'
                # 'bundleId':'com.frl.com.frl.VendorCrush'
            }
        )
        print(" your application is installed in the device sucessfully ")

    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        # email
        emailTF = self.driver.find_element_by_accessibility_id('login_email')
        emailTF.send_keys('linkin.park@mailinator.com')
        print("you email id is entered")
        # password
        passwordTF = self.driver.find_element_by_accessibility_id('login_password')
        passwordTF.send_keys("0987654")
        sleep(1)
        # login
        self.driver.find_element_by_accessibility_id('loginButton').click()
        print("login done")
        sleep(1)
        # click on settings-------in Xcode---- search for the element ->> user define run time attribute as ---> accessibilityIdentifier = accSettingBtn
        setting_element = self.driver.find_elements_by_xpath("//XCUIElementTypeButton[@name=\"accSettingBtn\"]")
        sleep(1)
        print(setting_element[0])
        setting_element[0].click()
        print("print on settings")
        sleep(1)
        # ---- logout --------
        logout = self.driver.find_element_by_accessibility_id("Log out")
        logout.click()
        print("click on logout")
        # click on radio button
        TouchAction(self.driver).tap(x=52, y=333).perform()
        print("click on radio button")
        sleep(1)
        # click on ok
        TouchAction(self.driver).tap(x=95, y=380).perform()
        print("click on ok")
        sleep(1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)          