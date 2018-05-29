# from appium import webdriver
#
# server = 'http://localhost:4723/wd/hub'
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'MI_NOTE_Pro',
#     'appPackage': 'com.tencent.mm',
#     'appActivity': '.ui.LauncherUI'
# }
#
#
# el4 = driver.find_element_by_id("com.tencent.mm:id/d2z")
# el4.click()
# el5 = driver.find_element_by_id("com.tencent.mm:id/ht")
# el5.send_keys("18613723052")
# el6 = driver.find_element_by_id("com.tencent.mm:id/ak_")
# el6.click()
# el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
# el7.send_keys("5801200zxg")
# TouchAction(driver).tap(x=521, y=1143).perform()
# TouchAction(driver).tap(x=614, y=1198).perform()


# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "OD103"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["platformVersion"] = "7.1"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el4 = driver.find_element_by_id("com.tencent.mm:id/d2z")
el4.click()
el5 = driver.find_element_by_id("com.tencent.mm:id/ht")
el5.send_keys("18613723052")
el6 = driver.find_element_by_id("com.tencent.mm:id/ak_")
el6.click()
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
el7.send_keys("123")
# TouchAction(driver).tap(x=521, y=1143).perform()
# TouchAction(driver).tap(x=614, y=1198).perform()

driver.quit()