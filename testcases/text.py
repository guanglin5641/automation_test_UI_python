import time

import pytest
from common.data import case_data
from common.path import GetPath
from testcases.base import Base
from page.login_page import LoginPage
from page.supplier_page import SupplierPage
import allure
from common.tool import add_image_attach
add_case = case_data("supplier_case.xlsx", "add_supplier")
edit_case = case_data("supplier_case.xlsx","edit_supplier")

class TestSupplier(Base):
    @staticmethod
    def fill_supplier_form(page, supplier):
        #添加表单信息
        page.input_name(supplier["name"])
        page.select_type("type")
    @allure.epic("供应商管理")
    @allure.title("添加供应商")
    @pytest.mark.parametrize("supplier", add_case)
    def test_add_supplier(self, driver, supplier):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入供应商列表页"):
            page = SupplierPage(driver)
        with allure.step(supplier["前置条件"]):
            page.click_to_add_page()
        with allure.step(supplier["测试标题"]):
            self.fill_supplier_form(page, supplier["操作"])
            with allure.step("点击添加按钮"):
                res = page.click_add_button(supplier["操作"])
            with allure.step("断言"):
                assert res == supplier["预期结果"]