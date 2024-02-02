from page.base_page import BasePage
from position.ware_postion.left_menu_position import LeftMenuPosition
from common import route


class LeftMenuPage(BasePage, LeftMenuPosition):
    def __init__(self, driver, path=route.INDEX):
        super().__init__(driver=driver, path=path)

    def click_two_level_menu(self, menu_name):
        xpath = self.two_level_menu(menu_name)
        self.find_element(position_expression=xpath).click()
        self.wait_page_ready(5)

    def click_one_level_menu(self, menu_name):
        xpath = self.one_level_menu(menu_name)
        # 直接使用 driver.find_element 找元素的话可能会报错：no such element
        # 因此需要使用 WebDriverWait 的 util 方法
        # elm = self.driver.find_element(By.XPATH, xpath)
        self.find_element(position_expression=xpath).click()
        self.wait_page_ready(5)

    def click_supplier_list(self):
        """
        点击菜单：供应商列表
        :return:
        """
        self.click_one_level_menu("供应商")
        self.click_two_level_menu("供应商列表")
