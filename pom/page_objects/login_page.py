from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    url = 'www.xxxx/logoin'
    user = (By.NAME,'acount')
    pwd = (By.Name,'pwd')
    button = (By.CSS, 'div a>span')

    def log_in(self):
        self.visit(*self.url)
        self.input(*self.user)
        self.input(*self.pwd)
        self.click(self.button)