class LeftMenuPosition(object):
    @classmethod
    def one_level_menu(cls, menu_name):
        """
        一级菜单定位
        :param menu_name:
        :return:
        """

        return f"//div[@class='el-sub-menu__title']/span[text()='{menu_name}']/ancestor::li[@class='el-sub-menu']"

    @classmethod
    def two_level_menu(cls, menu_name):
        """
        二级菜单定位
        :param menu_name:
        :return:
        """
        return f"//span[text()='{menu_name}']/parent::li"
