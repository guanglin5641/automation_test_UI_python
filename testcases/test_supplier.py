import time

import pytest

from testcases.base import Base
from page.login_page import LoginPage
from page.supplier_page import SupplierPage

import allure
from common.tool import add_image_attach



create_data = [
    {
        "case_name": "创建供应商供应商为空",
        "name": "1234",
        "type": "1688",
        "resource_type": "CPS",
        "balance_warning": "",
        "account": "",
        "password": "",
        "company_info": {
            "company": "",
            "contact": "",
            "contact_content": "",
        },
        "status": "",
        "remark": "",
        "expected": "创建成功！",
    },
    # {
    #     "case_name": "创建供应商供应商类型为空",
    #     "name": "测试",
    #     "type": "",
    #     "resource_type": "CPS",
    #     "balance_warning": "",
    #     "account": "",
    #     "password": "",
    #     "company_info": {
    #         "company": "",
    #         "contact": "",
    #         "contact_content": "",
    #     },
    #     "status": "",
    #     "remark": "",
    #     "expected": "请选择供应商类型",
    # },
    # {
    #     "case_name": "创建供应商资源类型为空",
    #     "name": "测试",
    #     "type": "1688",
    #     "resource_type": "",
    #     "balance_warning": "",
    #     "account": "",
    #     "password": "",
    #     "company_info": {
    #         "company": "",
    #         "contact": "",
    #         "contact_content": "",
    #     },
    #     "status": "",
    #     "remark": "",
    #     "expected": "请选择资源类型",
    # },
    # {
    #     "case_name": "创建供应商创建成功",
    #     "name": "测试",
    #     "type": "1688",
    #     "resource_type": "CPS",
    #     "balance_warning": "",
    #     "account": "",
    #     "password": "",
    #     "company_info": {
    #         "company": "",
    #         "contact": "",
    #         "contact_content": "",
    #     },
    #     "status": "",
    #     "remark": "",
    #     "expected": "创建成功！",
    # },
]

edit_data = [
    {
        "case_name": "编辑供应商供应商为空",
        "name": "",
        "type": "1688",
        "resource_type": "CPS",
        "balance_warning": "",
        "account": "",
        "password": "",
        "company_info": {
            "company": "",
            "contact": "",
            "contact_content": "",
        },
        "status": "",
        "remark": "",
        "expected": "请输入供应商名称",
    },
]


class TestSupplier(Base):
    @staticmethod
    def fill_supplier_form(page, supplier):
        #添加表单信息
        page.input_name(supplier["name"])
        page.select_type(supplier["type"])
        page.select_resource_type(supplier["resource_type"])
        page.input_balance_warning(supplier["balance_warning"])
        page.input_account_password(supplier["account"], supplier["password"])
        page.input_company_info(supplier["company_info"])
        page.input_remark(supplier["remark"])
        page.select_status(supplier["status"])



    @allure.epic("供应商管理")
    @allure.title("添加供应商")
    @pytest.mark.parametrize("supplier", create_data)
    def test_add_supplier(self, driver, supplier):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入供应商列表页"):
            page = SupplierPage(driver)
        with allure.step("进入添加供应商页面"):
            page.click_to_add_page()
        with allure.step("添加供应商"):
            self.fill_supplier_form(page, supplier)
            with allure.step("点击添加按钮"):
                res = page.click_add_button()
                a = page.page_assertion(
                    supplier["name"],
                    supplier["type"],
                    supplier["resource_type"],
                    supplier["company_info"]["company"],
                    supplier["company_info"]["contact_content"],
                    supplier["status"],
                    supplier["balance_warning"],
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    supplier["remark"]
                )
                print(a)
            with allure.step("断言"):
                assert a == 'All assertions passed.'
                assert res == supplier["expected"]


    # @allure.epic("供应商管理")
    # @allure.title("编辑供应商")
    # @pytest.mark.parametrize("edit_supplier", edit_data)
    # def test_edit_supplier(self, driver, edit_supplier):
    #     with allure.step("登录"):
    #         LoginPage(driver).login_success()
    #         add_image_attach(driver, "登录")
    #     with allure.step("进入供应商列表页"):
    #         page = SupplierPage(driver)
    #     with allure.step("进入编辑供应商页面"):
    #         page.click_to_edit_page()
    #     with allure.step("编辑供应商"):
    #         with allure.step("填入表单信息"):
    #             page.input_name(supplier["name"])
    #             page.select_type(supplier["type"])
    #             page.select_resource_type(supplier["resource_type"])
    #             page.input_balance_warning(supplier["balance_warning"])
    #             page.input_account_password(supplier["account"], supplier["password"])
    #             page.input_company_info(supplier["company_info"])
    #             page.input_remark(supplier["remark"])
    #             page.select_status(supplier["status"])

