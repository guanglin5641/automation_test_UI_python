from page.channel.login import LoginPage
from testcases.base import Base
from common.data import case_data
import pytest
import allure
case_data = case_data("channel.xlsx", "login")
class TestLogin(Base):
	@allure.feature("活动查询")
	@allure.story("活动查询")
	@allure.title("活动查询")
	@pytest.mark.parametrize("login_data" , case_data)
	def test_act_query(self,fixture_driver,login_data):
		with allure.step("打开登录页面"):
			login_page = LoginPage(fixture_driver)
		with allure.step("输入用户名和密码"):
			login_page.send_username(login_data["操作"]["username"])
			login_page.send_password(login_data["操作"]["password"])
		with allure.step("点击登录按钮"):
			login_page.click_login_button()
		
