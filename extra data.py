#emailTF = driver.find_element_by_xpath("//XCUIElementTypeOther[@name='login_email']")
			emailTF = self.driver.find_element_by_accessibility_id('login_email')
			# emailTF = self.driver.find_elements_by_class_name('CustomTextFieldView')
			emailTF.send_keys('linkin.park@mailinator.com')
			#emailTF.send_keys(keys.RETURN)
			print("you email id is entered")
			#self.assertEqual(emailTF.get_attribute("value"), "linkin.park@mailinator.com")
			#print("yes email id is same")
			passwordTF = self.driver.find_element_by_accessibility_id('login_password')
			passwordTF.send_keys("0987654")
			print("your password is entered")



el2 = self.driver.find_element_by_accessibility_id('login_email')
		el2.send_keys('linkin.park@mailinator.com')
		#el2.send_Keys(Keys.RETURN)
		print("email done")
		sleep(1)
		#self.assertEqual(el2.get_attribute("value"), "linkin.park@mailinator.com")
		print("email sucessfully done")
		el3 = self.driver.find_element_by_accessibility_id('login_password')
		el3.send_keys("0987654")
		#el3.send_Keys(Keys.RETURN)
		print("password done")
		sleep(1)
		#slef.assertNotEqual(el3.get_attribute("value"), "0987654")
		print("password sucessfully done")			


		{
  "platformName": "iOS",
  "platformVersion": "11.4",
  "deviceName": "iPhone 7",
  "app": "/Users/a3logics/Library/Developer/Xcode/DerivedData/VendorCrush-erlncoibubzofbbsjxrvgmajzisi/Build/Products/Debug-iphonesimulator/VendorCrush.app"
}