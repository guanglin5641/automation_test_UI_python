import time
from common.decorators import wait_all_methods
import random
from page.web_page.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@wait_all_methods
class ComponentPage(BasePage , object) :
	def __init__(self , driver , path , project) :
		super().__init__(driver , path=path , project=project)
		self.switch_to = None
	
	def set_rich_text_content_component(self , iframe_element , content) :
		"""
        在指定的iframe中设置富文本框的内容。

        参数:
        self: WebDriver 实例。
        content: 要输入的内容。如果为 None 或空字符串，则不执行任何操作。
        """
		
		if content is None or content.strip() == "" :
			return None
		else :
			self.switch_iframe(position_expression=iframe_element)
			self.find_element(position_expression='//body').clear()
			self.find_element(position_expression='//body').send_keys(content)
			self.switch_default_iframe()
		return
	
	def image_component(self , main_path , image_link) :
		'''
        图片选择组件
        :param main:
        :param brand_logo:
        :return:
        '''
		print(main_path , type(main_path))
		popups_main_path = f"(//div[@class='el-dialog'])[last()]"
		popups_link = popups_main_path + f"//input[@placeholder='输入图片链接后按回车键直接添加']"
		popups_choose = f"({popups_main_path}//div[@class='el-image'])[1]"
		popups_determine = f"({popups_main_path}//button)[last()]"
		thumbnail_check = main_path + '//li[1]'
		thumbnail_open = main_path + "//div[@class='yun-img-loader__pmask']"
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , thumbnail_check)))
				)
			
			a = 1
		except :
			
			a = 0
		
		if not image_link :
			if a == 1 :
				self.find_element(position_expression=thumbnail_check).click()
				self.find_element(position_expression=thumbnail_check).send_keys(Keys.BACKSPACE)
				
				return
			return
		if a == 1 :
			self.find_element(position_expression=thumbnail_check).click()
			self.find_element(position_expression=thumbnail_check).send_keys(Keys.BACKSPACE)
		self.find_element(position_expression=thumbnail_open).click()
		self.find_element(position_expression=popups_link).send_keys(image_link)
		self.find_element(position_expression=popups_link).send_keys(Keys.ENTER)
		self.find_element(position_expression=popups_choose).click()
		self.find_element_must_visible(position_expression=popups_determine).click()
		return
	
	def image_components(self , main_path , image_link) :
		'''
        多张图片选择组件
        :param main:
        :param brand_logo:
        :return:
        '''
		popups_main_path = f"(//div[@class='el-dialog'])[last()]"
		popups_link = popups_main_path + f"//input[@placeholder='输入图片链接后按回车键直接添加']"
		popups_choose = f"({popups_main_path}//div[@class='el-image'])[1]"
		popups_determine = f"({popups_main_path}//button)[last()]"
		thumbnail_check = main_path + '//li'
		thumbnail_open = main_path + "//div[@class='yun-img-loader__pmask']"
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , thumbnail_check)))
				)
			
			a = 1
		except :
			
			a = 0
		if not image_link :
			if a == 1 :
				b = self.find_elements(position_expression=thumbnail_check)
				for i in b :
					i.click()
					i.send_keys(Keys.BACKSPACE)
					time.sleep(0.5)
				return
			return
		if a == 1 :
			b = self.find_elements(position_expression=thumbnail_check)
			for i in b :
				i.click()
				i.send_keys(Keys.BACKSPACE)
				time.sleep(0.5)
		for c in image_link :
			self.find_element(position_expression=thumbnail_open).click()
			self.find_element(position_expression=popups_link).send_keys(c)
			self.find_element(position_expression=popups_link).send_keys(Keys.ENTER)
			self.find_element(position_expression=popups_choose).click()
			self.find_element(position_expression=popups_determine).click()
		return
	
	def category_component(self , input_box_element , main_category) :
		'''
        分类类目组件
        :param category:
        :return:
        '''
		if not main_category :
			return
		main_path = f"//div[@class='el-popper is-pure is-light el-dropdown__popper cate-panel-poper']"
		path = []
		for i in range(len(main_category)) :
			path.append(f"{main_path}//section//section[{i + 1}]//li/p")
		self.find_element(position_expression=input_box_element).click()
		for i in range(len(path)) :
			one_len = (self.find_elements(position_expression=f"{main_path}//section//section[{i + 1}]//li/p"))
			for y in one_len :
				if y.text == main_category[i] :
					y.click()
					break
		self.find_element(position_expression=input_box_element).click()
		return
	
	def input_box_component(self , input_box_element , input_box_text) :
		'''
        输入框组件
        :param input_box_element:
        :param input_box_text:
        :return:
        '''
		self.scroll_page(position_expression=input_box_element)
		input_element = self.find_element_must_visible(position_expression=input_box_element)
		if not input_box_text :
			input_element.send_keys(Keys.CONTROL + 'a')  # On Windows
			if platform.system() == 'Darwin' :  # On Mac
				input_element.send_keys(Keys.COMMAND + 'a')
			input_element.send_keys(Keys.DELETE)
			return
		input_element.send_keys(Keys.CONTROL + 'a')  # On Windows
		if platform.system() == 'Darwin' :  # On Mac
			input_element.send_keys(Keys.COMMAND + 'a')
		input_element.send_keys(Keys.DELETE)
		input_element.send_keys(input_box_text)
	
	def drop_down_box_component(self , drop_down_element , drop_down_text) :
		'''
        下拉框组件
        :param drop_down_element:
        :param drop_down_text:
        :return:
        '''
		print("打印时间" , time.time())
		element = "//div[@aria-hidden='false']//li/span"
		if not drop_down_text :
			return
		self.find_element_must_visible(position_expression=drop_down_element).click()
		options = self.find_elements(position_expression=element)
		for i in range(len(options)) :
			a_element = f"({element})[{i + 1}]"
			self.scroll_page(position_expression=a_element)
			a = self.find_element_must_visible(position_expression=a_element)
			if a.text == drop_down_text :
				a.click()
				print("点击时间" , time.time())
				break
		return
	
	def presence_of_element_located(self , locator) :
		"""An expectation for checking that an element is present on the DOM of a page.
        This does not necessarily mean that the element is visible.

        locator - used to find the element
        returns the WebElement once it is located

        locator = (By.ID, "element_id")  # ID 定位
        locator = (By.XPATH, "//div[@class='example']")  # XPATH 定位
        locator = (By.CLASS_NAME, "example-class")  # 类名定位
        """
		
		def _predicate(driver) :
			return driver.find_element(locator)
		
		return _predicate
	
	def presence_of_element_located_list(self , locator) :
		"""An expectation for checking that an element is present on the DOM of a page.
        This does not necessarily mean that the element is visible.
        locator - used to find the element
        returns the WebElement's text content as a list, split by newlines
        # 获取 WebElement 对象
        # 获取元素的文本内容并按换行符分割成列表
        # 将文本按换行符分割成列表
        # 返回分割后的文本列表
        """
		
		def _predicate(driver) :
			element = driver.find_element(locator)
			element_text = element.text
			element_text_lines = element_text.splitlines()
			return element_text_lines
	
	def drop_down_box_component_random_choice(self , drop_down_element) :
		'''
        下拉框组件，随机选择一个选项
        :param drop_down_element: 下拉框的定位元素
        :return: None
        '''
		element = "//div[@aria-hidden='false']//li/span"
		self.find_element_must_visible(position_expression=drop_down_element).click()
		options = self.find_elements(position_expression=element)
		if not options :
			return
		random_option = random.choice(options)
		random_option_element = f"({element})[{options.index(random_option) + 1}]"
		self.scroll_page(position_expression=random_option_element)
		random_option.click()
		
		return
	
	def check_box_component(self , check_element , check_texts) :
		'''
        多选点击组件
        :param check_element:
        :param check_texts:
        :return:
        '''
		check_element_list = f"{check_element}//label//span[@class='el-checkbox__label']"
		check_element_select = f"{check_element}//label[@class='el-checkbox is-checked']"
		get_list = self.find_elements(position_expression=check_element_list)
		resource_type_lists = []
		for i in get_list :
			resource_type_lists.append(i.text)
		all_dict = { item : index + 1 for index , item in enumerate(resource_type_lists) }
		text_len = len(check_texts)
		# 先查询是否有被点击元素
		
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , check_element_select)))
				)
			a = 1
		except :
			a = 0
		if not check_texts :
			if a == 1 :
				selected = self.find_elements(position_expression=check_element_select)
				for i in selected :
					i.click()
				return
			return
		elif a == 1 :
			selected = self.find_elements(position_expression=check_element_select)
			for i in selected :
				i.click()
			
			for i in range(text_len) :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//label[{all_dict[check_texts[i]]}]'
					self.find_element(position_expression=serial_number).click()
				else :
					continue
		else :
			for i in range(text_len) :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//label[{all_dict[check_texts[i]]}]'
					self.find_element(position_expression=serial_number).click()
				
				else :
					continue
	
	def single_box_component(self , single_element , single_text) :
		'''
        单选点击组件
        :param single_element:
        :param single_text:
        :return:
        '''
		single_text_lists = []
		# single_element = "//label[text()='状态']/parent::div/div"
		single_lists = f"{single_element}//span[@class='el-radio__label']"
		# print(single_lists)
		len_single_list = self.find_elements(position_expression=single_lists)
		for i in len_single_list :
			# if i.text == single_text:
			single_text_lists.append(i.text)
		if not single_text :
			return
		elif single_text in single_text_lists :
			serial_number = single_element + f"//span[text()='{single_text}']"
			self.find_element(position_expression=serial_number).click()
		return
	
	def switch_component(self , switch_element , switch_text) :
		'''
        开关组件
        :param switch_element: 元素组件对应的父级前缀
        :param switch_text:
        :return:
        '''
		switch_element_text = f"{switch_element}//span[@class='is-text']"
		if not switch_text :
			return
		brand_status_text = self.find_element(position_expression=switch_element_text).text
		if brand_status_text == switch_text :
			return
		self.find_element(position_expression=switch_element_text).click()
	
	def collapse_relative(self , supplier_phone , encoding_value) :
		'''
        选择话费供应商，并执行相关操作

        Args:
            supplier_phone (str): 供应商名称
            encoding_value (str): 编码值

        Returns:
            bool: 操作是否成功
        '''
		# 定义 XPath 表达式
		is_open = "//div[@class='el-collapse relative']"
		gys_list = f"{is_open}//span[@class='el-text el-text--primary']"
		is_true = f"{is_open}//span[@class='el-text el-text--primary']/parent::div/parent::div"
		gys_name = f"{is_open}//span[text()='{supplier_phone}']"
		encoding_position = f"{gys_name}/parent::div/parent::div/parent::div//div[@class='el-table__body-wrapper']//colgroup/col[1]"
		associated_location = f"{gys_name}/parent::div/parent::div/parent::div//div[@class='el-table__body-wrapper']//colgroup/col[6]"
		# 检查是否展开
		if self.find_element_must_visible(position_expression=is_open) :
			# 获取供应商列表和展开状态列表
			supplier_elements = self.find_elements(position_expression=gys_list)
			is_true_elements = self.find_elements(position_expression=is_true)
			
			# 遍历供应商列表
			for i in range(len(supplier_elements)) :
				# 检查供应商是否匹配
				if supplier_elements[i].text == supplier_phone :
					# 获取展开状态
					is_expanded = is_true_elements[i].get_attribute("aria-expanded")
					# 如果未展开，则点击展开
					if is_expanded == "false" :
						supplier_elements[i].click()
					# 获取编码位置值和相关位置值
					encoding_position_value = self.find_element(position_expression=encoding_position).get_attribute(
						"name"
						)
					associated_location_value = self.find_element(
						position_expression=associated_location
						).get_attribute("name")
					# 构建编码值和相关位置的 XPath 表达式
					encoding_values = f"{gys_name}/parent::div/parent::div/parent::div//tbody//td[@class='{encoding_position_value} el-table__cell']/div[@class='cell']"
					associated_clicks = f"{gys_name}/parent::div/parent::div/parent::div//tbody//td[@class='{associated_location_value} el-table-fixed-column--right is-first-column el-table__cell']//button"
					
					# 获取编码值和点击按钮列表
					encoding_list = self.find_elements(position_expression=encoding_values)
					associated_list = self.find_elements(position_expression=associated_clicks)
					
					# 遍历编码值列表
					for j in range(len(encoding_list)) :
						a = self.driver.execute_script("return arguments[0].textContent.trim();" , encoding_list[j])
						# print(a)
						# 检查编码值是否匹配
						if a == encoding_value :
							# print(a)
							# 点击相关位置按钮
							# time.sleep(2)
							# associated_list[j].click()
							self.driver.execute_script("arguments[0].click();" , associated_list[j])
					break
		
		return False  # 操作失败，返回 False
	
	# def textarea_component(self, textarea_element, content):
	#     """
	#     在指定的文本区域中输入内容。
	#
	#     参数:
	#     self: WebDriver 实例。
	#     textarea_element: 文本区域的 ID。
	#     content: 要输入的内容。
	#     """
	#     self.scroll_page(position_expression=textarea_element)
	#     try:
	#         # 使用 WebDriverWait 等待元素出现并可见
	#         locator = (By.XPATH, textarea_element)
	#
	#         wait = WebDriverWait(self.driver, 2)
	#         textarea = wait.until(EC.presence_of_element_located(locator))
	#         self.element_is_disappear(position_expression=locator)
	#         # 清空文本区域内容
	#         textarea.clear()
	#
	#         # 输入内容
	#         textarea.send_keys(content)
	#     except Exception as e:
	#         print(f"输入文本区域内容时出现异常: {str(e)}")
	def check_box_good_component(self , check_element , check_texts) :
		'''
        货源多选点击组件
        :param check_element:
        :param check_texts:
        :return:
        '''
		# check_element = "//div[@class='goods-detail-item']//p[@class='font-semibold']"
		check_element_list = f"{check_element}//div[@class='goods-detail-item']//p[@class='font-semibold']"
		check_element_select = f"{check_element}//label[@class='el-checkbox']//input"
		get_list = self.find_elements(position_expression=check_element_list)
		resource_good_lists = []
		for i in get_list :
			resource_good_lists.append(i.text)
		all_dict = { item : index + 1 for index , item in enumerate(resource_good_lists) }
		text_len = len(check_texts)
		# 先查询是否有被点击元素
		
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , check_element_select)))
				)
			a = 1
		except :
			a = 0
		if not check_texts :
			if a == 1 :
				selected = self.find_elements(position_expression=check_element_select)
				for i in selected :
					i.click()
				return
			return
		elif a == 1 :
			selected = self.find_elements(position_expression=check_element_select)
			for i in selected :
				i.click()
			
			for i in range(text_len) :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//tr[{all_dict[check_texts[i]]}]//label'
					self.find_element(position_expression=serial_number).click()
				else :
					continue
		else :
			for i in range(text_len) :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//tr[{all_dict[check_texts[i]]}]//label'
					self.find_element(position_expression=serial_number).click()
				else :
					continue
	
	def check_box_property_component(self , check_element , check_texts) :
		'''
        属性多选点击组件
        :param check_element:
        :param check_texts:
        :return:
        '''
		check_element_list = f"{check_element}//td[1]//div"
		check_element_select = f"{check_element}//label"
		get_list = self.find_elements(position_expression=check_element_list)
		property_lists = [i.text for i in get_list]
		all_dict = { item : index + 1 for index , item in enumerate(property_lists) }
		text_len = list(range(len(check_texts)))
		
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , check_element_select)))
				)
			a = 1
		except :
			a = 0
		if not check_texts :
			if a == 1 :
				selected = self.find_elements(position_expression=check_element_select)
				for i in selected :
					i.click()
				return
			return
		elif a == 1 :
			# selected = self.find_elements(position_expression=check_element_select)
			# for i in selected:
			#     i.click()
			
			for i in text_len :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//tbody//tr[{all_dict[check_texts[i]]}]//label'
					self.find_element(position_expression=serial_number).click()
				else :
					continue
		else :
			for i in text_len :
				if check_texts[i] in all_dict.keys() :
					serial_number = check_element + f'//tr[{all_dict[check_texts[i]]}]//label'
					self.find_element(position_expression=serial_number).click()
				else :
					continue
		
		# 如果未找到名称对应的行，返回 False
	
	def check_subproperty_component(self , check_element , check_texts) :
		check_element_list = f"{check_element}//span[2]"
		check_element_select = f"{check_element}//label"
		get_list = self.find_elements(position_expression=check_element_list)
		property_lists = [i.text for i in get_list]
		all_dict = { item : index + 1 for index , item in enumerate(property_lists) }
		text_len = list(range(len(check_texts)))
		try :
			WebDriverWait(self.driver , 1).until(
				EC.any_of(EC.visibility_of_element_located((By.XPATH , check_element_select)))
				)
			a = 1
		except :
			a = 0
		if not check_texts :
			if a == 1 :
				selected = self.find_elements(position_expression=check_element_select)
				for i in selected :
					i.click()
				return
			return
		elif a == 1 :
			# selected = self.find_elements(position_expression=check_element_select)
			# for i in selected:
			#     i.click()
			
			for i in text_len :
				if check_texts[i] in all_dict.keys() :
					serial_number = f"{check_element}//span[text()={check_texts[i]}]/parent::label"
					self.find_element(position_expression=serial_number).click()
				else :
					continue
		else :
			for i in text_len :
				if check_texts[i] in all_dict.keys() :
					serial_number = f"{check_element}//span[text()={check_texts[i]}]/parent::label"
					self.find_element(position_expression=serial_number).click()
				else :
					continue
	
	def select_dropdown_option(self , dropdown_element , option_value) :
		"""
        使用正则表达式传值并选择下拉列表中的选项

        Args:
        - driver: WebDriver对象
        - dropdown_id: 下拉列表的id
        - option_value: 需要选择的值，可以是正则表达式模式

        Returns:
        - 如果成功选择，返回成功消息，否则返回未找到匹配的选项消息
        """
		if not option_value :
			return
		
		self.find_element(position_expression=dropdown_element).click()
		drop_down_content = f"//span[text()='{option_value}']/parent::div/parent::div/parent::li"
		# time.sleep(2)
		self.find_element_must_visible(position_expression=drop_down_content).click()
		
		# try:
		#     dropdown = Select(self.find_element(By.XPATH, dropdown_element))
		#     options = [o.text for o in dropdown.options]
		#
		#     # 使用正则表达式进行模糊匹配
		#     regex = re.compile(option_value, re.IGNORECASE)
		#     matched_option = None
		#     for option in options:
		#         if regex.search(option):
		#             matched_option = option
		#             print(matched_option)
		#             break
		#     drop_down_content=f"//div[@class='el-select-dropdown']//li//span[text()='{matched_option}']"
		#     self.find_element(position_expression=drop_down_content).click()
		
		# if matched_option:
		#     dropdown.select_by_visible_text(matched_option)
		#     return f"成功选择下拉列表中的选项: {matched_option}"
		# else:
		#     return "未找到匹配的选项"
	
	def hover_and_delete_element(self , element_locator , delete_key=True) :
		"""
        模拟鼠标悬浮到指定元素，并执行删除操作。
        :param element_locator: 元素的定位方式（例如，通过ID，XPATH等定位元素）
        :param delete_key: 是否模拟按下Delete键，默认为True。如果需要点击删除按钮，传入 False，否则按默认值 True 模拟键盘 DELETE 操作。
        """
		# 找到目标元素
		element = self.find_element(position_expression=element_locator)
		
		# 创建一个对象来模拟鼠标悬浮
		actions = ActionChains(self.driver)
		actions.move_to_element(element).perform()  # 将鼠标悬停在目标元素上
		
		# 根据参数决定是否模拟按下 DELETE 键
		if delete_key :
			# 模拟按下 DELETE 键
			element.send_keys(Keys.DELETE)
		else :
			# 如果不使用 DELETE 键，可以在这里添加点击操作等其他逻辑
			pass


if __name__ == '__main__' :
	a = 7
	b = 21
	print(a ** b)



