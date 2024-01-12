import time
from common.data import case_data
import pytest
from common.path import GetPath
from testcases.base import Base
from page.login_page import LoginPage
# from page.brand_page import BrandPositionPage
import allure
from common.tool import add_image_attach
import time
from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from position.brand_position import BrandPosition
from common.route import BRAND_LIST, WAREHOUSE_PRODUCTS_LIST
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json


from page.component_page import ComponentPage
class BrandPositionPage(ComponentPage, BrandPosition, BasePage):
    def __init__(self, driver, path=WAREHOUSE_PRODUCTS_LIST):
        super().__init__(driver, path)

    def enter_brand_logo(self, brand_logo):
        self.category_component("//label[text()='所属类目']/parent::div//input",brand_logo)
        return
    def click_edit_brand(self):
        self.find_element(position_expression="(//span[text()='编辑'])[1]").click()
        return
    def enter_brand_name(self):
        self.find_element(position_expression="//span[text()='下一步']").click()
        return

get_path = GetPath()
text = [
    {
        "title": "添加品牌",
    }
]



class TestBrand(Base):
    @allure.epic("品牌理")
    @allure.title("编辑品牌")
    @pytest.mark.parametrize("brand", text)
    def test_edit_supplier(self, driver, brand):
        with allure.step("登录"):
            LoginPage(driver).login_success()
            add_image_attach(driver, "登录")
        with allure.step("进入列表页"):
            page = BrandPositionPage(driver)
            # numbers = page.number()
        with allure.step(""):
            page.click_edit_brand()
        with allure.step("11"):
            # page.enter_brand_name()
            page.enter_brand_logo(["实物-1",""])