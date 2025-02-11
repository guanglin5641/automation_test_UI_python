from page.component_page import ComponentPage
from position.channel.login import LoginPosition
from common.route import CHANNE_LLOGIN_URL
class LoginPage(ComponentPage,LoginPosition):
    def __init__(self , driver , path=CHANNE_LLOGIN_URL) :
        super().__init__(driver , path , "channel")
        
    def send_username(self , username ) :
        self.find_element(position_expression=self.username()).send_keys(username)
    def send_password(self , password ) :
        self.find_element(position_expression=self.password()).send_keys(password)
    
    def click_login_button(self) :
        self.find_element(position_expression=self.login_button()).click()
