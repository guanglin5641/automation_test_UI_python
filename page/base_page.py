from common.config import conf
from urllib.parse import urljoin
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
)
from typing import Callable
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

from common.log import log


class BasePage(object):
    host = conf.get_by_name("host")
    logger = log

    def __init__(self, driver: WebDriver, path: str):
        self.driver = driver
        self.url = self.get_url(path)
        self.driver.get(self.url)
        # 窗口最大化
        self.driver.maximize_window()

    def get_url(self, path):
        return urljoin(self.host, path)

    def switch_default_iframe(self):
        """
        切回到主文档中，配合 switch_iframe 使用
        :return:
        """
        self.driver.switch_to.default_content()

    def switch_iframe(self, position_expression, position_type=By.XPATH, timeout=5):
        """
        切换到指定的 iframe
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """
        elm = self.find_element(
            position_expression=position_expression,
            position_type=position_type,
            timeout=timeout,
        )
        self.driver.switch_to.frame(elm)

    def switch_latest_window(self):
        """
        切换到最新的 tab/窗口
        :return:
        """
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    def upload(self, img_path, position_expression, position_type=By.XPATH, timeout=5):
        """
        当 input 为 file 类型时，上传图片就是 send_keys 图片的本地路径
        :param img_path:
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """
        elm = self.find_element(
            position_type=position_type,
            position_expression=position_expression,
            timeout=timeout,
        )
        elm.send_keys(img_path)

    def fill_element_value(
        self, value, position_expression, position_type=By.XPATH, timeout=5
    ):
        """
        给元素设置值，一般是 input 输入框
        :param value:
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """

        # 如果元素不可见，捕获异常之后，等待页面加载完成，再尝试获取一次元素
        try:
            # 获取元素
            a = time.time()
            elm = self.find_element_must_visible(
                position_expression, position_type, timeout
            )
        except (ElementNotVisibleException, Exception):
            self.wait_page_ready(timeout)
            elm = self.find_element_must_visible(
                position_expression, position_type, timeout
            )

        # 清空数据
        # elm.clear()

        if not isinstance(value, str):
            value = str(value)
        lines = value.split("\n")

        # action = ActionChains(self.driver)

        # 点击输入框，让焦点聚焦在输入框，以便输入值
        # action.click(elm)

        # for line in lines:
        #     action.send_keys(line)
        #     action.send_keys(Keys.RETURN)
        # action.perform()
        for line in lines:
            elm.send_keys(line, Keys.RETURN)

        return True

    def element_is_disappear(
        self, position_expression, position_type=By.XPATH, timeout=5
    ):
        """
        元素是否已经消失
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until_not(
                EC.presence_of_element_located((position_type, position_expression))
            )
        except TimeoutException:
            return False
        return True

    def wait_page_ready(self, timeout: int = 10):
        """
        等待页面加载完成
        :param timeout:
        :return:
        """
        start_ms = time.time() * 1000
        end_ms = start_ms + timeout * 1000
        for x in range(timeout * 10):
            # 执行 js 当页面加载成功后，会返回 complete
            ready_state = self.driver.execute_script("return document.readyState")
            if ready_state == "complete":
                return True
            if time.time() * 1000 > end_ms:
                break
            time.sleep(0.1)
        raise Exception(f"尝试等待 {timeout} 秒后，页面仍旧没有加载完成")

    def find_element_must_visible(
        self, position_expression, position_type=By.XPATH, timeout=5
    ):
        """
        元素加载到 dom 树并且必须是可见（ 宽高大于0 ）的才认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """

        def func():
            return EC.visibility_of_element_located(
                (position_type, position_expression)
            )

        try:
            return self.__find_element(func, timeout)
        except Exception:
            raise ElementNotVisibleException(
                f"元素不可见，定位方式：{position_type}，定位表达式：{position_expression}"
            )

    def find_element(self, position_expression, position_type=By.XPATH, timeout=5):
        """
        元素加载到 dom 树就认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """

        def func():
            return EC.presence_of_element_located((position_type, position_expression))

        try:
            return self.__find_element(func, timeout)
        except Exception:
            raise NoSuchElementException(
                f"元素不存在，定位方式：{position_type}，定位表达式：{position_expression}"
            )
    def find_elements(self, position_expression, position_type=By.XPATH, timeout=5):
        """
        元素加载到 dom 树就认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
        def func():
            return EC.presence_of_all_elements_located((position_type, position_expression))

        try:
            return self.__find_element(func, timeout)
        except Exception:
            raise NoSuchElementException(
                f"元素不存在，定位方式：{position_type}，定位表达式：{position_expression}"
            )
    #滑动页面加载页面所有元素
    def scroll_page(self,position_expression,position_type=By.XPATH,timeout=5):
        '''

        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        '''
        elm = self.find_element(
            position_type=position_type,
            position_expression=position_expression,
            timeout=timeout,
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", elm)
        return elm
    def __find_element(self, func: Callable, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(func())

