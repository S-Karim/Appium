from appium import webdriver
import time
import base64
import os
desired_cap ={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app":"C:/Users/akkar/Desktop/android sdk/Airmirror/com.sand.airmirror-v1.0.4.3.apk",
    "appPackage":"com.flipkart.android",
    "appActivity":"com.flipkart.android.SplashActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
driver.start_recording_screen()
driver.implicitly_wait(10)
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()
driver.implicitly_wait(10)
driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
driver.implicitly_wait(10)

search_element=driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView")
driver.set_value(search_element,"iphone")
driver.implicitly_wait(10)

driver.execute_script('mobile: performEditorAction',{'action':'search'})
driver.implicitly_wait(40)

driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='₹35,999']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='ADD TO CART']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='SKIP & GO TO CART']").click()
driver.implicitly_wait(10)
video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
filepath = os.path.join("G:/Screenshot/",video_name+".mp4")
with open(filepath,"wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
driver.implicitly_wait(10)
ts=(time.strftime("%Y_%m_%d_%H%M%S"))
activityname=driver.current_activity
filename=activityname+ts
driver.save_screenshot("G:/Screenshot/" + filename + ".png")

