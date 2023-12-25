import time
from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from position.supplier_position import SupplierPosition
from common.route import SUPPLIER_LIST, SUPPLIER_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json

class SupplierPage(BasePage, SupplierPosition):
    def __init__(self, driver, path=SUPPLIER_LIST):
        super().__init__(driver, path)
    def click_to_add_page(self):
        """
        列表页点击之后跳转到新增页面
        :return:
        """
        self.find_element(position_expression=self.add_button()).click()
    def click_to_edit_page(self):
        """
        列表页点击之后跳转到编辑页面
        :return:
        """
        self.find_element(position_expression=self.list_text_operation()).click()
    def click_add_button(self,data):
        """
        保存
        添加供应商
        :return:
        """
        elm = self.find_element(position_expression=self.add_button())
        self.driver.execute_script("arguments[0].click();", elm)

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(SUPPLIER_SAVE)),
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
            result = self.is_page_in_expected_state(data)  # 自定义的判断函数
            if result == "符合预期":
                return "创建成功"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def click_edit_button(self,data,number):
        """
        保存
        编辑供应商
        :return:
        """
        elm = self.find_element(position_expression=self.save_button())
        self.driver.execute_script("arguments[0].click();", elm)

        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(SUPPLIER_SAVE+"?id=" + number)),
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
            result = self.is_page_in_expected_state(data)
            if result == "符合预期":
                return "修改完成"
            else:
                return f"页面状态不符合预期: {result}"
        else:
            return ret.text
    def input_name(self, name):
        """
        输入供应商名称
        :param name:
        :return:
        """
        if not name:
            a = self.find_element(position_expression=self.name())
            a.send_keys(Keys.CONTROL + 'a')
            a.send_keys(Keys.BACKSPACE)

            return
        elif self.find_element(position_expression=self.name()) != None:
            self.find_element(position_expression=self.name()).clear()
        self.find_element(position_expression=self.name()).send_keys(name)
    def select_type(self, name):
        """
        供应商类型
        点击 input 框之后，出现下拉列表，然后再点击对应的选项
        :param name:
        :return:
        """
        if not name:
            return

        self.find_element(position_expression=self.type()).click()
        self.find_element_must_visible(
            position_expression=self.type_option(name)
        ).click()
    def get_resource_type_lists(self):
        '''
        获取资源类型数据
        :return:
        '''
        get_list = self.find_elements(position_expression=self.resource_type_lists())
        resource_type_lists= []
        for i in get_list:
            resource_type_lists.append(i.text)
        return (resource_type_lists)
    def select_resource_type(self, name):
        """
        选择资源类型
        :param name:
        :return:
        """
        all_list = self.get_resource_type_lists()
        all_dict = {item: index + 1 for index, item in enumerate(all_list)}
        for i, d_item in enumerate(all_list):

            self.find_element(position_expression=self.resource_type(d_item,all_dict)).click()
        elements = self.find_elements(position_expression=self.selected_resource_type())
        ele_len = len(elements)
        if not name:
            if elements:
                for element in range(ele_len):
                    elements[element].click()
        else:
            if elements:
                for element in range(ele_len):
                    elements[element].click()

            for i, item in enumerate(name):
                self.find_element(position_expression=self.resource_type(item,all_dict)).click()
    def input_balance_warning(self, balance):
        """
        输入余额预警
        :param balance:
        :return:
        """
        if not balance:
            a =self.find_element(position_expression=self.balance_warning())
            a.send_keys(Keys.CONTROL + 'a')
            a.send_keys(Keys.BACKSPACE)
            return
        elif self.find_element(position_expression=self.balance_warning()) != None:
            self.find_element(position_expression=self.balance_warning()).clear()
        self.find_element(position_expression=self.balance_warning()).send_keys(balance)
    def input_account_password(self, account, password):
        """
        输入供应商的账号和密码
        :param account:
        :param password:
        :return:
        """
        if not account:
            a = self.find_element(position_expression=self.account())
            a.send_keys(Keys.CONTROL + 'a')
            a.send_keys(Keys.BACKSPACE)

        elif self.find_element(position_expression=self.account()) != None:
            self.find_element(position_expression=self.account()).clear()
        self.find_element(position_expression=self.account()).send_keys(account)
        if not password:
            a = self.find_element(position_expression=self.password())
            a.send_keys(Keys.CONTROL + 'a')
            a.send_keys(Keys.BACKSPACE)
            return
        elif self.find_element(position_expression=self.password()) != None:
            self.find_element(position_expression=self.password()).clear()
        self.find_element(position_expression=self.password()).send_keys(password)
    def input_company_info(self, company_info):
        """
        输入公司信息
        :param company_info:
        :return:
        """
        if not company_info:
            company_text = self.find_element(position_expression=self.company())
            contact_text = self.find_element(position_expression=self.contact())
            contact_content_text = self.find_element(position_expression=self.contact_content())
            company_text.send_keys(Keys.CONTROL + 'a')
            company_text.send_keys(Keys.BACKSPACE)
            contact_text.send_keys(Keys.CONTROL + 'a')
            contact_text.send_keys(Keys.BACKSPACE)
            contact_content_text.send_keys(Keys.CONTROL + 'a')
            contact_text.send_keys(Keys.BACKSPACE)
            return
        if company_info["company"]:
            if self.find_element(position_expression=self.company()) != None:
                self.find_element(position_expression=self.company()).clear()
            self.find_element(position_expression=self.company()).send_keys(
                company_info["company"]
            )
        if company_info["contact"]:
            if self.find_element(position_expression=self.contact()) != None:
                self.find_element(position_expression=self.contact()).clear()
            self.find_element(position_expression=self.contact()).send_keys(
                company_info["contact"]
            )
        if company_info["contact_content"]:
            if self.find_element(position_expression=self.contact_content()) != None:
                self.find_element(position_expression=self.contact_content()).clear()
            self.find_element(position_expression=self.contact_content()).send_keys(
                company_info["contact_content"]
            )
    def select_status(self, text):
        """
        选择状态
        :param text:
        :return:
        """
        if not text:
            return

        self.find_element(position_expression=self.status(text)).click()
    def input_remark(self, text):
        """
        输入备注信息
        :param text:
        :return:
        """
        if not text:
            a = self.find_element(position_expression=self.remark())
            a.send_keys(Keys.CONTROL + 'a')
            a.send_keys(Keys.BACKSPACE)
            return
        elif self.find_element(position_expression=self.remark()) != None:
            self.find_element(position_expression=self.remark()).clear()
        self.find_element(position_expression=self.remark()).send_keys(text)
    def number (self):
        '''
        获取供应商编号
        :return:
        '''
        serial_number = self.find_element(position_expression=self.serial_number()).text
        id = serial_number.replace('编号：', '')
        return id
    def get_list_text(self):
        """
        获取列表页的文本
        :return:
        """
        name = self.find_element(position_expression=self.list_text_name())
        super_type = self.find_element(position_expression=self.list_text_super_type())
        resource_types = self.find_elements(position_expression=self.list_text_resource_types())
        contact_company = self.find_element(position_expression=self.list_text_contact_company())
        contact_information = self.find_element(position_expression=self.list_text_contact_information())
        state = self.find_element(position_expression=self.list_text_state())
        balance_warning = self.find_element(position_expression=self.list_text_balance_warning())
        create_time = self.find_element(position_expression=self.list_text_creation_time())
        remark = self.find_element(position_expression=self.list_text_remark())
        resource_type_list = []
        for i in resource_types:
            resource_type_list.append(i.text)
        return name.text,super_type.text,resource_type_list,contact_company.text,contact_information.text,state.text,balance_warning.text,create_time.text,remark.text

    def is_page_in_expected_state(self, data):
        """
        页面断言
        :return:
        """
        try:
            list = self.get_list_text()
            failed_assertions = []

            if 'name' in data and data['name']:
                if data['name'] != list[0]:
                    failed_assertions.append(
                        f"查找 'name' 不存在. 预期: {data['name']}, 实际: {list[0]}")
            if 'type' in data and data['type']:
                if data['type'] != list[1]:
                    failed_assertions.append(
                        f" 'super_type' 不存在. 预期: {data['super_type']}, 实际: {list[1]}")
            if 'resource_type' in data and data['resource_type']:
                if data['resource_type'] != list[2]:
                    failed_assertions.append(
                        f"查找 'resource_type' 不存在. 预期: {data['resource_type']}, 实际: {list[2]}")
            if 'balance_warning' in data and data['balance_warning'] :
                balance_warning = re.search(r'\d+', list[6]).group()
                if data['balance_warning'] != balance_warning:
                    failed_assertions.append(
                        f"查找 'balance_warning' 不存在. 预期: {data['balance_warning']}, 实际: {list[6]}")
            if 'company' in data[0]['company_info']['company'] and data['company_info']['company']:
                company = re.search(r'公司：(.*)', list[3]).group(1)
                if data['company_info']['company'] != company:
                    failed_assertions.append(
                        f"查找 'contact_company' 不存在. 预期: {data['company_info']['company']}, 实际: {list[3]}")
            if 'contact_content' in data[0]['company_info']['contact_content'] and data['company_info']['contact_content']:
                contact_content = re.search(r'联系方式：(.*)', list[4]).group(1)
                if data['company_info']['contact_content'] != contact_content:
                    failed_assertions.append(
                        f"查找 'contact_information' 不存在. 预期: {data['company_info']['contact_content']}, 实际: {list[4]}")
            if 'status' in data and data['status'] != None:
                if data['status'] != list[5]:
                    failed_assertions.append(
                        f"查找 'state' 不存在. 预期: {data['state']}, 实际: {list[5]}")
            if 'remark' in data and data['remark'] != None:
                if data['remark'] != list[8]:
                    failed_assertions.append(
                        f"查找 'remark' 不存在. 预期: {data['remark']}, 实际: {list[8]}")
            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)


