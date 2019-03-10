import requests
#
# #
# url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.tmall.com'

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# from test11 import haha

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

path = r'/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
driver.maximize_window()
url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.7fa67adc2iVs8U&s=120&q=%CA%B3%C6%B7'
# url = 'https://www.jianshu.com/sign_in'
driver.get(url)
print("删除Cookie",driver.delete_all_cookies())
print(driver.title)
time.sleep(40)
# driver.page_source
print("获取Cookie",driver.get_cookies())
print(driver.current_url)
time.sleep(10)
print(driver.title)

# '''
# https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.7fa67adc2iVs8U&s=60&q=%CA%B3%C6%B7&sort=s&style=g&from=mallfp..pc_1_searchbutton&smAreaId=110100&type=pc#J_Filter
# '''

# url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.7fa67adc2iVs8U&s=120&q=%CA%B3%C6%B7'
# url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.ccf77adcc2VQEp&s=180&q=%CA%B3%C6%B7&sort=s&style=g&smAreaId=110100&type=pc#J_Filter'
# headers = {
#     # 'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
#     'User-Agent':'UCWEB7.0.2.37/28/999'
# }
#
# res = requests.get(url=url, headers=headers, verify=False)
# print(res.text)
# haha()
# import requests
# if 1:
#     url = 'http://127.0.0.1:5000/send_mail/'
#     a = '123'
#     b = '456'
#     res = requests.get(url, params={'name': a,'pwd':b})
#     print(res.text)
# else:
#     print('asdfghjk')

