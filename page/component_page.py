import time
from selenium.common.exceptions import NoSuchElementException
from position.brand_position import BrandPosition
from page.base_page import BasePage
from common.route import BRAND_LIST, BRAND_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from common.path import GetPath
import json
class ComponentPage(BasePage,object):
    def __init__(self, driver, path=BRAND_LIST):
        super().__init__(driver, path)
    def image_component(self, main,brand_logo):
        '''
        图片选择组件
        :param main:
        :param brand_logo:
        :return:
        '''
        thumbnail_main_path = f"//div[text()='{main}']/parent::div"
        popups_main_path = f"(//div[@class='el-dialog'])[last()]"
        popups_link = popups_main_path + f"//input[@placeholder='输入图片链接后按回车键直接添加']"
        popups_choose = f"({popups_main_path}//div[@class='el-image'])[1]"
        popups_determine = f"({popups_main_path}//button)[last()]"
        thumbnail_check = thumbnail_main_path + '//li[1]'
        thumbnail_open = thumbnail_main_path + "//div[@class='yun-img-loader__pmask']"
        try:
            WebDriverWait(self.driver, 1).until(
                EC.any_of(EC.visibility_of_element_located((By.XPATH, thumbnail_check))))
            print(1)
            a = 1
        except:
            print(1)
            a = 0

        if not brand_logo:
            if a == 1:
                self.find_element(position_expression=thumbnail_check).click()
                operate = self.find_element(position_expression=thumbnail_check)
                operate.send_keys(Keys.BACKSPACE)
                return
            return
        if a == 1:
            self.find_element(position_expression=thumbnail_check).click()
            operate = self.find_element(position_expression=thumbnail_check)
            operate.send_keys(Keys.BACKSPACE)
        self.find_element(position_expression=thumbnail_open).click()
        self.find_element(position_expression=popups_link).send_keys(brand_logo)
        self.find_element(position_expression=popups_link).send_keys(Keys.ENTER)
        self.find_element(position_expression=popups_choose).click()
        self.find_element(position_expression=popups_determine).click()
        return
    def category_component(self, category):
        '''
        分类选择组件
        :param category:
        :return:
        '''
        main_path = f"//div[text()='{category}']/parent::div"
        return

    # def click_add_brand(self):
    #     '''
    #     列表页点击之后跳转到新增页面
    #     :return:
    #     '''
    #     self.find_element(position_expression=self.brand_banner_add_button()).click()
    # def number (self):
    #     '''
    #     获取供应商编号
    #     :return:
    #     '''
    #     serial_number = self.find_element(position_expression=self.brand_list_id()).text
    #
    #     return serial_number
    # def click_edit_brand(self):
    #     '''
    #     列表页点击之后跳转到编辑页面
    #     :return:
    #     '''
    #
    #     self.find_element(position_expression=self.brand_list_edit_button()).click()




