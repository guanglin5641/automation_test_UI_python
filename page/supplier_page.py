import time

from page.base_page import BasePage
from position.supplier_position import SupplierPosition
from common.route import SUPPLIER_LIST, SUPPLIER_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
                # EC.url_changes(self.get_url(SUPPLIER_SAVE)),
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
            print(ret.text)
            return ret.text



    def input_name(self, name):
        """
        输入供应商名称
        :param name:
        :return:
        """
        if not name:
            return

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
        if not name:
            return

        self.find_element(position_expression=self.resource_type(name)).click()

    def input_balance_warning(self, balance):
        """
        输入余额预警
        :param balance:
        :return:
        """
        if not balance:
            return

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
        failed_assertions = []

        try:
            list = self.get_list_text()

            # 只对在 data 中有值的字段进行断言
            if 'name' in data and data['name']:
                if data['name'] != list[0]:
                    failed_assertions.append(f"Field 'name' is incorrect. Expected: {data['name']}, Actual: {list[0]}")
            if 'super_type' in data and data['super_type']:
                if data['super_type'] != list[1]:
                    failed_assertions.append(
                        f"Field 'super_type' is incorrect. Expected: {data['super_type']}, Actual: {list[1]}")
            if 'resource_type' in data and data['resource_type']:
                if data['resource_type'] != list[2]:
                    failed_assertions.append(
                        f"Field 'resource_type' is incorrect. Expected: {data['resource_type']}, Actual: {list[2]}")
            if 'contact_company' in data and data['contact_company']:
                if data['contact_company'] != list[3]:
                    failed_assertions.append(
                        f"Field 'contact_company' is incorrect. Expected: {data['contact_company']}, Actual: {list[3]}")
            if 'contact_information' in data and data['contact_information']:
                if data['contact_information'] != list[4]:
                    failed_assertions.append(
                        f"Field 'contact_information' is incorrect. Expected: {data['contact_information']}, Actual: {list[4]}")
            if 'state' in data and data['state']:
                if data['state'] != list[5]:
                    failed_assertions.append(
                        f"Field 'state' is incorrect. Expected: {data['state']}, Actual: {list[5]}")
            if 'balance_warning' in data and data['balance_warning']:
                if data['balance_warning'] != list[6]:
                    failed_assertions.append(
                        f"Field 'balance_warning' is incorrect. Expected: {data['balance_warning']}, Actual: {list[6]}")
            if 'create_time' in data and data['create_time']:
                if data['create_time'] != list[7]:
                    failed_assertions.append(
                        f"Field 'create_time' is incorrect. Expected: {data['create_time']}, Actual: {list[7]}")
            if 'remark' in data and data['remark']:
                if data['remark'] != list[8]:
                    failed_assertions.append(
                        f"Field 'remark' is incorrect. Expected: {data['remark']}, Actual: {list[8]}")
            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)
