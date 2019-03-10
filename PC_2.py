import datetime
import os
import random
import time

import requests
from lxml import etree
from selenium import webdriver
# import config
import threading

# import numpy as np

mUA_list = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C153 Safari/604.1',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
]

pcUA = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
mWidth = 1440
mHeight = 2000
PIXEL_RATIO = 3.0

mobileEmulation = {"deviceMetrics": {"width": mWidth, "height": mHeight, "pixelRatio": PIXEL_RATIO},
                   }  # "userAgent": random.choice(pcUA)



def create_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option('mobileEmulation', mobileEmulation)
    # ops.add_argument('--headless')
    # ops.add_argument('--disable-gpu')

    web = webdriver.Chrome(chrome_options=ops)
    web.set_page_load_timeout(10)
    web.set_script_timeout(10)
    web.set_window_size(mWidth, mHeight)
    return web


driver = create_chrome()
driver.maximize_window()

driver.get(
    'https://detail.tmall.com/item.htm?id=584865383924&skuId=3951416717001&areaId=110100&user_id=902218705&cat_id=2&is_b=1&rn=289a6a85d6f5c3ca9cb4ea875d191f90&on_comment=1')

time.sleep(2)
# print(driver.get_cookies())
time.sleep(20)
print(driver.page_source)

