from selenium import webdriver
import json

import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


mUA = 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
mWidth = 675
mHeight = 967
PIXEL_RATIO = 3.0

mobileEmulation = {"deviceMetrics": {"width": mWidth, "height": mHeight, "pixelRatio": PIXEL_RATIO},
                   "userAgent": mUA}

#
def create_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option('mobileEmulation', mobileEmulation)
    # ops.add_argument('--headless')
    # ops.add_argument('--disable-gpu')

    """
    '218.60.8.99:3129',
    '113.200.56.13:8010',
    '140.143.96.216:80',
    """
    ops.add_argument('--proxy-server=http://218.60.8.99:3129')

    web = webdriver.Chrome(chrome_options=ops)
    web.set_page_load_timeout(10)
    web.set_script_timeout(10)
    web.set_window_size(mWidth, mHeight)
    return web


driver = create_chrome()



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=127.0.0.1:8000')
# path = r'/usr/bin/chromedriver'
# driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
driver.maximize_window()
# url = 'https://login.m.taobao.com/login.htm?loginFrom=wap_tmall&assets_js=mui%2Ffeloader%2F4.0.22%2Ffeloader-min.js,mui%2Ftmapp-standalone%2F4.0.3%2Fseed.js,mui%2Ftmapp-standalone%2F4.0.3%2Flogin-download.js&assets_css=3.0.8%2Fmobile%2Ftmallh5.css&redirectURL=https%3A%2F%2Fwww.tmall.com'
url = 'https://login.tmall.com/'
driver.get(url)

time.sleep(5)
# coun = driver.find_element_by_id('username')
# coun.click()
# time.sleep(2)
# coun.send_keys('18611138595')
# time.sleep(3)
# pwd = driver.find_element_by_id('password')
# pwd.click()
# time.sleep(2)
# pwd.send_keys('xwh123456')
# 获取cookie并通过json模块将dict转化成str
# name="um_token"
# value="HV02PAAZ0b01bf1a7b76044f5c8372510072c9a0999999"
# driver.add_cookie(cookie_dict={name:value})
# dictCookies = driver.get_cookies()
# jsonCookies = json.dumps(dictCookies)
# # 登录完成后，将cookie保存到本地文件
# # with open('cookies.json', 'w') as f:
# #     f.write(jsonCookies)
#
time.sleep(3)
driver.find_element_by_id('submit-btn').click()

input("回车：")
driver.get(url)