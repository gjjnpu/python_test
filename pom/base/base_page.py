from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import  time

# chrome, firefox, ie, safari
def open_browser(browser_type):

    # browser = {'chrome': ['Chrome', 'chrome', 'cc', 'guge'], 'ie': ['ie', 'Ie', 'IE']}
    # if browser_type in browser['chrome']:
    #     pass
    # else if browser_type in browser['ie']:
    #     pass
    # else:
    #     pass

    try:
        driver = getattr(webdriver, browser_type)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class BasePage:
    '''
        1. 元素定位
        2. 输入
        3. 点击
        4. 访问
        5. 关闭
        6. 等待
        。。。。
    '''
    driver = webdriver.Chrome()

    def __init__(self, broser_type):
         self.driver = open_browser(broser_type)

    # 元素定位(id,class,xpath,css....)
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    def input(self, name, value, text):
        self.locate(name, value,text)

    def click(self, name, value):
        self.locate(name, value).click()

    def visit(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def sleep(self, second):
        time.sleep(time)

    def assert_text(self, by, value, expected):
        try:
            reality = self.locator(by, value).text
            assert expected == reality, '{} and {} is not equal'.format(expected, reality)
        except Exception as e:
            print('assert failure :{}'.format(e))

    def driver_wait(self,by, value):
        return WebDriverWait(self.driver,10, 0.5).until(lambda el:self.locate(by, value))
