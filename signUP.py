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

    def testSignUp(self):
        # alert
        alertN = self.driver.find_element_by_accessibility_id('Allow').click()    
        sleep(1)
        # click on Sign-in Button
        signIn = self.driver.find_element_by_accessibility_id("Sign up")
        signIn.click()
        # first name
        fN = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        fN.click()
        fN.send_keys("Linkin1")
        # Second name
        el6 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")
        el6.click()
        el6.send_keys("park")
        # zip code 
        el7 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]")
        el7.click()
        el7.send_keys("50055")
        # keyboard
        TouchAction(self.driver).tap(x=339, y=431).perform()
        sleep(1)
        # email
        el8 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]")
        el8.click()
        el8.send_keys("imagine.park1@mailinator.com")
        sleep(1)
        TouchAction(self.driver).tap(x=328, y=437).perform()
        el8.click()
        TouchAction(self.driver).tap(x=339, y=429).perform()
        # confirm email
        el9 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]")
        el9.send_keys("imagine.park1@mailinator.com")
        sleep(1)
        TouchAction(self.driver).tap(x=341, y=423).perform()
        sleep(1)
        # swipe
        #self.driver.swipe("202", "606", "202", "383", "2000")
        self.driver.swipe("202", "483", "202", "148", "2000")
        sleep(1)
        print("swipe fixed1")
        # phone no.
        el10 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]")
        el10.click()
        el10.send_keys("9602225510")
        sleep(1)
        # keyboard
        TouchAction(self.driver).tap(x=339, y=431).perform()
        sleep(1)
        # swipe
        #self.driver.swipe("202", "242", "202", "94", "2000")
        self.driver.swipe("202", "324", "202", "383", "2000")
        sleep(1)
        print("swipe fixed2")
        # role tenant disable
        els5 = self.driver.find_elements_by_accessibility_id("Tenant")
        els5[0].click()
        print("tenant disabled")
        # swipe
       # self.driver.swipe("202", "242", "202", "94", "2000")
        self.driver.swipe("191", "618", "191", "94", "2000")
        sleep(1)
        print("swipe fixed2")
        # next
        #els2 = self.driver.find_elements_by_accessibility_id("Next")  
        el4 = self.driver.find_element_by_accessibility_id("Next >").click()
        #print("next pe click")
      #  TouchAction(self.driver).tap(x=181, y=608).perform()
        sleep(1)
        print("next pe click")
        # password
        el11 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el11.click()
        el11.send_keys("0987654")
        print("password")
        sleep(1)
        # confirm password
        el12 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")
        el12.send_keys("0987654")
        print("confirm password")
        sleep(1)
        # swipe
        self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed2")
        # select question 1
        TouchAction(self.driver).tap(x=78, y=320).perform() # the question field
        sleep(1)
        TouchAction(self.driver).tap(x=35, y=469).perform() # select the question
        sleep(1)
        # answer 1
        el15 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]")
        el15.click()
        el15.send_keys("Test1")
        sleep(1)
        # keyboard
        TouchAction(self.driver).tap(x=339, y=431).perform()
        sleep(1)
        # select question 2
        TouchAction(self.driver).tap(x=97, y=491).perform()  # the question field
        TouchAction(self.driver).tap(x=34, y=470).perform()  # select the question
        sleep(1)
        # answer 2
        el19 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]")
        el19.send_keys("Test2")
        sleep(1)
        # keyboard
        TouchAction(self.driver).tap(x=339, y=431).perform()
        sleep(1)
        # swipe
        self.driver.swipe("202", "582", "202", "304", "2000")
        sleep(1)
        print("swipe fixed3")
        # select question 3
        #TouchAction(self.driver).tap(x=77, y=484).perform()
        q3 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]")
        q3.click()
        sleep(1)
        TouchAction(self.driver).tap(x=32, y=472).perform()
        sleep(1)
        # answer 3    
        #el20 = TouchAction(self.driver).tap(x=101, y=374).perform()
        #el20.send_keys("Test3")
        ans3 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]")
        ans3.click()
        ans3.send_keys("test")
        sleep(1)
        # keyboard
        #TouchAction(self.driver).tap(x=339, y=431).perform()
        print("before last keyboard")
        TouchAction(self.driver).tap(x=329, y=426).perform()
        sleep(1)
        print("after last keyboard")
        # click on tearms and conditions
      #  el17 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]")
      #  el17.click()
     #   sleep(1)
        # click in tearms and condition radio button
       # TouchAction(self.driver).tap(x=43, y=480).perform()
        tnc = self.driver.find_elements_by_xpath("(//XCUIElementTypeButton[@name=\"Button\"])[1]\n")
        tnc[0].click()
        sleep(1)
        print("clicked on radio button of t&c ")
        #back
       # self.driver.back()
        sleep(1)
       # tnc[0].is_selected()
       # print("radio")
        # radio button of email
       # el21 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]")
       # el21.click()
        TouchAction(self.driver).tap(x=44, y=544).perform()
        sleep(1)
        # submit
        el16 = self.driver.find_element_by_accessibility_id("Submit")
        el16.click()
        sleep(1)
        # TouchAction(driver).tap(x=124, y=618).perform()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)