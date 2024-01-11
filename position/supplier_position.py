class SupplierPosition(object):
    @classmethod
    def name(cls):
        """
        供应商名称
        :return:
        """
        return f"//label[text()='供应商名称']/parent::div//input"
    def nm(cls):

        return f'''//*[@id="app"]/div/section/main/div/section/button/span'''
    @classmethod
    def type(cls):
        """
        供应商类型
        :return:
        """
        return f"//input[@placeholder='请选择供应商类型']/parent::div"

    @classmethod
    def resource_type(cls, text,all_list):

        if text in all_list:
            index = all_list[text]
        return f"//label[text()='资源类型']/following-sibling::div//label[{index}]"
    @classmethod
    def selected_resource_type(self):

        return f"//div[@class='el-checkbox-group']//label[@class='el-checkbox is-checked']"

    @classmethod
    def type_option(cls, type_name):
        """
        选择供应商类型
        :param type_name:
        :return:
        """
        return f"//span[text()='{type_name}']/parent::li"

    @classmethod
    def balance_warning(cls):
        return f"//label[text()='账号余额预警值']/parent::div//input"

    @classmethod
    def account(cls):
        return f"//label[text()='云仓供应商后台账号']/parent::div//input"

    @classmethod
    def password(cls):
        return f"//label[text()='云仓供应商后台密码']/parent::div//input"

    @classmethod
    def company(cls):
        return f"//label[text()='所属公司']/parent::div//input"

    @classmethod
    def contact(cls):
        return f"//label[text()='联系人']/parent::div//input"

    @classmethod
    def contact_content(cls):
        return f"//label[text()='联系方式']/parent::div//input"

    @classmethod
    def status(cls, status_text):
        return f"//span[text()='{status_text}']"

    @classmethod
    def remark(cls):
        return f"//label[text()='备注']/parent::div//textarea"

    @classmethod
    def add_button(cls):
        return f"//span[text()='新增']/parent::button"
    @classmethod
    def list_text_name(cls):
        '''
        供应商名称
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][1]//p[@class='font-semibold']'''

    @classmethod
    def list_text_super_type(cls):
        '''
        供应商类型
        '''
        return f'''//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[2]/div'''
    @classmethod
    def list_text_resource_types(cls):
        '''
        资源类型(多项)
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][1]//span[@class='el-tag__content']'''
    @classmethod
    def list_text_contact_company(cls):
        '''
        联系公司
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][3]//p[1]'''
    @classmethod
    def list_text_contact_information(cls):
        '''
        联系人
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][3]//p[2]'''
    @classmethod
    def list_text_state(cls):
        '''
        状态
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][4]//span[@class="el-tag__content"]'''
    @classmethod
    def list_text_balance_warning(cls):
        '''
        账号余额预警值
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][5]//span[@class='el-text']'''
    @classmethod
    def list_text_creation_time(cls):
        '''
        创建时间
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][6]//div'''
    @classmethod
    def list_text_remark(cls):
        '''
        备注
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][7]//div'''
    @classmethod
    def list_text_operation(cls):
        '''
        操作编辑
        '''
        return f'''//tr[@class='el-table__row'][1]//td[@class][8]//span[1]'''

    def save_button(cls):
        '''
        操作编辑
        :return:
        '''
        return f'''//span[text()='保存']/parent::button'''
    def cancel_button(cls):
        '''
        操作编辑
        :return:
        '''
        return f'''//span[text()='取消']/parent::button'''
    def serial_number(cls):
        '''
        查找编号
        :return:
        '''
        return f'''//tr[@class='el-table__row'][1]//p[contains(text(), '编号：')]'''
    def resource_type_lists(cls):
        return  f'''//div[@class='el-checkbox-group']//span[@class='el-checkbox__label']'''
