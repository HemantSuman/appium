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
        # print("print bhi ho gaya lol")
        # save the changes
        el8 = self.driver.find_element_by_accessibility_id("Submit")
        print("yaha tk thi hi")
        el8.click()
        print("submit bhi ho gaya  wah!!")
        sleep(1)
        # logout-------------------------
        logout = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]\n")
        logout[0].click()
        print("logout open ho gaya hai!!")
        sleep(1)
        # ----- ALERT ----
      #  el1 = self.driver.switchTo().alert()
       # print("is switch a sucessful")
        sleep(1)
        els2 = self.driver.find_elements_by_xpath("//XCUIElementTypeOther[@name=\"logoutAlert1\"]\n")
        els2[0].click()
        print("alert vala box")
        sleep(2)
        # Logout alert--------------
     # logoutA = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther")
    #    print("logoutA")
        #checkbox
      #  radio = self.driver.find_element_by_accessibility_id("logoutRadio")
     #   print("radio identify toh ho gaya")
      #  radio.click()
     #   print("am I joke to you")
        #self.driver.switchTo().alert()
        #print("switch hua?")
        #capabilities.setCapability("autoAcceptAlerts", true);

        #el9 = self.driver.find_element_by_accessibility_id("Log out")
        #el9.click()
        #sleep(1)
        # print("logout pe click bhi ho gaya")
        # self.driver.find_element_by_name('OK').click()
        # print("ok pe bhi click")

        # -----> popup for logout "are you sure <--------"
        # TouchAction(self.driver).tap(x=50, y=332).perform()
        # TouchAction(self.driver).tap(x=130, y=383).perform()
        # print("testing touch")
        # sleep(1)
 
 # different ways for logout

 #       logout = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]\n")
 #       logout[0].click()
 #       print("logout open ho gaya hai!!")
 #       sleep(1)
        # ----- ALERT ----
      #  el1 = self.driver.switchTo().alert()
       # print("is switch a sucessful")
  #      sleep(1)
  #      els2 = self.driver.find_elements_by_xpath("//XCUIElementTypeOther[@name=\"logoutAlert1\"]\n")
 #       els2[0].click()
 #       print("alert vala box")
 #       sleep(2)
        # Logout alert--------------
     #  logoutA = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther")
     #  print("logoutA")
        #checkbox
  #      radio = self.driver.find_element_by_accessibility_id("logoutRadio")
  #      print("radio identify toh ho gaya")
  #      radio.click()
  #      print("am I joke to you")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
