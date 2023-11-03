import time
from common.config import conf
from page.base_page import BasePage
from position.supplier_postion.login_position import LoginPosition
from common.route import SUP_LONGIN
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.component_page import ComponentPage
class LoginPositionPage(BasePage,LoginPosition):
    def __init__(self, driver,path=SUP_LONGIN):
        super().__init__(driver,path,use_supplier_url=True)
        self.supplier_name = conf.get_by_name("supplier.username")
        self.supplier_pwd = conf.get_by_name("supplier.password")
    def login_send_login_name(self, username):
        self.find_element(position_expression=self.login_name()).send_keys(username)
        return
    def login_send_login_pwd(self, password):
        self.find_element(position_expression=self.login_pwd()).send_keys(password)
        return
    def login_click_login_button(self):
        self.find_element(position_expression=self.login_button()).click()

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_supplier_url(SUP_LONGIN)),
                EC.visibility_of_element_located(
                    (By.XPATH, self.name_error())
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, self.pwd_error())
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, self.toast_error())
                ),

                EC.visibility_of_element_located(
                    (By.XPATH, self.popup_error())
                )
            )
        )
        if isinstance(ret, bool):
            return "登录成功"
        else:
            return ret.text


    def login_success(self):
        self.find_element(position_expression=self.login_name()).send_keys(self.supplier_name)
        self.find_element(position_expression=self.login_pwd()).send_keys(self.supplier_pwd)
        self.find_element(position_expression=self.login_button()).click()
        wait = WebDriverWait(self.driver, 5)

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_supplier_url(SUP_LONGIN)),
                EC.visibility_of_element_located(
                    (By.XPATH, self.name_error())
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, self.pwd_error())
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, self.toast_error())
                ),

                EC.visibility_of_element_located(
                    (By.XPATH, self.popup_error())
                )
            )
        )
        if isinstance(ret, bool):
            return "登录成功"
        else:
            return "登录失败"



