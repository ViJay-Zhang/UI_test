from appium import webdriver
import time

# 启动参数
desired_caps={}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:52001'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
#最好输入appActivity的完整名称，有些app不输入完整的名称执行脚本会报错
desired_caps['appActivity'] = '.Settings'
#unicode设置(允许中文输入)
desired_caps['unicodeKeyboard'] = True
#键盘设置(允许中文输入)
desired_caps['resetKeyboard'] = True
time.sleep(3)
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
driver.quit()