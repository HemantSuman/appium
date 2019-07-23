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
        app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
        # app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
        
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
        els5 = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField\n")
        print(els5[0])
        # els5[0].click()
        # sleep(1)
        # print("click ho gaya hai!!!!")
        els5[0].clear()
        sleep(1)
        print("clear bhi ho gaya")
        els5[0].send_keys("lol")
        sleep(1)
        # swipe upto submit button
        TouchAction(self.driver)   .press(x=262, y=599)   .move_to(x=257, y=220)   .release()   .perform()
        TouchAction(self.driver)   .press(x=214, y=583)   .move_to(x=224, y=418)   .release()   .perform()
        TouchAction(self.driver)   .press(x=180, y=426)   .move_to(x=181, y=306)   .release()   .perform()
        TouchAction(self.driver)   .press(x=267, y=466)   .move_to(x=269, y=249)   .release()   .perform()

        # print("print bhi ho gaya lol")
        # save the changes
      #  submit = self.driver.find_element_by_accessibility_id('Submit')  
       # submit.click()
     #   submit.submit();
        # submitp = self.driver.find_elements_by_xpath("//XCUIElementTypeButton[@name=\"Submit\"]\n")
        # submitp[0].click()
        print("Previous Submit")
        submtBtnY = self.driver.find_element_by_accessibility_id('SubmitM')
        submtBtnY.click()
        print("submit bhi ho gaya  wah!!")
        sleep(1)
      #  self.driver.back()
        # logout-------------------------
        logout = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]\n")
        logout[0].click()
        print("logout open ho gaya hai!!")
        sleep(1)
        # ----- ALERT ----
       #el1 = self.driver.switchTo().alert()        ---- Failed ------
       #print("is switch a sucessful")              ---- Failed ------ 
       # ------ logout --------
       # logout = self.driver.find_element_by_accessibility_id("Log out")
        #logout.click()
        logout = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]\n")
        logout[0].click()
        print("click on logout")
        # click on box
        logoutA = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther")
        print("logoutA")
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
