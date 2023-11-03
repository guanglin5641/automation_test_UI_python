from page.base_page import BasePage
from position.ware_postion.category_position import CategoryPosition
from common.route import CATEGORY_LIST, CATEGORY_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# import mysql.connector



class CategoryPositionPage(BasePage, CategoryPosition):
    def __init__(self, driver, path=CATEGORY_LIST):
        super().__init__(driver, path)
    def get_category_list_text(self):
        '''
        获取列表页的文本内容
        :return: 包含列表页各元素文本信息的字典
        '''
        category_list_id = self.find_element(position_expression=self.category_list_id()).text
        category_list_name = self.find_element(position_expression=self.category_list_name()).text
        category_list_logo = self.find_element(position_expression=self.category_list_logo()).get_attribute('src')
        category_list_create_time = self.find_element(position_expression=self.category_list_create_time()).text
        category_list_update_time = self.find_element(position_expression=self.category_list_update_time()).text
        return category_list_name, category_list_logo, category_list_id, category_list_create_time, category_list_update_time
    def click_add_category(self):
        '''
        列表页点击之后跳转到新增页面
        :return:
        '''
        self.find_element(position_expression=self.category_banner_add_button()).click()
    def click_edit_category(self):
        '''
        列表页点击之后跳转到编辑页面
        :return:
        '''

        self.find_element(position_expression=self.category_list_edit_button()).click()



    def enter_category_name(self, category_name):
        '''
        输入类目名称
        :param category_name:
        :return:
        '''
        if not category_name:
            self.find_element(position_expression=self.category_edit_name()).send_keys(Keys.CONTROL+"a")
            self.find_element(position_expression=self.category_edit_name()).send_keys(Keys.BACKSPACE)
            return
        elif self.find_element(position_expression=self.category_edit_name()) != None:
            self.find_element(position_expression=self.category_edit_name()).clear()

        self.find_element(position_expression=self.category_edit_name()).click()
        self.find_element(position_expression=self.category_edit_name()).send_keys(category_name)


    def enter_category_status(self, category_status):
        '''
        输入类目状态
        :param category_status:
        :return:
        '''
        if not category_status:
            return
        category_status_text = self.find_element(position_expression=self.category_edit_status_text()).text
        if category_status_text == category_status:
            return
        self.find_element(position_expression=self.category_edit_status()).click()
    def enter_category_logo(self, category_logo):
        '''
        输入类目logo
        :param  category_logo:
        :return:
        '''
        try:
            WebDriverWait(self.driver, 1).until(
                EC.any_of(EC.visibility_of_element_located((By.XPATH, self.category_edit_logo_cls()))))
            a = 1
        except:
            a = 0

        if not category_logo:
            if a == 1:
                self.find_element(position_expression=self.category_edit_logo_cls()).click()
                operate = self.find_element(position_expression=self.category_edit_logo_cls())
                operate.send_keys(Keys.BACKSPACE)
                return
            return
        if a == 1:
            self.find_element(position_expression=self.category_edit_logo_cls()).click()
            operate = self.find_element(position_expression=self.category_edit_logo_cls())
            operate.send_keys(Keys.BACKSPACE)
        self.find_element(position_expression=self.category_edit_logo()).click()
        print(category_logo)
        self.find_element(position_expression=self.category_edit_logo_upload_button()).send_keys(category_logo)
        self.find_element(position_expression=self.category_edit_logo_choose()).click()
        logo_link = self.find_element(position_expression=self.category_edit_logo_choose()).get_attribute('src')
        self.find_element(position_expression=self.category_edit_logo_fix_button()).click()
        return logo_link



    def category_number (self):
        '''
        获取类目编号
        :return:
        '''
        category_serial_number = self.find_element(position_expression=self.category_list_id()).text

        return category_serial_number


    def click_category_save_button(self,data,logo):
        '''
        新增页面点击保存按钮
        :return:
        '''
        elm = self.find_element(position_expression=self.category_button_edit_add())
        self.driver.execute_script("arguments[0].click();", elm)
        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(CATEGORY_SAVE)),
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='el-form-item__error']")
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-message__content']")

                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-notification__content']")

                ),
            )
        )
        if isinstance(ret, bool):
            # 添加你的额外判断条件
            # return "创建成功"
            result = self.category_is_page_in_expected_state(data,logo)  # 自定义的判断函数
            if result == "符合预期":
                return "添加类目成功"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def click_edit_button(self,data,number,logo):
        """
        保存
        编辑类目
        :param number:
        :param logo:
        :return:
        """
        elm = self.find_element(position_expression=self.category_button_edit_submit()) #不理解
        self.driver.execute_script("arguments[0].click();", elm)

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(CATEGORY_SAVE +"?id=" + number)),
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
            result = self.category_is_page_in_expected_state(data,logo)
            if result == "符合预期":
                return "修改完成"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def click_category_cancel_button(self):
        '''
        新增页面点击取消按钮
        :return:
        '''

        self.find_element(position_expression=self.click_category_cancel_button()).click()

    def category_is_page_in_expected_state(self,category_data,logo):
        '''
        页面断言
        :param data:
        :return:
        '''
        try:
            list = self.get_category_list_text()
            failed_assertions = []


            if 'category_name' in category_data and category_data['category_name']:
                # print(11)
                if category_data['category_name'] != list[0]:
                    failed_assertions.append(
                        f"查找 'name' 不存在. 预期: {category_data['category_name']}, 实际: {list[0]}")



            if 'category_logo' in category_data and category_data['category_logo']:
                # print(2)
                if logo != list[1]:
                    failed_assertions.append(
                        f"查找 'logo' 不存在. 预期: {logo}, 实际: {logo}")


            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)




