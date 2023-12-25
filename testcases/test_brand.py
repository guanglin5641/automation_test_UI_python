import time

import pytest

from testcases.base import Base
from page.login_page import LoginPage
from page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach
create_data=[]
class Testbrand(Base):
    @allure.epic("供应商管理")
    @allure.title("添加供应商")
    @pytest.mark.parametrize("aaa", create_data)
    def test_add_supplier(self,driver,aaa):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入供应商列表页"):
            page = BrandPositionPage(driver)
            a = page.get_brand_list_text()
            print(a)
        with allure.step("进入添加供应商页面"):
            page.click_add_brand()
        with allure.step("添加供应商"):
            page.add_brand(aaa)

