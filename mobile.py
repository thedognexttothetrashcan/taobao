import datetime
import os
import random
import re
import time

import requests
from lxml import etree
from selenium import webdriver

mUA = 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
mWidth = 520
mHeight = 20431
PIXEL_RATIO = 3.0

mobileEmulation = {"deviceMetrics": {"width": mWidth, "height": mHeight, "pixelRatio": PIXEL_RATIO},
                   "userAgent": mUA}


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


def parse_url(url=None, func=None):
    driver.maximize_window()
    # url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.af6e5cb21bM0ce&brand=30111&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&type=pc'

    driver.get(url=url)
    time.sleep(2)
    # js = 'document.body.scrollTop=30000'
    # driver.execute_script(js)

    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)

    content = driver.page_source
    time.sleep(2)
    return func(content)
    # return first_page_parse(content)
    # return content


def first_page_parse(content):
    tree = etree.HTML(content)
    # time.sleep(100000)
    # price = tree.xpath('//p[@class="productPrice"]//em/text()')
    odiv = tree.xpath('//section[@id="J_srp"]//a[@class="tile_item"]')
    for a_div in odiv:
        item = {}
        # 详情连接
        detail_href = 'https:' + str(a_div.xpath('./@href')[0])
        # 商品id
        mode = re.compile(r'\d+')
        product_id = mode.search(detail_href).group()
        # 月销量
        yue_xiao = str(a_div.xpath('.//div[@class="tii_price"]//span[@class="tii_sold"]/text()')[0])
        # 标题
        title = str(a_div.xpath('.//div[@class="tii_title"]/h3/text()')[0]).strip()
        # 价格
        price = str(a_div.xpath('string(.//div[@class="tii_price"])')).replace('   \ue609  ', '').split('月销')[0].strip()
        # 店名称
        Shop_name = str(a_div.xpath('./div[@class="j_shop_more shop_more"]/span[1]/text()')[0])

        item['detail_href'] = detail_href
        item['yue_xiao'] = yue_xiao
        item['title'] = title
        item['price'] = price
        item['Shop_name'] = Shop_name
        item['product_id'] = product_id

        # 调用pase_url 解析详情页链接
        parse_url(url=detail_href, func=detail_page)
        print(item)


def detail_page(content):
    # print(content)
    # if '查看全部' in content:
    # print('123456789'*80)
    # common = driver.find_element_by_link_text('查看全部').click()
    driver.find_element_by_class_name('mui-tagscloud-more').click()
    time.sleep(2)
    conmon = driver.page_source
    # print(type(conmon))
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(2)
    tree = etree.HTML(conmon)
    all_li = tree.xpath('//*[@id="J_CommentsWrapper"]/ul[2]/li')
    for li in all_li:
        a1 = li.xpath('./text()')
        a = li.xpath('./[4]/text()')
        print(a)
    print('1234567890')


if __name__ == '__main__':
    url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.af6e5cb21bM0ce&brand=30111&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&type=pc'
    parse_url(url, first_page_parse)

