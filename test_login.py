import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import keys

class LoginTests(unitest.Testcase):

def setUp(self):
	# in app the absolute path is missing , need to provide the absolute path
	app = ('/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-drujpsgrcnoviifewrqsbmyiuslu/Build/Products/Debug-iphoneos/VendorCrush.app')
	self.driver = webdriver.Remote(
		command_executor = 'http://127.0.0.4:4723/wd/hub',
	#	command_executor = 'http://ec2-34-217-175-48.us-west-2.compute.amazonaws.com:1337/wd/hub',
		desired_capabities={
			'app': app,
			'platformName': 'iOS',
			'platformVersion': '11.4',
			'deviceName': 'iPhone'
		}
	)

def tearDown(self):
	self.driver.quit()

# test case 1 - test Email Field

def testEmailField(self):
	emailTF = self.driver.find_element_by_accessibility_id('emailTextField') # need to change
	emailTF.send_keys(keys.RETURN)
	sleep(1)
	self.assertEqual(emailTF.get_attribute("value"), "")

# test case 2 - test Password Field
def testPasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('passwordTextField') # need to change
        passwordTF.send_keys("validPW")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertNotEqual(passwordTF.get_attribute("value"), "validPW")