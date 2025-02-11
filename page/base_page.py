from common.config import conf
from urllib.parse import urljoin
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait , TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
	NoSuchElementException ,
	ElementNotVisibleException ,
	)
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.common.exceptions import NoAlertPresentException
from common.log import log
from selenium.webdriver.common.alert import Alert
from typing import List , Callable , Optional
import re
import os
from selenium.webdriver.remote.webdriver import WebDriver
from urllib.parse import urljoin
import logging
from common.decorators import wait_all_methods


@wait_all_methods
class BasePage :
	def __init__(self , driver: WebDriver , path: str , project: str) :
		self.driver = driver
		self.project_host = conf.get_by_name(f"{project}.host")
		self.project_url = urljoin(self.project_host , path)
		self.logger = logging.getLogger(__name__)
		
		# 获取当前用例名称
		test_case_name = getattr(driver , "current_test_case" , None)
		
		# 如果当前用例变了，才允许打开页面
		if test_case_name is None or test_case_name != driver.current_test_case :
			if driver.current_test_case is None :
				driver.current_test_case = 0
			else :
				driver.current_test_case += 1  # 先更新当前用例
			self.logger.info(f"当前用例 [{test_case_name}] 打开页面: {self.project_url}")
			driver.get(self.project_url)
			self.pop_ups()
			driver.maximize_window()
		else :
			self.logger.info(f"当前用例 [{test_case_name}] 已打开页面，不重复打开")
	
	def pop_ups(self) :
		try :
			alert = Alert(self.driver)
			# 获取警告弹窗的文本内容
			alert_text = alert.text
			# 打印警告弹窗的文本内容
			self.logger.info(f"系统报错弹窗: {alert_text}")
			# 可以根据具体情况执行相应的操作，比如确认警告弹窗
			alert.accept()  # 确认警告弹窗
		except NoAlertPresentException :
			pass
		return
	
	def get_url(self , path) :
		return urljoin(self.project_host , path)
	
	def switch_default_iframe(self) :
		"""
        切回到主文档中，配合 switch_iframe 使用
        :return:
        """
		self.driver.switch_to.default_content()
	
	def switch_iframe(self , position_expression , position_type=By.XPATH , timeout=5) :
		"""
        切换到指定的 iframe
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """
		elm = self.find_element(
			position_expression=position_expression ,
			position_type=position_type ,
			timeout=timeout ,
			)
		self.driver.switch_to.frame(elm)
	
	def switch_latest_window(self) :
		"""
        切换到最新的 tab/窗口
        :return:
        """
		window_handles = self.driver.window_handles
		self.driver.switch_to.window(window_handles[-1])
	
	def upload(self , img_path , position_expression , position_type=By.XPATH , timeout=5) :
		"""
        当 input 为 file 类型时，上传图片就是 send_keys 图片的本地路径
        :param img_path:
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """
		elm = self.find_element(
			position_type=position_type ,
			position_expression=position_expression ,
			timeout=timeout ,
			)
		elm.send_keys(img_path)
	
	def uploads(self , img_path , position_expression , position_type=By.XPATH , timeout=5) :
		"""
        上传图片到指定的元素位置，直接使用传入的图片路径。
        :param img_path: 图片的路径，必须传入
        :param position_expression: 用于定位上传按钮的表达式
        :param position_type: 定位方式
        :param timeout: 定位超时时间
        """
		if not os.path.exists(img_path) :
			raise ValueError(f"图片路径不存在: {img_path}")
		# 定位上传按钮并模拟文件上传
		elm = self.find_element(
			position_type=position_type ,
			position_expression=position_expression ,
			timeout=timeout , )
		elm.send_keys(img_path)
	
	def get_image_path_from_folder(self , folder_path) :
		'''
        当 input 为 file 类型时，上传图片就是 send_keys 图片的本地路径
        :param folder_path: 文件夹的路径
        :img_files:   列出文件夹中的所有文件
        :endswith :过滤出其中的图片文件
        :return:  返回文件夹中所有文件的路径列表  [0]代表取第一个
        '''
		img_files = os.listdir(folder_path)
		img_files = [f for f in img_files if f.endswith('.jpg') or f.endswith('.png')]
		
		if img_files :
			return os.path.join(folder_path , img_files[0])
		else :
			return None
	
	def get_image_path_from_folders(self , folder_path) :
		'''
        :param folder_path: 相对于项目根目录的路径
        :return: 文件夹中第一张图片的绝对路径
        :project_root:为了处理'/'或者'\'的路径转义
        '''
		# 获取项目根目录路径
		project_root = os.path.abspath(os.path.join(os.getcwd() , '../../..'))
		# 合并项目根目录与相对路径
		full_path = os.path.join(project_root , folder_path)
		# 检查文件夹是否存在
		if not os.path.exists(full_path) :
			print(f"Error: The folder {full_path} does not exist.")
			return None
		# 获取文件夹中的所有图片文件
		img_files = os.listdir(full_path)
		img_files = [f for f in img_files if f.endswith('.jpg') or f.endswith('.png')]
		if img_files :
			return os.path.join(full_path , img_files[0])  # 取根路径的第一个，方法代码本身改索引即可换图
		else :
			print("没有图片可用.")
			return False
	
	def fill_element_value(
			self , value , position_expression , position_type=By.XPATH , timeout=5
			) :
		"""
        给元素设置值，一般是 input 输入框
        :param value:
        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        """
		
		# 如果元素不可见，捕获异常之后，等待页面加载完成，再尝试获取一次元素
		try :
			# 获取元素
			a = time.time()
			elm = self.find_element_must_visible(
				position_expression , position_type , timeout
				)
		except (ElementNotVisibleException , Exception) :
			self.wait_page_ready(timeout)
			elm = self.find_element_must_visible(
				position_expression , position_type , timeout
				)
		
		# 清空数据
		# elm.clear()
		
		if not isinstance(value , str) :
			value = str(value)
		lines = value.split("\n")
		
		# action = ActionChains(self.driver)
		
		# 点击输入框，让焦点聚焦在输入框，以便输入值
		# action.click(elm)
		
		# for line in lines:
		#     action.send_keys(line)
		#     action.send_keys(Keys.RETURN)
		# action.perform()
		for line in lines :
			elm.send_keys(line , Keys.RETURN)
		
		return True
	
	def element_is_disappear(
			self , position_expression , position_type=By.XPATH , timeout=5
			) :
		"""
        元素是否已经消失
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
		wait = WebDriverWait(self.driver , timeout)
		try :
			wait.until_not(
				EC.presence_of_element_located((position_type , position_expression))
				)
		except TimeoutException :
			return False
		return True
	
	def wait_page_ready(self , timeout: int = 10) :
		"""
        等待页面加载完成
        :param timeout:
        :return:
        """
		start_ms = time.time() * 1000
		end_ms = start_ms + timeout * 1000
		for x in range(timeout * 10) :
			# 执行 js 当页面加载成功后，会返回 complete
			ready_state = self.driver.execute_script("return document.readyState")
			if ready_state == "complete" :
				return True
			if time.time() * 1000 > end_ms :
				break
			time.sleep(0.1)
		raise Exception(f"尝试等待 {timeout} 秒后，页面仍旧没有加载完成")
	
	def find_element_must_visible(
			self , position_expression , position_type=By.XPATH , timeout=5
			) :
		"""
        元素加载到 dom 树并且必须是可见（ 宽高大于0 ）的才认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
		
		def func() :
			return EC.visibility_of_element_located(
				(position_type , position_expression)
				)
		
		try :
			return self.__find_element(func , timeout)
		except Exception :
			raise ElementNotVisibleException(
				f"元素不可见，定位方式：{position_type}，定位表达式：{position_expression}"
				)
	
	def find_element_visibility_of_element_located(
			self , position_expression , position_type=By.XPATH , timeout=5
			) :
		"""

        可见性意味着元素不仅被显示出来，而且具有大于 0 的高度和宽度，并返回找到并可见的 WebElement
        一个检查元素是否存在于页面的 DOM 中且可见的期望
        :场景，用于等待某个列表容器的元素出现
        """
		
		def func() :
			return EC.visibility_of_element_located(
				(position_type , position_expression)
				)
		
		try :
			return self.__find_element(func , timeout)
		except Exception :
			raise ElementNotVisibleException(
				f"元素不可见，定位方式：{position_type}，定位表达式：{position_expression}"
				)
	
	def find_element_must_clickable(
			self , position_expression , position_type=By.XPATH , timeout=10
			) :
		"""An Expectation for checking an element is visible and enabled such that
        you can click it.
        element is either a locator (text) or an WebElement
        ：确保一个元素既是可见的，又是可点击的
        ：确保元素的 display 属性不是 none
        ：场景：①当你要点击一个按钮时，你通常需要确保按钮不仅存在，而且可以被点击。②动态加载内容：在处理动态加载的内容时，
        元素可能刚加载完成但尚未可点击，使用 element_to_be_clickable 可以确保在点击之前等待元素准备好。
        """
		
		def func() :
			return EC.element_to_be_clickable(
				(position_type , position_expression)
				)
		
		try :
			return self.__find_element(func , timeout)
		except Exception :
			raise ElementNotVisibleException(
				f"元素不可见，定位方式：{position_type}，定位表达式：{position_expression}"
				)
	
	def find_element(self , position_expression , position_type=By.XPATH , timeout=10) :
		"""
        元素加载到 dom 树就认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
		
		def func() :
			self.logger.info(f"当前行进元素{position_expression},使用find_element方法")
			return EC.presence_of_element_located((position_type , position_expression))
		
		try :
			return self.__find_element(func , timeout)
		except Exception :
			raise NoSuchElementException(
				f"元素不存在，定位方式：{position_type}，定位表达式：{position_expression}"
				)
	
	def find_elements(self , position_expression , position_type=By.XPATH , timeout=5) :
		"""
        元素加载到 dom 树就认为查找成功，并返回元素
        :param position_type:
        :param position_expression:
        :param timeout:
        :return:
        """
		
		def func() :
			return EC.presence_of_all_elements_located((position_type , position_expression))
		
		try :
			element = self.__find_element(func , timeout)
			return element
		except Exception :
			raise NoSuchElementException(
				f"元素不存在，定位方式：{position_type}，定位表达式：{position_expression}"
				)
	
	# 滑动页面加载页面所有元素
	def scroll_page(self , position_expression , position_type=By.XPATH , timeout=5) :
		'''

        :param position_expression:
        :param position_type:
        :param timeout:
        :return:
        '''
		elm = self.find_element(
			position_type=position_type ,
			position_expression=position_expression ,
			timeout=timeout ,
			)
		self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});" , elm)
		return elm
	
	def base_assertion_checks(
			self ,
			click_on_the_element: str ,  # 必填
			error_check_element_list: List[str] ,  # 必填，必须是列表
			is_url: bool = True ,  # 不必填，默认值为 False
			check_data: Optional[str] = None ,  # 必填
			data: Optional[dict] = None ,  # 不必填
			expected_results: Optional[str] = None ,
			state_check_method: Optional[Callable[[dict] , bool]] = None ,
			post_click_actions: Optional[List[Callable]] = None
			) :
		"""
        数据检查
        :param click_on_the_element: 点击的元素,确认或编辑
        :param error_check_element_list: 错误检查元素列表,报错信息的元素,列表传入
        :param is_url: 是否检查 URL 变化 True/为校验URL变化,False为校验元素变化
        :param check_data: 检查的参数 检查是否跳转的元素或者URl
        :param data: 数据  校验数据保存后是否正确的data
        :param expected_results: 期望结果 预期结果
        :param state_check_method: 状态检查方法  校验数据保存后是否正确的data
        :param post_click_actions: 成功后是否需要在进行操作
        :return:
        """
		# 滚动页面到指定元素位置
		self.scroll_page(position_expression=click_on_the_element)
		# 查找并点击指定元素
		elm = self.find_element(position_expression=click_on_the_element)
		self.driver.execute_script("arguments[0].click();" , elm)
		# 执行点击后的动作
		wait = WebDriverWait(self.driver , 5)
		# 动态生成等待条件
		conditions = []
		# 添加 URL 变化的条件
		if is_url is True :
			conditions.append(EC.url_changes(self.get_url(check_data)))
		else :
			conditions.append(EC.staleness_of(self.find_element(position_expression=check_data)))
			# 添加错误信息检查的条件
		for error_xpath in error_check_element_list :
			conditions.append(EC.visibility_of_element_located((By.XPATH , error_xpath)))
		# 使用 EC.any_of 动态传入多个条件
		ret = wait.until(EC.any_of(*conditions))
		if isinstance(ret , bool) :
			# 调用传入的状态检查方法
			if state_check_method :
				result = state_check_method(data)
				if result is True :
					if post_click_actions :
						for action in post_click_actions :
							action()
					return expected_results
				else :
					return f"页面状态不符合预期: {result}"
			else :
				return expected_results
		else :
			# 如果是错误信息，返回错误文本
			return ret.text
	
	def base_page_judgment(self , expected_data , *actual_data_lists) :
		"""
        页面断言通用方法
        :param expected_data: 包含期望值的字典
        :param actual_datas: 包含实际值的列表，可选添加多个
        :return: True 如果所有页面元素都存在于导出元素中，否则返回所有不匹配的断言信息
        """
		
		failed_assertions = []
		actual_datas = [item for sublist in actual_data_lists for item in sublist]
		print(actual_datas)
		expected_values = list(expected_data.values())
		print(expected_values)
		# 检查所有页面元素是否都在导出元素中
		for actual_data in actual_datas :
			if actual_data not in expected_values :
				failed_assertions.append(
					f"页面元素 '{actual_data}' 未在导出元素中找到."
					)
			else :
				expected_values.remove(actual_data)
		if failed_assertions :
			return "\n".join(failed_assertions)
		else :
			return True
	
	def base_list_copywriting(self , list_dictionary) :
		'''
        获取列表页的文本内容
        :return: 包含列表页各元素文本信息的列表
        '''
		
		def process_value(keys , value) :
			if isinstance(keys , tuple) :
				# 处理元组键的情况
				results = []
				for key in keys :
					if value == 'text' :
						results.append(self.find_element(position_expression=key).text)
					elif value == 'img' :
						results.append(self.find_element(position_expression=key).get_attribute('src'))
					elif value == 'img,optional' :
						try :
							results.append(
								(self.find_element(position_expression=key)).find_element(
									By.TAG_NAME ,
									'img'
									).get_attribute(
									'src'
									)
								)
						except :
							results.append('')
					elif value == 'text,split' :
						return re.sub(r'\D+' , '' , self.find_element(position_expression=key).text)
					else :
						return ''
				return results
			else :
				# 处理单个键的情况
				if value == 'text' :
					try :
						return self.find_element_must_visible(position_expression=keys).text
					except :
						return ''
				elif value == 'img' :
					try :
						return self.find_element_must_visible(position_expression=keys).get_attribute('src')
					except :
						return ''
				elif value == 'img,optional' :
					try :
						return (self.find_element(position_expression=keys)).find_element(
							By.TAG_NAME ,
							'img'
							).get_attribute('src')
					except :
						return ''
				elif value == 'text,split' :
					try :
						return re.sub(r'\D+' , '' , self.find_element(position_expression=keys).text)
					except :
						return ''
				else :
					return ''
		
		results = [process_value(key , value) for key , value in list_dictionary.items()]
		
		return results
	
	def wait_for_page_to_load(self , timeout=10) :
		"""
        等待页面加载完成，确保没有动画或加载条等阻碍操作的元素
        :param timeout: 等待时间
        """
		try :
			wait = WebDriverWait(self.driver , timeout)
			# 等待直到页面加载条消失
			wait.until(EC.invisibility_of_element_located((By.CLASS_NAME , 'loading-spinner')))
		except TimeoutException :
			print("页面加载超时，请检查加载状态！")
	
	def __find_element(self , func: Callable , timeout: int = 5) :
		wait = WebDriverWait(self.driver , timeout)
		return wait.until(func())


