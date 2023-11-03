import time

from common.data import case_data
import pytest
from common.path import GetPath
from testcases.base import Base
from page.supplier_page.login_page import LoginPositionPage
from page.ware_page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach
get_path = GetPath()
add_case = case_data("sup_login.xlsx", "add_brand")


class TestLogin(Base):
    @allure.feature("登录")
    @allure.story("登录")
    @allure.title("登录")
    @pytest.mark.parametrize("login", add_case)
    def test_login(self, driver, login):
        page = LoginPositionPage(driver)
        page.login_send_login_name(login["操作"]["username"])
        page.login_send_login_pwd(login["操作"]["pwd"])
        ret = page.login_click_login_button()
        assert ret == login["预期结果"]

