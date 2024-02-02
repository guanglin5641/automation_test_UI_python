class SupplierPosition(object):
    @classmethod
    def name(cls):
        """
        供应商名称
        :return:
        """
        return f"//label[text()='供应商名称']/parent::div//input"

    @classmethod
    def type(cls):
        """
        供应商类型
        :return:
        """
        return f"//input[@placeholder='请选择供应商类型']/parent::div"

    @classmethod
    def resource_type(cls, text):
        d = {"虚拟商品": 1, "实物商品": 2, "CPS": 3, "CPA": 4, "话费": 5}
        index = 1
        if text in d:
            index = d[text]
        return f"//label[text()='资源类型']/following-sibling::div//label[{index}]"

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
