import time

import pytest
from common.path import get_path
from testcases.base import Base
from page.login_page import LoginPage
from page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach

create_data = [
    {
        "brand_name": "测试",
        "brand_status": "启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img": get_path.get_image_path('main_img.png'),
        "main_categories": "",
        "alias": "测试别名",
        "english_name": "测试英文名",
        "consumer_group": "测试消费群体",
        "brand_positioning": "测试品牌定位",
        "sort": "2147483647",
        "establishment_time": "2023-11-11",
        "origin": "测试发源地",
        "affiliated_company": "测试所属公司",
        "remark": "测试备注",
        "expected_outcome": "添加品牌成功"
    },
    {
        "brand_name": "测试",
        "brand_status": "启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img": "",
        "main_categories": "",
        "alias": "",
        "english_name": "",
        "consumer_group": "",
        "brand_positioning": "",
        "sort": "2147483647",
        "establishment_time": "",
        "origin": "",
        "affiliated_company": "",
        "remark": "",
        "expected_outcome": "添加品牌成功"
    },
    {
        "brand_name": "",
        "brand_status": "启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img": "",
        "main_categories": "",
        "alias": "",
        "english_name": "",
        "consumer_group": "",
        "brand_positioning": "",
        "sort": "",
        "establishment_time": "",
        "origin": "",
        "affiliated_company": "",
        "remark": "",
        "expected_outcome": "请输入品牌名称"
    },
    {
        "brand_name": "测试",
        "brand_status": "启用",
        "brand_logo": "",
        "brand_main_img": "",
        "main_categories": "",
        "alias": "",
        "english_name": "",
        "consumer_group": "",
        "brand_positioning": "",
        "sort": "",
        "establishment_time": "",
        "origin": "",
        "affiliated_company": "",
        "remark": "",
        "expected_outcome": "请上传logo"
    },

]
edit_data = [
    {
        "brand_name": "测试",
        "brand_status": "启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img": get_path.get_image_path("logo.png"),
        "main_categories": "",
        "alias": "测试别名",
        "english_name": "测试英文名",
        "consumer_group": "测试消费群体",
        "brand_positioning": "测试品牌定位",
        "sort": "2147483647",
        "establishment_time": "2023-11-11",
        "origin": "测试发源地",
        "affiliated_company": "测试所属公司",
        "remark": "测试备注",
        "expected_outcome": "修改完成"
    },
    {
        "brand_name": "",
        "brand_status": "启用",
        "brand_logo": get_path.get_image_path("logo.png"),
        "brand_main_img": get_path.get_image_path("logo.png"),
        "main_categories": "",
        "alias": "测试别名",
        "english_name": "测试英文名",
        "consumer_group": "测试消费群体",
        "brand_positioning": "测试品牌定位",
        "sort": "2147483647",
        "establishment_time": "2023-11-11",
        "origin": "测试发源地",
        "affiliated_company": "测试所属公司",
        "remark": "测试备注",
        "expected_outcome": "请输入品牌名称"

    },
{
        "brand_name": "测试",
        "brand_status": "启用",
        "brand_logo": "",
        "brand_main_img": "",
        "main_categories": "",
        "alias": "",
        "english_name": "",
        "consumer_group": "",
        "brand_positioning": "",
        "sort": "",
        "establishment_time": "",
        "origin": "",
        "affiliated_company": "",
        "remark": "",
        "expected_outcome": "请上传logo"
    },

]


class TestBrand(Base):
    @allure.epic("品牌管理")
    @allure.title("添加品牌")
    @pytest.mark.parametrize("brand", create_data)
    def test_add_supplier(self, driver, brand):
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
            logo_link = page.enter_brand_logo(brand["brand_logo"])
            main_img_link = page.enter_brand_main_img(brand["brand_main_img"])
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
                ret = page.click_brand_save_button(brand, logo_link, main_img_link)
            with allure.step("断言"):
                assert ret == brand["expected_outcome"]

    @allure.epic("品牌理")
    @allure.title("编辑品牌")
    @pytest.mark.parametrize("brand", edit_data)
    def test_edit_supplier(self, driver, brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入列表页"):
            page = BrandPositionPage(driver)
            numbers = page.number()
            print(numbers)
        with allure.step("进入编辑品牌页面"):
            page.click_edit_brand()
        with allure.step("编辑品牌"):
            page.enter_brand_name(brand["brand_name"])
            page.enter_brand_status(brand["brand_status"])
            logo_link = page.enter_brand_logo(brand["brand_logo"])
            main_img_link = page.enter_brand_main_img(brand["brand_main_img"])
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
            with allure.step("点击编辑按钮"):
                rret = page.click_edit_button(brand, numbers, logo_link, main_img_link)
            with allure.step("断言"):
                assert rret == brand["expected_outcome"]

