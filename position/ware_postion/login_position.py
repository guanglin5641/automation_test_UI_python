class LoginPosition(object):
    @classmethod
    def input(cls, placeholder_text):
        """
        定位登录界面的用户名、密码输入框
        :param placeholder_text:
        :return:
        """
        return f"//input[@placeholder='{placeholder_text}']"

    @classmethod
    def button(cls, button_name):
        """
        定位登录界面的登录按钮
        :param button_name:
        :return:
        """
        return f"//span[text()='{button_name}']/parent::button"
