from appium import webdriver
import time
import base64
import os
desired_cap ={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C:/Users/akkar/Desktop/android sdk/Airmirror/com.sand.airmirror-v1.0.4.3.apk",
    "appPackage": "com.sand.airmirror",
    "appActivity": "com.sand.airmirror.ui.splash.SplashActivity_"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
driver.start_recording_screen()
driver.find_element_by_id("com.sand.airmirror:id/tvRegister").click()
'''
search_element=driver.find_element_by_id("com.sand.airmirror:id/content")
driver.set_value(search_element,"cacctesting2@gmail.com")
driver.implicitly_wait(10)
#driver.find_element_by_id("com.flipkart.android:id/btn_msignup").click()
driver.find_element_by_xpath("//android.widget.EditText[@text='Password']").send_keys("Python2019*")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.EditText[@text='Enter password again']").send_keys("Python2019*")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.EditText[@text='Nick name']").send_keys("Sk")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@text='NEXT']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.EditText[@text='Enter Verification Code']").send_keys("QKAEQA")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@text='VERIFY AND SIGN UP']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='Cancel']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='Me']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='Sign out']").click()
driver.implicitly_wait(10)
'''
driver.find_element_by_xpath("//android.widget.TextView[@text='SIGN IN']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.EditText[@text='Email']").send_keys("cacctesting2@gmail.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.EditText[@text='Password']").send_keys("Python2019*")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@text='SIGN IN']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='OK']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.Button[@text='Allow']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='Cancel']").click()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//android.widget.TextView[@text='Me']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.TextView[@text='Sign out']").click()

video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
filepath = os.path.join("G:/Screenshot/",video_name+".mp4")
with open(filepath,"wb") as vd:
    vd.write(base64.b64decode(video_rawdata))

ts = (time.strftime("%Y_%m_%d_%H%M%S"))
activityname = driver.current_activity
filename = activityname + ts
driver.save_screenshot("G:/Screenshot/" + filename + ".png")