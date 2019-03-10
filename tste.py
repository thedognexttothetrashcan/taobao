# # from selenium import webdriver
# # import time
# # from selenium.webdriver.chrome.options import Options
# #
# # chrome_options = Options()
# # # chrome_options.add_argument('--headless')
# # # chrome_options.add_argument('--disable-gpu')
# #
# # path = r'/usr/bin/chromedriver'
# # driver = webdriver.Chrome(chrome_options=chrome_options)
# #
# # # url = 'https://login.tmall.com/?redirectURL=https%3A%2F%2Flist.tmall.com%2Fsearch_product.htm%3Fq%3D%25CA%25B3%25C6%25B7%26type%3Dp%26spm%3Da220m.1000858.a2227oh.d100%26from%3D.list.pc_1_searchbutton'
# # url = 'https://login.tmall.com/?redirectURL=https%3A%2F%2Flist.tmall.com%2Fsearch_product.htm%3Fspm%3Da220m.1000858.0.0.2c467adcD1Hb2U%26s%3D120%26q%3D%25CA%25B3%25C6%25B7%26sort%3Ds%26style%3Dg%26smAreaId%3D110100%26type%3Dpc%23J_Filter'
# # driver.get(url)
# # time.sleep(3)
# # login = driver.find_element_by_id('J_Quick2Static')
# # # login = driver.find_element_by_class_name('forget-pwd J_Quick2Static')
# # login.click()
# # print('kjgkjgk')
# # time.sleep(3)
# # zanghu = driver.find_elements_by_link_text('密码登录')
# # # zanghu = driver.find_elements_by_xpath('//*[@id="J_Form"]/div[2]/span')
# # zanghu.send_keys('18611138595')
# # pd = driver.find_element_by_id('TPL_password_1')
# # time.sleep(3)
# # pd.send_keys('5921haohao')
# # login = driver.find_element_by_id('J_SubmitStatic')
# # login.click()
# # driver.save_screenshot('ta11212.png')
# # time.sleep(3)
# #
# # driver.quit()
# #
# #
# #
# # url = 'http://www.baidu.com/'
# # driver.get(url)
# # # time.sleep(20)
# # driver.save_screenshot('l1.png')
# # driver.implicitly_wait(20)
# #
# # # 通过driver查找的到input输入框
# # myinput = driver.find_element_by_id('kw')
# # # 往框里面写内容
# # myinput.send_keys('气质美女')
# # time.sleep(3)
# # driver.save_screenshot('l2.png')
# #
# # # 点击百度一下
# # mybutton = driver.find_element_by_id('su')
# # mybutton.click()
# # time.sleep(4)
# # driver.save_screenshot('l3.png')
# # # 找到指定美女点击
# # # image = driver.find_element_by_xpath('//div[@id="1"]/div[1]/a[1]')
# # # image.click()
# # # time.sleep(3)
# #
# # # 点击美女图片的链接
# # oa = driver.find_element_by_link_text('气质美女_海量精选高清图片_百度图片')
# # driver.save_screenshot('l4.png')
# # oa.click()
# #
# #
# import json
# import random
#
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
#
# chrome_options = Options()
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
#
# from lxml import etree
# from selenium import webdriver
#
# mUA = 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
# mWidth = 375
# mHeight = 667
# PIXEL_RATIO = 3.0
#
# mobileEmulation = {"deviceMetrics": {"width": mWidth, "height": mHeight, "pixelRatio": PIXEL_RATIO},
#                    "userAgent": mUA}
#
#
# def create_chrome():
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option('mobileEmulation', mobileEmulation)
#     # ops.add_argument('--headless')
#     # ops.add_argument('--disable-gpu')
#
#     web = webdriver.Chrome(chrome_options=ops)
#     web.set_page_load_timeout(10)
#     web.set_script_timeout(10)
#     web.set_window_size(mWidth, mHeight)
#     return web
#
#
# driver = create_chrome()
#
#
#
#
#
# # path = r'/usr/bin/chromedriver'
# # driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
# # driver.maximize_window()
# url = 'https://login.m.taobao.com/login.htm?loginFrom=wap_tmall&assets_js=mui%2Ffeloader%2F4.0.22%2Ffeloader-min.js,mui%2Ftmapp-standalone%2F4.0.3%2Fseed.js,mui%2Ftmapp-standalone%2F4.0.3%2Flogin-download.js&assets_css=3.0.8%2Fmobile%2Ftmallh5.css&redirectURL=https%3A%2F%2Fwww.tmall.com'
# driver.get(url)
# # er wei ma
# # itchat = driver.find_element_by_id('J_Quick2Static')
# # itchat.click()
#
# # dian ji
# time.sleep(10)
# coun = driver.find_element_by_id('username')
# coun.click()
# time.sleep(2)
# coun.send_keys('18611138595')
# time.sleep(3)
# pwd = driver.find_element_by_id('password')
# pwd.click()
# time.sleep(2)
# pwd.send_keys('xwh123456')
# with open('cookies.json', 'r', encoding='utf-8') as f:
#     listCookies = json.loads(f.read())
# # hua kuai
# # action = ActionChains(driver)
# # dragger = driver.find_element_by_id('nc_1_n1z')
# # action.click_and_hold(dragger).perform()
# # action.release()
# # action.move_by_offset(180, 0).perform()
# # action.click_and_hold(dragger).move_by_offset(8000, 0).perform()
#
# # x = 258
# # # while x < 190:
# # #     x += random.randint(100, 160)
# # #     print(x)
# # action.click_and_hold(dragger).move_by_offset(x,0).perform()
# #
# # time.sleep(0.3)
# # # login
# # time.sleep(3)
# # login = driver.find_element_by_id('J_SubmitStatic')
# # login.click()
#
# # driver.quit()
#
#
#
#


import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
r = requests.get(url='https://s.taobao.com/search?q=%E5%8D%AB%E8%A1%A3',headers=headers)

print(r.text)


#
