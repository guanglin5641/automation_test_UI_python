import time
from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from position.ware_postion.brand_position import BrandPosition
from common.route import BRAND_LIST, BRAND_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json


from page.component_page import ComponentPage
class BrandPositionPage(ComponentPage, BrandPosition, BasePage):
    def __init__(self, driver, path=BRAND_LIST):
        super().__init__(driver, path)
    def get_brand_list_text(self):
        '''
        获取列表页的文本内容
        :return: 包含列表页各元素文本信息的字典
        '''
        brand_list_id = self.find_element(position_expression=self.brand_list_id()).text
        brand_list_name = self.find_element(position_expression=self.brand_list_name()).text
        brand_list_logo = self.find_element(position_expression=self.brand_list_logo()).get_attribute('src')
        brand_list_main_img = self.find_element(position_expression=self.brand_list_main_img())
        img_tags = brand_list_main_img.find_elements(By.TAG_NAME, 'img')
        if img_tags:
            # 如果存在图片，返回图片的 src 属性
            brand_list_main_imgs = img_tags[0].get_attribute('src')
        else:
            # 否则返回元素内部的文本内容
            brand_list_main_imgs = brand_list_main_img.text
        brand_list_affiliated_company = self.find_element(position_expression=self.brand_list_affiliated_company()).text
        brand_list_main_categories = self.find_element(position_expression=self.brand_list_main_categories()).text
        brand_list_time = self.find_element(position_expression=self.brand_list_time()).text
        brand_list_sort = self.find_element(position_expression=self.brand_list_sort()).text


        return brand_list_name,brand_list_logo,brand_list_main_imgs,brand_list_affiliated_company,brand_list_main_categories,brand_list_time,brand_list_sort,brand_list_id
    def click_add_brand(self):
        '''
        列表页点击之后跳转到新增页面
        :return:
        '''
        self.find_element(position_expression=self.brand_banner_add_button()).click()
    def click_edit_brand(self):
        '''
        列表页点击之后跳转到编辑页面
        :return:
        '''

        self.find_element(position_expression=self.brand_list_edit_button()).click()

    def enter_brand_name(self, brand_name):
        '''
        输入品牌名称
        :param brand_name:
        :return:
        '''
        if not brand_name:
            self.find_element(position_expression=self.brand_edit_name()).send_keys(Keys.CONTROL+"a")
            self.find_element(position_expression=self.brand_edit_name()).send_keys(Keys.BACKSPACE)
            return
        self.find_element(position_expression=self.brand_edit_name()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_name()).send_keys(Keys.BACKSPACE)
        self.find_element(position_expression=self.brand_edit_name()).send_keys(brand_name)
    def enter_brand_status(self, brand_status):
        '''
        输入品牌状态
        :param brand_status:
        :return:
        '''
        if not brand_status:
            return
        brand_status_text = self.find_element(position_expression=self.brand_edit_status_text()).text
        if brand_status_text == brand_status:
            return
        self.find_element(position_expression=self.brand_edit_status()).click()
    # def enter_brand_logo(self, brand_logo):
    #     '''
    #     输入品牌logo
    #     :param brand_logo:
    #     :return:
    #     '''
    #     try:
    #         WebDriverWait(self.driver, 1).until(
    #             EC.any_of(EC.visibility_of_element_located((By.XPATH, self.brand_edit_logo_cls()))))
    #         a = 1
    #     except:
    #         a = 0
    #
    #     if not brand_logo:
    #         if a == 1:
    #             self.find_element(position_expression=self.brand_edit_logo_cls()).click()
    #             operate = self.find_element(position_expression=self.brand_edit_logo_cls())
    #             operate.send_keys(Keys.BACKSPACE)
    #             return
    #         return
    #     if a == 1:
    #         self.find_element(position_expression=self.brand_edit_logo_cls()).click()
    #         operate = self.find_element(position_expression=self.brand_edit_logo_cls())
    #         operate.send_keys(Keys.BACKSPACE)
    #     self.find_element(position_expression=self.brand_edit_logo()).click()
    #     self.find_element(position_expression=self.brand_edit_logo_upload_button()).send_keys(brand_logo)
    #     self.find_element(position_expression=self.brand_edit_logo_choose()).click()
    #     logo_link = self.find_element(position_expression=self.brand_edit_logo_choose()).get_attribute('src')
    #     self.find_element(position_expression=self.brand_edit_logo_fix_button()).click()
    #     return logo_link
    def enter_brand_logo(self,brand_logo):

        self.image_component(self.brand_edit_logo_cls(),brand_logo)
        return
    def enter_brand_main_img(self,brand_main_img):
        self.image_component(self.brand_edit_main_img_cls(),brand_main_img)
        return

    # def enter_brand_main_img(self, brand_main_img):
    #     '''
    #     输入品牌主图
    #     :param brand_main_img:
    #     :return:
    #     '''
    #     try:
    #         WebDriverWait(self.driver, 1).until(
    #             EC.any_of(EC.visibility_of_element_located((By.XPATH, self.brand_edit_main_img_cls()))))
    #         a = 1
    #     except:
    #         a = 0
    #     if not brand_main_img:
    #         if a == 1:
    #             self.find_element(position_expression=self.brand_edit_main_img_cls()).click()
    #             operate = self.find_element(position_expression=self.brand_edit_main_img_cls())
    #             operate.send_keys(Keys.BACKSPACE)
    #             # print("元素可见")
    #             return
    #         return
    #     if a == 1:
    #         self.find_element(position_expression=self.brand_edit_main_img_cls()).click()
    #         operate = self.find_element(position_expression=self.brand_edit_main_img_cls())
    #         operate.send_keys(Keys.BACKSPACE)
    #     self.find_element(position_expression=self.brand_edit_main_img()).click()
    #     self.find_element(position_expression=self.brand_edit_main_img_upload_button()).send_keys(
    #         brand_main_img)
    #     self.find_element(position_expression=self.brand_edit_main_img_choose()).click()
    #     main_img_link = self.find_element(position_expression=self.brand_edit_main_img_choose()).get_attribute(
    #         'src')
    #     self.find_element(position_expression=self.brand_edit_main_img_fix_button()).click()
    #     return main_img_link
    def enter_brand_main_categories(self,main_categories):
        '''
        主营类目
        :param main_categories:
        :return:
        '''
        if not main_categories:
            return
        self.category_component(self.brand_edit_main_categories(),main_categories)

    # def enter_brand_main_categories(self,main_categories):
    #     '''
    #     输入品牌主分类
    #     :param main_categories:
    #     :return:
    #     '''
    #     if not main_categories:
    #
    #         return
    #     self.find_element(position_expression=self.brand_edit_main_categories()).click()
    #     self.scroll_page(position_expression=self.brand_edit_alias())
    #     self.find_element(position_expression=self.brand_edit_main_categories_select_box_one_click()).click()

    def enter_brand_alias(self,alias):
        '''
        输入品牌别名
        :param alias:
        :return:
        '''
        if not alias:
            self.find_element(position_expression=self.brand_edit_alias()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_alias()).clear()

            return
        self.scroll_page(position_expression=self.brand_edit_alias())
        self.find_element(position_expression=self.brand_edit_alias()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_alias()).clear()
        self.find_element(position_expression=self.brand_edit_alias()).send_keys(alias)
    def enter_brand_english_name(self,english_name):
        '''
        输入品牌英文名
        :param english_name:
        :return:
        '''
        if not english_name:
            self.find_element(position_expression=self.brand_edit_english_name()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_english_name()).clear()

            return
        self.scroll_page(position_expression=self.brand_edit_english_name())
        self.find_element(position_expression=self.brand_edit_english_name()).clear()

        self.find_element(position_expression=self.brand_edit_english_name()).send_keys(english_name)
    def enter_brand_consumer_group(self,consumer_group):
        '''
        输入品牌消费组
        :param consumer_group:
        :return:
        '''
        if not consumer_group:
            self.find_element(position_expression=self.brand_edit_consumer_group()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_consumer_group()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_consumer_group())
        self.find_element(position_expression=self.brand_edit_consumer_group()).clear()

        self.find_element(position_expression=self.brand_edit_consumer_group()).send_keys(consumer_group)
    def enter_brand_brand_positioning(self,brand_positioning):
        '''
        输入品牌位置
        :param brand_positioning:
        :return:
        '''
        if not brand_positioning:
            self.find_element(position_expression=self.brand_edit_brand_positioning()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_brand_positioning()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_brand_positioning())
        self.find_element(position_expression=self.brand_edit_brand_positioning()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_brand_positioning()).clear()
        self.find_element(position_expression=self.brand_edit_brand_positioning()).send_keys(brand_positioning)
    def enter_brand_sort(self,sort):
        '''
        输入品牌排序
        :param sort:
        :return:
        '''
        if not sort:
            self.find_element(position_expression=self.brand_edit_sort()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_sort()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_sort())
        self.find_element(position_expression=self.brand_edit_sort()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_sort()).clear()
        self.find_element(position_expression=self.brand_edit_sort()).send_keys(sort)
    def enter_brand_establishment_time(self,establishment_time):
        '''
        输入品牌成立时间
        :param establishment_time:
        :return:
        '''
        if not establishment_time:
            self.find_element(position_expression=self.brand_edit_establishment_time()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_establishment_time()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_establishment_time())
        self.find_element(position_expression=self.brand_edit_establishment_time()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_establishment_time()).clear()
        self.find_element(position_expression=self.brand_edit_establishment_time()).send_keys(establishment_time)
    def enter_brand_origin(self,origin):
        '''
        输入品牌来源
        :param origin:
        :return:
        '''
        if not origin:
            self.find_element(position_expression=self.brand_edit_origin()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_origin()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_origin())
        self.find_element(position_expression=self.brand_edit_origin()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_origin()).clear()
        self.find_element(position_expression=self.brand_edit_origin()).send_keys(origin)
    def enter_brand_affiliated_company(self,affiliated_company):
        '''
        输入品牌所属公司
        :param affiliated_company:
        :return:
        '''
        if not affiliated_company:
            self.find_element(position_expression=self.brand_edit_affiliated_company()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_affiliated_company()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_affiliated_company())
        self.find_element(position_expression=self.brand_edit_affiliated_company()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_affiliated_company()).clear()
        self.find_element(position_expression=self.brand_edit_affiliated_company()).send_keys(affiliated_company)
    def enter_brand_remark(self,remark):
        '''
        输入品牌备注
        :param remark:
        :return:
        '''
        if not remark:
            self.find_element(position_expression=self.brand_edit_remark()).send_keys(Keys.CONTROL + "a")
            self.find_element(position_expression=self.brand_edit_remark()).clear()
            return
        self.scroll_page(position_expression=self.brand_edit_remark())
        self.find_element(position_expression=self.brand_edit_remark()).send_keys(Keys.CONTROL + "a")
        self.find_element(position_expression=self.brand_edit_remark()).clear()
        self.find_element(position_expression=self.brand_edit_remark()).send_keys(remark)
    def click_brand_save_button(self,data):
        '''
        新增页面点击保存按钮
        :return:
        '''
        elm = self.find_element(position_expression=self.brand_button_edit_add())
        self.driver.execute_script("arguments[0].click();", elm)
        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(BRAND_SAVE)),
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='el-form-item__error']")
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-message__content']")

                ),
            )
        )
        if isinstance(ret, bool):
            # 添加你的额外判断条件
            # return "创建成功"
            result = self.brand_is_page_in_expected_state(data)  # 自定义的判断函数
            if result == "符合预期":
                return "添加品牌成功"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def click_edit_button(self,data,number):
        """
        保存
        编辑供应商
        :param number:
        :param logo:
        :return:
        """
        elm = self.find_element(position_expression=self.brand_button_edit_submit())
        self.driver.execute_script("arguments[0].click();", elm)

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(BRAND_SAVE +"?id=" + number)),
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='el-form-item__error']")
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-message__content']")

                ),
            )
        )
        # 如果页面发生跳转，就说明创建供应商成功
        if isinstance(ret, bool):
            # 添加你的额外判断条件
            # return "创建成功"
            result = self.brand_is_page_in_expected_state(data)
            if result == "符合预期":
                return "修改完成"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def click_brand_cancel_button(self):
        '''
        新增页面点击取消按钮
        :return:
        '''

        self.find_element(position_expression=self.click_brand_cancel_button()).click()
    def number (self):
        '''
        获取供应商编号
        :return:
        '''
        serial_number = self.find_element(position_expression=self.brand_list_id()).text

        return serial_number
    def brand_is_page_in_expected_state(self,brand_data):
        '''
        页面断言
        :param data:
        :return:
        '''
        try:
            list = self.get_brand_list_text()
            failed_assertions = []
            if 'brand_name' in brand_data and brand_data['brand_name']:
                # print(11)
                if brand_data['brand_name'] != list[0]:
                    failed_assertions.append(
                        f"查找 'name' 不存在. 预期: {brand_data['brand_name']}, 实际: {list[0]}")
            if 'brand_logo' in brand_data and brand_data['brand_logo']:
                # print(2)
                if brand_data['brand_logo'] != list[1]:
                    failed_assertions.append(
                        f"查找 'logo' 不存在. 预期: {brand_data['brand_logo']}, 实际: {list[1]}")
            if 'brand_main_img' in brand_data and brand_data['brand_main_img']:
                # print(3)
                if brand_data['brand_main_img'] != list[2]:
                    failed_assertions.append(
                        f"查找 'main_img' 不存在. 预期: {brand_data['brand_main_img']}, 实际: {list[2]}")
            if 'affiliated_company' in brand_data and brand_data['affiliated_company']:
                # print(4)
                if brand_data['affiliated_company'] != list[3]:
                    failed_assertions.append(
                        f"查找 'affiliated_company' 不存在. 预期: {brand_data['affiliated_company']}, 实际: {list[3]}")
            if 'establishment_time' in brand_data and brand_data['establishment_time']:
                # print(5)
                if brand_data['establishment_time'] != list[5]:
                    failed_assertions.append(
                        f"查找 'establishment_time' 不存在. 预期: {brand_data['establishment_time']}, 实际: {list[5]}")
            if 'sort' in brand_data and brand_data['sort']:
                # print(6)
                if brand_data['sort'] != list[6]:
                    failed_assertions.append(
                        f"查找 'sort' 不存在. 预期: {brand_data['sort']}, 实际: {list[6]}")
            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)





