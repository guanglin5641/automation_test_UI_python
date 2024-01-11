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
    def image_component(self, input_box_element,brand_logo):
        '''
        图片选择组件
        :param main:
        :param brand_logo:
        :return:
        '''
        popups_main_path = f"(//div[@class='el-dialog'])[last()]"
        popups_link = popups_main_path + f"//input[@placeholder='输入图片链接后按回车键直接添加']"
        popups_choose = f"({popups_main_path}//div[@class='el-image'])[1]"
        popups_determine = f"({popups_main_path}//button)[last()]"
        thumbnail_check = input_box_element + '//li[1]'
        thumbnail_open = input_box_element + "//div[@class='yun-img-loader__pmask']"
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
    def category_component(self,input_box_element,main_category):
        '''
        分类类目组件
        :param category:
        :return:
        '''
        main_path = f"//div[@class='el-popper is-pure is-light el-dropdown__popper cate-panel-poper']"
        one_path = f"{main_path}//section//section[1]//li/p"
        two_path = f"{main_path}//section//section[2]//li/p"
        three_path = f"{main_path}//section//section[3]//li/p"
        four_path = f"{main_path}//section//section[4]//li/p"
        self.find_element(position_expression=input_box_element).click()
        one_len = (self.find_elements(position_expression=one_path))

        for i in one_len:
            if i.text == main_category[0]:
                i.click()
                two_len = (self.find_elements(position_expression=two_path))
                for j in two_len:
                    if j.text == main_category[1]:
                        j.click()
                        three_len = (self.find_elements(position_expression=three_path))
                        for k in three_len:
                            if k.text == main_category[2]:
                                k.click()
                                four_len = (self.find_elements(position_expression=four_path))
                                for l in four_len:
                                    if l.text == main_category[3]:
                                        l.click()
                                break
                        break

        return


