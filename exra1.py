mport unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

	def setUp(self):
		#app = '/Users/a3logics/Desktop/megha/VendorCrush.app'
		app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
		#app = '/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app'
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

	def tearDown(self):
   		self.driver.quit()

   	def testField(self):
   		#els1 = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther")
		#els1.click()



		# -----------extra from logintry1.
		#settings
		#settings_click = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther")
		#settings_click.click()
		#els1 = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther")
		#els1.click()
		#print("Befor Acc Setting")
		#self.driver.find_element_by_accessibility_id('accSettingBtn').click()
		#print("After Acc Setting")
		#self.driver.find_element_by_accessibility_id('SettingsVC').click()
		#print("I am on setting screen, let me know what settings need to be chnaged. I am on it !!")
		#sleep(1)
		#click on personal information
		#el5 = self.driver.find_element_by_accessibility_id("Personal Information")
		#el5 = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"Company name for Vendor profile\"]/XCUIElementTypeOther")
		#el5.click()
		# click on first name and edit name
		#el6 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField")
		#el6.click()
		#el7 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Vendor Crush\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField")
		#el7.send_keys(" first name")
		# save the changed information
		#el8 = self.driver.find_element_by_accessibility_id("Submit")
		#
		#el8.click()
		#check email if got the mail--------------------> this is advanced part-------need to fetch data through browser	