import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")

        # 设置为无头模式
        # options.add_argument("--headless")

        # 禁用GPU加速
        options.add_argument("--disable-gpu")

        # 禁用Chrome的沙盒模式，虽然在沙盒中运行以增加安全性，但是会出现一些问题
        options.add_argument("--no-sandbox")

        # 禁用/dev/shm的使用。在Linux系统上，Chrome通常会使用/dev/shm来管理共享内存
        options.add_argument("--disable-dev-shm-usage")

        service = Service()
        path = os.path.join(os.path.dirname(__file__), "chromedriver")
        # driver.py 所在目录存在 chromedriver 则直接使用，否则就自动下载
        if os.path.exists(path):
            service.path = path

        driver = webdriver.Chrome(options=options, service=service)

        # 删除所有cookies
        driver.delete_all_cookies()

        self.driver = driver

    def get_instance(self) -> WebDriver:
        """
        获取 driver 实例
        :return:
        """
        return self.driver

    def quit(self):
        """
        关闭 driver 实例
        :return:
        """
        self.driver.quit()


if __name__ == "__main__":
    pass
