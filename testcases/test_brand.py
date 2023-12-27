import time

import pytest
from common.path import get_path
from testcases.base import Base
from page.login_page import LoginPage
from page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach
create_data=[
    {
        "brand_name":"测试",
        "brand_status":"启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img":r"C:\Users\EDY\Downloads/ca9887acfce75d52caddc723f908f1d6.png",
        "main_categories":"",
        "alias":"测试别名",
        "english_name":"测试英文名",
        "consumer_group":"测试消费群体",
        "brand_positioning":"测试品牌定位",
        "sort":"2147483647",
        "establishment_time":"2023-11-11",
        "origin":"测试发源地",
        "affiliated_company":"测试所属公司",
        "remark":"测试备注",
        "expected_outcome":"添加品牌成功"
    },

]
class Testbrand(Base):
    @allure.epic("品牌管理")
    @allure.title("添加品牌")
    @pytest.mark.parametrize("brand", create_data)
    def test_add_supplier(self,driver,brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入品牌列表页"):
            page = BrandPositionPage(driver)
        with allure.step('进入新增品牌页面'):
            page.click_add_brand()
        with allure.step('输入品牌信息'):
            page.enter_brand_name(brand["brand_name"])
            page.enter_brand_status(brand["brand_status"])
            page.enter_brand_logo(brand["brand_logo"])
            page.enter_brand_main_img(brand["brand_main_img"])
            page.enter_brand_main_categories(brand["main_categories"])
            page.enter_brand_alias(brand["alias"])
            page.enter_brand_english_name(brand["english_name"])
            page.enter_brand_consumer_group(brand["consumer_group"])
            page.enter_brand_brand_positioning(brand["brand_positioning"])
            page.enter_brand_sort(brand["sort"])
            page.enter_brand_establishment_time(brand["establishment_time"])
            page.enter_brand_origin(brand["origin"])
            page.enter_brand_affiliated_company(brand["affiliated_company"])
            page.enter_brand_remark(brand["remark"])
            with allure.step("点击新增"):

                ret = page.click_brand_save_button()
                print(ret)

                with allure.step("断言"):
                    assert ret == brand["expected_outcome"]

