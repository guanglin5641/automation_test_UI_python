class LoginPosition(object):
    @classmethod
    def login_name(cls):
        return f"//input[@placeholder='账号']"
    @classmethod
    def login_pwd(cls):
        return f"//input[@placeholder='密码']"
    @classmethod
    def login_button(cls):
        return f"//span[text()='登 录']"
    @classmethod
    def name_error(cls):
        return f"//input[@placeholder='账号']/parent::div/parent::div/parent::div//div[text()='必填']"
    @classmethod
    def pwd_error(cls):
        return f"//input[@placeholder='密码']/parent::div/parent::div/parent::div//div[text()='必填']"
    @classmethod
    def toast_error(cls):
        return f"//p[@class='el-message__content']"
    @classmethod
    def popup_error(cls):
        return f"//div[@class='el-notification__content']"