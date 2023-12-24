import json
import time

from selenium.webdriver import ActionChains

from position.login_position import LoginPosition
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.config import conf
from common import route
import requests
from urllib.parse import urljoin


class LoginPage(BasePage, LoginPosition):
    def __init__(self, driver, path=route.LOGIN_ROUTE):
        super().__init__(driver, path)

    def login_success(self):
        self.input_username_value(conf.get_by_name("username"))
        self.input_password_value(conf.get_by_name("password"))
        self.click_signin_button()

    def login_api_success(self, path=route.LOGIN_API_ROUTE):
        self.logger.info("--- api 登录 ---")

        username = conf.get_by_name("username")
        self.logger.info(f"用户名：{username}")

        password = conf.get_by_name("password")
        self.logger.info(f"密码：{password}")

        resp = requests.post(
            urljoin(conf.get_by_name("api_host"), path),
            json={"account": username, "password": password},
        )
        self.logger.info(f"api 接口返回：{resp.text}")
        if resp.status_code != 200:
            raise Exception(f"api接口请求错，用户名：{username}")
        data = resp.json()
        if data["code"] != 0:
            raise Exception(f"api登录错误，错误码：{data['code']}")
        token = data["data"]["token"]

        # 将 token 写入 localstorage
        storage_data = {
            "t": int(time.time() * 1000),
            "expired": 259200000,
            "data": token,
        }
        json_str = json.dumps(storage_data, ensure_ascii=False)
        js = f"window.localStorage.setItem('sourceToken','{json_str}')"
        self.driver.execute_script(js)

        # 跳转到首页
        self.driver.get(urljoin(conf.get_by_name("host"), route.INDEX))

    def input_username_value(self, value):
        if not value:
            return
        self.fill_element_value(value=value, position_expression=self.input("账号"))

    def input_password_value(self, value):
        if not value:
            return
        self.fill_element_value(value=value, position_expression=self.input("密码"))

    def click_signin_button(self):
        """
        点击登录按钮
        :return:
        """
        # xpath = self.button("登 录")
        # action = ActionChains(self.driver)
        # action.click(self.find_element(position_expression=xpath))
        self.find_element(position_expression=self.button("登 录")).click()
        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='el-form-item__error']")
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-message__content']")
                ),
                EC.url_changes(self.url),
            )
        )
        if isinstance(ret, bool):
            return "登录成功"
        else:
            return ret.text
