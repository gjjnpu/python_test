'''
    定义测试流程
'''

from keyword_for_ui.webui_keyword import WebuiDemo
import  time

# TEST 1

wd = WebuiDemo('Chrome')
getattr(wd, 'visit')('https://www.baidu.com')
#wd.visit('https://www.baidu.com/')
# wd.input('id', 'kw', 'python')
# wd.ckick('id', 'su')