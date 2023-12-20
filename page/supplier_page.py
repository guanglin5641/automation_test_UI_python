import time

from page.base_page import BasePage
from position.supplier_position import SupplierPosition
from common.route import SUPPLIER_LIST, SUPPLIER_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def click_add_button(self):
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
        # 如果页面发生跳转就说明创建供应商成功
        if isinstance(ret, bool):
            return "创建成功"
        else:
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
    def page_assertion(self,name,super_type,resource_types,contact_company,contact_information,state,balance_warning,create_time,remark):
        """
        页面断言
        :return:
        """
        try:
            list = self.get_list_text()
            assert name == list[0]
            assert super_type == list[1]
            assert resource_types == list[2]
            assert contact_company == list[3]
            assert contact_information == list[4]
            assert state == list[5]
            assert balance_warning == list[6]
            assert create_time == list[7]
            assert remark == list[8]
            return "All assertions passed."

        except AssertionError as e:
            return str(e)


if __name__ == '__main__':

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))