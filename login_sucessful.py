import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

	def setUp(self):
		#app = '/Users/a3logics/Desktop/megha/VendorCrush.app'
		app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
		app = os.path.abspath(app)
		self.driver = webdriver.Remote(
			command_executor='http://127.0.0.1:4723/wd/hub',
			desired_capabilities={
				'app': app,
				'platformName': 'iOS',
				'platformVersion': '11.4',
				'deviceName': 'iPhone 7',
				'bundleId':'com.frl.com.frl.VendorCrush'
			}
		)
		print(" your application is installed in the device sucessfully ")

	directory = '%s/' % os.
	file_name = 'screenshot.png'
	self.driver.save_screenshot(directory + file_name)	

	def tearDown(self):
   		self.driver.quit()	
	
	def testField(self):
		# through appium
		emailTF = self.driver.find_element_by_accessibility_id('login_email')
		emailTF.send_keys('linkin.park@mailina.com')
		#emailTF.send_keys(keys.RETURN)
		print("you email id is entered")
		#self.assertEqual(emailTF.get_attribute("value"), "linkin.park@mailinator.com")
		#print("yes email id is same")
		passwordTF = self.driver.find_element_by_accessibility_id('login_password')
		passwordTF.send_keys("0987654")
		#passwordTF.send_keys(Keys.RETURN)
		sleep(1)
		print("your password is entered")	

	def testLogin(self):
		self.testField()
		#el4 = self.driver.find_element_by_accessibility_id("loginButton")
		#el4.click()
		self.driver.find_element_by_accessibility_id('loginButton').click()
		sleep(1)
		#loginbutton = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='loginButton']")
		#loginbutton.click()
		#print("login done")
		el6 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther")
		el6.click()
		#personal information
		el4 = driver.find_element_by_accessibility_id("Personal Information")
		el4.click()	
		#click on user name
		el5 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField")
		el5.click()
		el5.send_keys("linkin1")



if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
	unittest.TextTestRunner(verbosity=2).run(suite)	