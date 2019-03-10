import re
import time

import pymysql
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


def first_page_parse2(content):
    tree = etree.HTML(content)
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
        # parse_url(url=detail_href, func=detail_page)
        save_to_mysql(item)


def first_page_parse(content):
    tree = etree.HTML(content)
    div = tree.xpath('//a[@class="list_item"]')
    # time.sleep(1000)
    for a_div in div:
        item = {}
        til = a_div.xpath('.//div[@class="li_info"]/h3/text()')
        if til == None:
            print('运行第二个解析函数...............')
            first_page_parse2(content)

        # 标题
        title = str(a_div.xpath('.//div[@class="li_info"]/h3/text()')[0]).strip()

        # 详情连接
        detail_href = 'https:' + str(a_div.xpath('./@href')[0])

        # 商品id
        mode = re.compile(r'\d+')
        product_id = mode.search(detail_href).group()

        # 价格
        price = str(a_div.xpath('string(.//div[@class="lii_price"])')).replace('   \ue609  ', '').split('月销')[0].strip(
            '免运费')

        # 店名称
        shop_name = str(a_div.xpath('.//p[@class="lii_sold"]/span[1]/text()')[0])

        # 月销量
        sale_num = str(a_div.xpath('.//p[@class="lii_sold"]/text()')[0])

        item['detail_href'] = detail_href
        item['sale_num'] = sale_num
        item['title'] = title
        item['price'] = price
        item['Shop_name'] = shop_name
        item['product_id'] = product_id

        # 调用pase_url 解析详情页链接
        parse_url(url=detail_href, func=detail_page)
        save_to_mysql(item)


db = pymysql.connect(host="211.103.199.115", user="pdm002", password="pdm#Ko0307min", db="pdi_data", port=3306,
                     charset='utf8')

def save_to_mysql(item):
    print(item)

    # print(type(db))
    # cur = db.cursor()
    # sql = """insert into tm_product() values('%s','%s','%s','%s','%s')""" % ()
    # # print(sql)
    # try:
    #     cur.execute(sql)
    #     db.commit()
    # except Exception as e:
    #     # print(e)
    #     db.rollback()


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
        a = li.xpath('./li[@class="tag-product"]/text()')
        print(a)


if __name__ == '__main__':
    # iphone
    # url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.af6e5cb21bM0ce&brand=30111&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&type=pc'
    url = 'https://list.tmall.com/search_product.htm?q=%C8%FD%D0%C7&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
    list_url = [
        'https://list.tmall.com/search_product.htm?q=%D0%A1%C3%D7&type=p&spm=a220m.1000858.a2227oh.d100&xl=xiao_1&from=.list.pc_1_suggest',
        'https://list.tmall.com/search_product.htm?q=%BA%C3%B2%CA%CD%B7%CB%E1Q%CC%C7&type=p&tmhkh5=&spm=a220m.6910245.a2227oh.d100&from=mallfp..m_1_searchbutton',
        'https://list.tmall.com/search_product.htm?spm=a223j.8443192.0.0.585ac41yHala3&q=iPhone&from=nav_ct_8019_8000_8001']
    num = 0
    for url in list_url:
        time.sleep(3)
        num += 1
        print('第%d叶......................start' % int(num))
        parse_url(url, first_page_parse)
        print('第%d叶......................end' % int(num))
        print('\n')
    db.close()
