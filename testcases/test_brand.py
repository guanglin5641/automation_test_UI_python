import time
from common.data import case_data
import pytest
from common.path import GetPath
from testcases.base import Base
from page.login_page import LoginPage
from page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach
get_path = GetPath()
add_case = case_data("brand_case.xlsx", "add_brand")
edit_case = case_data("brand_case.xlsx","edit_brand")



class TestBrand(Base):
    @allure.epic("品牌管理")
    @allure.title("添加品牌")
    @pytest.mark.parametrize("brand", add_case)
    def test_add_supplier(self, driver, brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入品牌列表页"):
            page = BrandPositionPage(driver)
        with allure.step(brand["前置条件"]):
            page.click_add_brand()
        with allure.step(brand["测试标题"]):
            page.enter_brand_name(brand["操作"]["brand_name"])
            page.enter_brand_status(brand["操作"]["brand_status"])
            logo_link = page.enter_brand_logo(brand["操作"]["brand_logo"])
            main_img_link = page.enter_brand_main_img(brand["操作"]["brand_main_img"])
            page.enter_brand_main_categories(brand["操作"]["main_categories"])
            page.enter_brand_alias(brand["操作"]["alias"])
            page.enter_brand_english_name(brand["操作"]["english_name"])
            page.enter_brand_consumer_group(brand["操作"]["consumer_group"])
            page.enter_brand_brand_positioning(brand["操作"]["brand_positioning"])
            page.enter_brand_sort(brand["操作"]["sort"])
            page.enter_brand_establishment_time(brand["操作"]["establishment_time"])
            page.enter_brand_origin(brand["操作"]["origin"])
            page.enter_brand_affiliated_company(brand["操作"]["affiliated_company"])
            page.enter_brand_remark(brand["操作"]["remark"])
            with allure.step("点击新增"):
                ret = page.click_brand_save_button(brand["操作"],)
            with allure.step("断言"):
                assert ret == brand["预期结果"]
                # assert ret == brand["expected_outcome"]

    @allure.epic("品牌理")
    @allure.title("编辑品牌")
    @pytest.mark.parametrize("brand", edit_case)
    def test_edit_supplier(self, driver, brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入列表页"):
            page = BrandPositionPage(driver)
            numbers = page.number()
        with allure.step(brand["前置条件"]):
            page.click_edit_brand()
        with allure.step(brand["测试标题"]):
            page.enter_brand_name(brand["操作"]["brand_name"])
            page.enter_brand_status(brand["操作"]["brand_status"])
            logo_link = page.enter_brand_logo(brand["操作"]["brand_logo"])
            main_img_link = page.enter_brand_main_img(brand["操作"]["brand_main_img"])
            page.enter_brand_main_categories(brand["操作"]["main_categories"])
            page.enter_brand_alias(brand["操作"]["alias"])
            page.enter_brand_english_name(brand["操作"]["english_name"])
            page.enter_brand_consumer_group(brand["操作"]["consumer_group"])
            page.enter_brand_brand_positioning(brand["操作"]["brand_positioning"])
            page.enter_brand_sort(brand["操作"]["sort"])
            page.enter_brand_establishment_time(brand["操作"]["establishment_time"])
            page.enter_brand_origin(brand["操作"]["origin"])
            page.enter_brand_affiliated_company(brand["操作"]["affiliated_company"])
            page.enter_brand_remark(brand["操作"]["remark"])
            with allure.step("点击编辑按钮"):
                rret = page.click_edit_button(brand["操作"], numbers)
            with allure.step("断言"):
                assert rret == brand["预期结果"]

