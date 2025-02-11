class LoginPosition(object):
	@classmethod
	def username(cls):
		return f' //input[@placeholder="请输入用户名或手机号"]'
	@classmethod
	def password(cls):
		return f' //input[@placeholder="请输入密码"]'
	def login_button(self):
		return f'//span[text()="登 录"]/parent::button'
	
