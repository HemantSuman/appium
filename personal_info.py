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
    	# alert
    	alertN = self.driver.find_element_by_accessibility_id('Allow').click()    
    	sleep(1)
        #TouchAction(self.driver).tap(x=276, y=392).perform()
        #sleep(1)
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
        #print(setting_element[0])
        setting_element[0].click()
        print("print on settings")
        sleep(1)
        # <--------------- tried Action method, not removing for future refernece  ---------------------------------------------->

        # actions = TouchAction(self.driver)
        # actions.tap(setting_element)
        # actions.tap(setting_element).perform()
        # actions.perform()
        # print(" after settings code")
        # <---------------------------------------------------------------------------------------------------------------------->
        # click on personal information
        personal_information = self.driver.find_element_by_accessibility_id("Personal Information").click()
        # edit name
        sleep(1)
        firstname = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField\n")
       # print(firstname[0])
       # personal_information.click()
        # sleep(1)
        # print("click ho gaya hai!!!!")
        firstname[0].clear()
        sleep(1)
        print("clear bhi ho gaya")
        firstname[0].send_keys("lol")
       # firstname[0].set_value("lol1")
        sleep(1)
        firstname[0].send_keys(Keys.RETURN)
        print("return key")
        sleep(1)
        # phone number
        phoneNo = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]\n")
       	sleep(1)
       	self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed")
        self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed 2")
        sleep(1)
        self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed 3")
        sleep(1)
        self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed 4")
        sleep(1)
        # save the changes
        submit = self.driver.find_element_by_accessibility_id("Submit")
        submit.click()
        #submitp = self.driver.find_elements_by_xpath("//XCUIElementTypeButton[@name=\"Submit\"]\n")
        #submitp[0].click()
        print("submit pe click ")
        sleep(5)
        xyz11 = firstname[0].get_attribute("value")
        print(xyz11)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)