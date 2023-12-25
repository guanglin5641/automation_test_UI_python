import time
from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from position.brand_position import BrandPosition
from common.route import BRAND_LIST, BRAND_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json

class BrandPositionPage(BasePage, BrandPosition):
    def __init__(self, driver, path=BRAND_LIST):
        super().__init__(driver, path)
    def click_add_brand(self):
        '''
        列表页点击之后跳转到新增页面
        :return:
        '''
        self.driver.find_element(self.brand_banner_add_button).click()
    def click_brand_save_button(self):
        '''
        新增页面点击保存按钮
        :return:
        '''
        self.driver.find_element(self.brand_list_edit_button).click()

    def get_brand_list_text(self):
        '''
        获取列表页的文本内容
        :return: 包含列表页各元素文本信息的字典
        '''
        elements = {
            'brand_list_id': self.brand_list_id,
            'brand_list_name': self.brand_list_name,
            'brand_list_logo': self.brand_list_logo,
            'brand_list_main_img': self.brand_list_main_img,
            'brand_list_affiliated_company': self.brand_list_affiliated_company,
            'brand_list_main_categories': self.brand_list_main_categories,
            'brand_list_time': self.brand_list_time,
            'brand_list_sort': self.brand_list_sort,
        }

        result_dict = {
            key: self.find_element(position_expression=value()).text if key not in ['brand_list_affiliated_company',
                                                                                    'brand_list_main_categories'] else value
            for key, value in elements.items()}

        return result_dict
