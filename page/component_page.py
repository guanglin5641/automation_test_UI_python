import time
from page.base_page import BasePage
from common.route import BRAND_LIST
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ComponentPage(BasePage, object):
    def __init__(self, driver, path=BRAND_LIST):
        super().__init__(driver, path)

    def image_component(self, main_path, image_link):
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
        thumbnail_check = main_path + '//li[1]'
        thumbnail_open = main_path + "//div[@class='yun-img-loader__pmask']"
        try:
            WebDriverWait(self.driver, 1).until(
                EC.any_of(EC.visibility_of_element_located((By.XPATH, thumbnail_check))))

            a = 1
        except:

            a = 0

        if not image_link:
            if a == 1:
                self.find_element(position_expression=thumbnail_check).click()
                self.find_element(position_expression=thumbnail_check).send_keys(Keys.BACKSPACE)

                return
            return
        if a == 1:
            self.find_element(position_expression=thumbnail_check).click()
            self.find_element(position_expression=thumbnail_check).send_keys(Keys.BACKSPACE)
        self.find_element(position_expression=thumbnail_open).click()
        self.find_element(position_expression=popups_link).send_keys(image_link)
        self.find_element(position_expression=popups_link).send_keys(Keys.ENTER)
        self.find_element(position_expression=popups_choose).click()
        self.find_element(position_expression=popups_determine).click()
        return
    def image_components(self, main_path, image_link):
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
        thumbnail_check = main_path + '//li'
        thumbnail_open = main_path + "//div[@class='yun-img-loader__pmask']"
        try:
            WebDriverWait(self.driver, 1).until(
                EC.any_of(EC.visibility_of_element_located((By.XPATH, thumbnail_check))))

            a = 1
        except:

            a = 0
        if not image_link:
            if a == 1:
                b = self.find_elements(position_expression=thumbnail_check)
                for i in b:
                    i.click()
                    i.send_keys(Keys.BACKSPACE)
                    time.sleep(0.5)
                return
            return
        if a == 1:
            b = self.find_elements(position_expression=thumbnail_check)
            for i in b:
                i.click()
                i.send_keys(Keys.BACKSPACE)
                time.sleep(0.5)
        for c in image_link:
            self.find_element(position_expression=thumbnail_open).click()
            self.find_element(position_expression=popups_link).send_keys(c)
            self.find_element(position_expression=popups_link).send_keys(Keys.ENTER)
            self.find_element(position_expression=popups_choose).click()
            self.find_element(position_expression=popups_determine).click()
        return
    def category_component(self, input_box_element, main_category):
        '''
        分类类目组件
        :param category:
        :return:
        '''
        main_path = f"//div[@class='el-popper is-pure is-light el-dropdown__popper cate-panel-poper']"
        path = []
        for i in range(len(main_category)):
            path.append(f"{main_path}//section//section[{i+1}]//li/p")
        self.find_element(position_expression=input_box_element).click()
        for i in range(len(path)):

            one_len = (self.find_elements(position_expression=f"{main_path}//section//section[{i+1}]//li/p"))
            for y in one_len:
                if y.text == main_category[i]:
                    y.click()
                else:
                    break