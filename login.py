import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):
	def setUp(self):
			#app = '/Users/a3logics/Library/Developer/CoreSimulator/Devices/79091DD3-5415-4D7C-B162-6553C6575839/data/Containers/Bundle/Application/9579CA88-F4CA-4747-88F3-C6F6B8A72C47/VendorCrush.app' 
			#app = '/Users/a3logics/Library/Developer/CoreSimulator/Devices/782AB29B-5EF5-4EE4-9E44-F98C34C00C93/data/Containers/Bundle/Application/F2BFF057-330E-4B97-B0D0-39DAF5AE83D4/VendorCrush.app'
			app = '/Users/a3logics/Desktop/megha/VendorCrush.app'
			app = os.path.abspath(app)
			self.driver = webdriver.Remote(
				command_executor='http://127.0.0.1:4723/wd/hub',
				desired_capabilities ={
					'app': app,
					'platformName': 'iOS',
					'platformVersion': '11.4',
					'deviceName': 'iPhone 8 Plus',
					'bundleId':'com.frl.com.frl.VendorCrush'
				}
			)
			print(" your application is installed in the device sucessfully ")

	def testEmailField(self):
			#emailTF = driver.find_element_by_xpath("//XCUIElementTypeOther[@name='login_email']")
			emailTF = self.driver.find_element_by_accessibility_id('login_email')
			# emailTF = self.driver.find_elements_by_class_name('CustomTextFieldView')
			emailTF.send_keys('linkin.park@mailinator.com')
			emailTF.send_keys(keys.RETURN)
			print("you email id is entered")
			sleep(1)
			self.assertEqual(emailTF.get_attribute("value"), "linkin.park@mailinator.com")
			print("yes email id is same")

	def testPasswordField(self):
			passwordTF = self.driver.find_element_by_accessibility_id('login_password')
			passwordTF.send_keys("0987654")
			passwordTF.send_keys(keys.RETURN)
			print("your password is entered")
			sleep(1)
			self.assertNotEqual(passwordTF.get_attribute("value"), "0987654")

	def login(self):
			self.testEmailField()
			self.testPasswordField()
			self.driver.find_element_by_accessibility_id('loginButton').click()
			print("sucessfully clicked on login Button ")
			#emailTF = driver.find_element_by_xpath("//XCUIElementTypeButton[@name='loginButton']")
			sleep(1)


	def tearDown(self):
    		self.driver.quit()


if __name__ == '__main__':
		suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
		unittest.TextTestRunner(verbosity=2).run(suite)