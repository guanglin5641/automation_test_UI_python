import time
from common.data import case_data
import pytest
from common.path import GetPath
from testcases.base import Base
from page.login_page import LoginPage
from page.component_page import ComponentPage
import allure
from common.tool import add_image_attach
get_path = GetPath()
add_case = case_data("brand_case.xlsx", "add_brand")
edit_case = case_data("brand_case_ceshi.xlsx","edit_brand")
class TestBrand(Base):
    @allure.epic("品牌理")
    @allure.title("编辑品牌")
    @pytest.mark.parametrize("brand", edit_case)
    def test_edit_supplier(self, driver, brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入列表页"):
            page = ComponentPage(driver)
            numbers = page.number()
        with allure.step(brand["前置条件"]):
            page.click_edit_brand()
        with allure.step(brand["测试标题"]):
            logo_link = page.enter_brand_logo(brand["操作"]["brand_logo"])
            time.sleep(10)