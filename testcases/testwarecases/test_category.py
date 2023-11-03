from common.data import case_data
import pytest
from common.path import GetPath
from testcases.base import Base
from page.ware_page.login_page import LoginPage
from page.ware_page.category_page import CategoryPositionPage
import allure
from common.tool import add_image_attach
get_path = GetPath()
add_case = case_data("category_case.xlsx", "add_category")
edit_case = case_data("category_case.xlsx","edit_category")



class TestCategory(Base):
    @staticmethod
    def fill_category_form(page, category):
        # 添加表单信息
        page.enter_category_name(category["name"])
        page.enter_category_status(category["status"])
        link=page.enter_category_logo(category["icon"])
        return link

    @allure.epic("类目管理")
    @allure.title("添加类目")
    @pytest.mark.parametrize("category", add_case)
    def test_add_supplier(self, driver, category):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入类目列表页"):
            page = CategoryPositionPage(driver)
        with allure.step(category["前置条件"]):
            page.click_add_category()
        with allure.step(category["测试标题"]):
            link=self.fill_category_form(page, category["操作"])

            with allure.step("点击新增"):
                ret = page.click_category_save_button(category["操作"],link)
            with allure.step("断言"):
                assert ret == category["预期结果"]
                # assert ret == category["expected_outcome"]

    @allure.epic("类目管理")
    @allure.title("编辑类目")
    @pytest.mark.parametrize("category", edit_case)
    def test_edit_supplier(self, driver, category):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入列表页"):
            page = CategoryPositionPage(driver)
            numbers = page.category_number()
            print(numbers)
        with allure.step(category["前置条件"]):
            page.click_edit_category()
        with allure.step(category["测试标题"]):
            page.enter_category_name(category["操作"]["name"])
            logo_link = page.enter_category_logo(category["操作"]["icon"])
            page.enter_category_status(category["操作"]["status"])

            with allure.step("点击编辑按钮"):
                rret = page.click_edit_button(category["操作"], numbers, logo_link)
            with allure.step("断言"):
                assert rret == category["预期结果"]

