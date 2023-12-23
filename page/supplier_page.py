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
                return "修改成功"
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
            print("aaaaaa")
            self.find_element(position_expression=self.balance_warning()).clear()
            # self.find_element(position_expression=self.balance_warning()).send_keys(balance)
        print(11111)
        self.find_element(position_expression=self.balance_warning()).send_keys(balance)

    def input_account_password(self, account, password):
        """
        输入供应商的账号和密码
        :param account:
        :param password:
        :return:
        """
        if account:
            self.find_element(position_expression=self.account()).send_keys(account)
        if password:
            self.find_element(position_expression=self.password()).send_keys(password)

    def input_company_info(self, company_info):
        """
        输入公司信息
        :param company_info:
        :return:
        """
        if not company_info:
            return
        if company_info["company"]:
            self.find_element(position_expression=self.company()).send_keys(
                company_info["company"]
            )
        if company_info["contact"]:
            self.find_element(position_expression=self.contact()).send_keys(
                company_info["contact"]
            )
        if company_info["contact_content"]:
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
            return
        self.find_element(position_expression=self.remark()).send_keys(text)

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

            # 只对在 data 中有值的字段进行断言
            # 如果 data['name'] 不为空且不是字符串 "null"

            if 'name' in data and data['name']:
                if data['name'] != list[0]:
                    failed_assertions.append(
                        f"查找 'name' 不存在. 预期: {data['name']}, 实际: {list[0]}")
            if 'super_type' in data and data['super_type']:
                if data['super_type'] != list[1]:
                    failed_assertions.append(
                        f" 'super_type' 不存在. 预期: {data['super_type']}, 实际: {list[1]}")

            if 'resource_type' in data and data['resource_type']:
                if data['resource_type'] != list[2]:
                    failed_assertions.append(
                        f"查找 'resource_type' 不存在. 预期: {data['resource_type']}, 实际: {list[2]}")

            if 'contact_company' in data and data['contact_company']:
                if data['contact_company'] != list[3]:
                    failed_assertions.append(
                        f"查找 'contact_company' 不存在. 预期: {data['contact_company']}, 实际: {list[3]}")

            if 'contact_information' in data and data['contact_information']:
                if data['contact_information'] != list[4]:
                    failed_assertions.append(
                        f"查找 'contact_information' 不存在. 预期: {data['contact_information']}, 实际: {list[4]}")

            if 'state' in data and data['state']:
                if data['state'] != list[5]:
                    failed_assertions.append(
                        f"查找 'state' 不存在. 预期: {data['state']}, 实际: {list[5]}")

            if 'balance_warning' in data and data['balance_warning']:
                balance_warning = re.search(r'\d+', list[6]).group()
                print(balance_warning)
                if data['balance_warning'] != balance_warning:
                    failed_assertions.append(
                        f"查找 'balance_warning' 不存在. 预期: {data['balance_warning']}, 实际: {list[6]}")

            if 'create_time' in data and data['create_time']:
                if data['create_time'] != list[7]:
                    failed_assertions.append(
                        f"查找 'create_time' 不存在. 预期: {data['create_time']}, 实际: {list[7]}")

            if 'remark' in data and data['remark']:
                if data['remark'] != list[8]:
                    failed_assertions.append(
                        f"查找 'remark' 不存在. 预期: {data['remark']}, 实际: {list[8]}")

            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)
    def number (self):
        serial_number = self.find_element(position_expression=self.serial_number()).text
        id = serial_number.replace('编号：', '')
        return id
    def get_resource_type_lists(self):
        get_list = self.find_elements(position_expression=self.resource_type_lists())
        resource_type_lists= []
        for i in get_list:
            resource_type_lists.append(i.text)
        return (resource_type_lists)




if __name__ == '__main__':
    a = "¥10\n"
    b = re.search(r'\d+',a).group()
    print(b)


