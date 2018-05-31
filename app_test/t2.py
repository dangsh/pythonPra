# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "OD103"
caps["appPackage"] = "com.smartisanos.calculator"
caps["appActivity"] = "com.smartisanos.calculator.Calculator"
caps["platformVersion"] = "7.1"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# el9 = driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageButton[1]")
# el9.click()
el10 = driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.FrameLayout/com.smartisanos.calculator.DisplayView")
print(el10.get_attribute("text"))