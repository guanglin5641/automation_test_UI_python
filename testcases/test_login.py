import time

from page.login_page import LoginPage
from testcases.base import Base
import pytest
import allure

import os

data = [
    {"username": "", "password": "", "expected": "必填"},
    {"username": "admin", "password": "111", "expected": "用户名或密码错误"},
    {"username": "admin", "password": "123456", "expected": "登录成功"},
]


class TestLogin(Base):
    @allure.epic("登录")
    @allure.title("网页登录")
    @pytest.mark.parametrize("account", data)
    def test_login(self, driver, account):
        """登录测试用例"""
        page = LoginPage(driver)
        with allure.step("输入用户名和密码"):
            page.input_username_value(account["username"])
            page.input_password_value(account["password"])
        with allure.step("点击登录按钮"):
            res = page.click_signin_button()
        with allure.step("断言"):
            assert account["expected"] == res

    @allure.epic("登录")
    @allure.title("api 登录")
    def test_api_login(self, driver):
        page = LoginPage(driver)

        with allure.step("登录 admin"):
            page.login_api_success()

if __name__ == '__main__':
    TestLogin()