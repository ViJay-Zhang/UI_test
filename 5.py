from appium import webdriver
import time
import threading

#方法一：此方法在启动后一个Appium可以正常执行，另外一个会出现“一个进程没有关闭，又运行另外一个进程了”的报错信息，
# 要先关闭再重启Appium才能再次执行，基本上不能同时执行多台模拟器或手机，有可能是Appium或模拟器的问题
# desired_caps1 = {
#     'platformName':'Android',
#     'platformVersion':'4.4.2',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.android.settings',
#     'appActivity':'.Settings'
# }
#
# desired_caps2 = {
#     'platformName':'Android',
#     'platformVersion':'4.4.2',
#     'deviceName':'127.0.0.1:62025',
#     'appPackage':'com.android.settings',
#     'appActivity':'.Settings'
# }
#
# def task1():
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
#     #休眠20s等待页面加载完成
#     time.sleep(20)
#     #打印获取当前上下文
#     # print(driver.contexts)
#     # print("127.0.0.1:62001执行完成")
#     driver.quit()
#
# def task2():
#     driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
#     #休眠20s等待页面加载完成
#     time.sleep(20)
#     #打印获取当前上下文
#     # print(driver.contexts)
#     # print("127.0.0.1:62025执行完成")
#     driver.quit()
#
# threads = []
# t1 = threading.Thread(target=task1)
# threads.append(t1)
#
# t2 = threading.Thread(target=task2)
# threads.append(t2)

# if __name__ == '__main__':
#     # for t in threads:
#     # t.start()
#
#     threading.Thread(target=task1).start()
#     threading.Thread(target=task2).start()


#方法二：此方法在启动后都在一个Appium和一个模拟器上执行，另外一个Appium和模拟器不执行
desired_caps={
    'platformName':'Android',
    'platformVersion':'4.4.2',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.android.settings',
    'appActivity':'.Settings'
}

desired_caps01={
    'platformName':'Android',
    'platformVersion':'4.4.2',
    'deviceName':'127.0.0.1:62025',
    'appPackage':'com.android.settings',
    'appActivity':'.Settings'
}

class Settest():

    # def test_seting01(self):
    #     self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #     time.sleep(3)
    #     #关闭驱动
    #     self.driver.quit()
    def test_seting02(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps01)
        time.sleep(3)
        #关闭驱动
        self.driver.quit()
a=Settest()
if __name__ == '__main__':
    # a.test_seting01()
    a.test_seting02()