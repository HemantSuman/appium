import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

	def setUp(self):
		app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
		app = os.path.abspath(app)
		self.driver = webdriver.Remote(
			command_executor='http://127.0.0.1:4723/wd/hub',
			desired_capabilities={
				'app': app,
				'platformName': 'iOS',
				'platformVersion': '12.1',
				'deviceName': 'iPhone 7'
				#'bundleId':'com.frl.com.frl.VendorCrush'
			}
		)
		print(" your application is installed in the device sucessfully ")

	def tearDown(self):
   		self.driver.quit() 	
	
	def testLogin(self):
		# email		
		emailTF = self.driver.find_element_by_accessibility_id('login_email')
		emailTF.send_keys('linkin.park@mailinator.com')
		sleep(1)
		print("you email id is entered")
		# password
		passwordTF = self.driver.find_element_by_accessibility_id('login_password')
		passwordTF.send_keys("0987654")
		sleep(1)
		self.driver.find_element_by_accessibility_id('loginButton').click()
		print("login done")
		sleep(1)
		setting_element = self.driver.find_elements_by_xpath("//XCUIElementTypeButton[@name=\"accSettingBtn\"]")
		sleep(1)
		print("after starting code")
		print(setting_element[0])
		print("i am printing")
		setting_element[0].click()
		sleep(5)

if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
 unittest.TextTestRunner(verbosity=2).run(suite)
