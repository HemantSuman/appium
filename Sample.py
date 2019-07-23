import unittest
import os
from appium import webdriver
from time import sleep

# class TableSearchTest(unittest.TestCase):


# if __name__ == "main":
	# main()

# def main():
# Set up appium
#app = os.path.join(os.path.dirname(__file__), 'TableSearchwithUISearchController/Swift', 'Search.swift.app')
def setUp(self):

app = '/Users/a3logics/Library/Developer/CoreSimulator/Devices/79091DD3-5415-4D7C-B162-6553C6575839/data/Containers/Bundle/Application/9579CA88-F4CA-4747-88F3-C6F6B8A72C47/VendorCrush.app'

app = os.path.abspath(app)
driver = webdriver.Remote(
	command_executor='http://127.0.0.1:4723/wd/hub',
	desired_capabilities = 
	{
		'app': app,
		'platformName': 'iOS',
		'platformVersion': '11.4',
		'deviceName': 'iPhone 7',
		'bundleId':'com.frl.com.frl.VendorCrush'
	}
)
print(" your application is installed in the device sucessfully ")

	