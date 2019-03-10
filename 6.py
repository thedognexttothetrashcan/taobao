import random
import re
import time
import requests
from lxml import etree
from selenium import webdriver

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "cna=gY5E8vPMGACASvgLWesBpgg; _med=dw:1440&dh:900&pw:1440&ph:900&ist:0; l=bBgQUK1lvHlc2bE_BOCg5uI81fb9kIRPguPRwGoei_5Q-1T-JB_OlkIbwe96Vj5P9bYB4R3ZAF9teFmT8PsV.; sm4=110100; enc=xzqpgSiaHaMOi%2BHzY%2BcQ8xIJ6jeSOrGpaJQ3yJ2MJm22hbDyWWnk1saajEjzUU5PAmCn0Kvw4fr%2FIX%2F6FkAhoA%3D%3D; _uab_collina=155187561517221955690883; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; tk_trace=1; t=a3e60ff03b942db42bf59b62b90443e5; _tb_token_=31be3e73997e5; cookie2=1b8f21a5c9e506e84e656d60295a13a5; cq=ccp%3D0; _m_h5_tk=2b2e6ca1faf3b9ef51840702c02623a2_1552193233241; _m_h5_tk_enc=14e720156a77f0f3f7de9aebce6942d4; hng=""; uc1=cookie21=V32FPkk%2FhSg%2F&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoTZ5iTH1XrsOA%3D%3D; uc3=vt3=F8dByEvz0Szpp1DisBo%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; uss=""; csg=43d8c04e; skt=5b8c3cc2a083a8a4; tt=tmall-main; res=scroll%3A1440*5485-client%3A1440*789-offset%3A1440*5485-screen%3A1440*900; pnm_cku822=098%23E1hvH9vUvbpvjQCkvvvvvjiPRLqhtjrbRLqpQjEUPmPysjYWP2chAjlURFM96j9Pvpvhvv2MMQyCvh1hNx9vITtGVB%2Bkaf90%2BktEnHsG1CywJhHTpYLZV1O07oDn9Wma%2BoHoEpchQC6tExhlBqev%2BulgEc6OfwkXdeQEVADlYbVrwZyaWXxrKphv8hCvvvvvvhCvphvZ99vvplXvpComvvC216CvHUUvvhn9phvZ99vvpGJivpvUphvhifEJ0R4EvpvVpyUU2E%2BXvphvCyCCvvvvv2yCvvBvpvvviQhvChCvCCp%3D; isg=BLq61pFZsrFqODnGWWrCECoAC-ZwfzRHEENi48SzI80Yt1rxrPmfVEvFAwPOJ7bd",
    "referer": "https://list.tmall.com/search_product.htm?q=iiphone&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}
# url = 'https://list.tmall.com/search_product.htm?q=三星+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
# url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.4f585cb2WFk5MD&brand=30111&s=60&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&smAreaId=110100&type=pc#J_Filter'
def first_page(url):
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    div = tree.xpath('//div[@class="product-iWrap"]')
    for li in div:
        item = {}
        # 价格
        price = li.xpath('./p/em/@title')[0]
        # 详情页链接
        detail_href = 'http:' + li.xpath('./div/a/@href')[0]
        # 商品id
        product_id_detail = li.xpath('./div/a/@href')[0]
        product_id = re.findall(r'\d+',product_id_detail)[0]
        # 商品名称
        product_name= li.xpath('./p/a/@title')[0]
        # 商店名称
        shop_name = str(li.xpath('./div[@class="productShop"]/a/text()')[0]).strip('\n')
        # 月销量
        try:
            mon_sales = str(li.xpath('./p[@class="productStatus"]/span/em/text()')[0]).strip('\n')
        except Exception as e:
            mon_sales = '空'
        # 评价数量
        try:
            comment_count = str(li.xpath('./p[@class="productStatus"]/span[2]/a/text()')[0])
        except Exception as e:
            comment_count = '空'
        # 评价链接
        try:
            comment_href = 'http:'+str(li.xpath('./p[@class="productStatus"]/span[2]/a/@href')[0])
        except Exception as e:
            comment_href = '空'



        item['price'] = price
        item['detail'] = detail_href
        item['shop_name'] = product_name
        item['shop_name'] = shop_name
        item['mon_sales'] = mon_sales
        item['comment_count'] = comment_count
        item['comment_href'] = comment_href
        item['product_id'] = product_id
        detaail_page(item)






# # mUA = 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
# mUA ="user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
# mWidth = 520
# mHeight = 20431
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
from selenium.webdriver.chrome.options import Options
def get_chrome():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    return webdriver.Chrome(chrome_options=chrome_options)

def detaail_page(item):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "cna=gY5GE8vPMGACASvgLWesBpgg; l=bBgQUK1lvHlc2bE_BOCg5uI81fb9kIRPguPRwGoei_5Q-1T-JB_OlkIbwe96Vj5P9bYB4R3ZAF9teFmT8PsV.; sm4=110100; enc=xzqpgSiaHaMOi%2BHzY%2BcQ8xIJ6jeSOrGpaJQ3yJ2MJm22hbDyWWnk1saajEjzUU5PAmCn0Kvw4fr%2FIX%2F6FkAhoA%3D%3D; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; uss=""; _m_h5_tk=1c56b3d37cd4403e000ffc74cbf0e4c9_1552207508287; _m_h5_tk_enc=b596a3c994e77edd8777cd0bdb03dc57; hng=CN%7Czh-CN%7CCNY%7C156; t=a3e60ff03b942db42bf59b62b90443e5; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _tb_token_=ff5667554a5e5; cookie2=1773b3ac32e4331c11fb93ca5d48c43d; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpdiBh&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5icOEeoPwA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvz36PVYahQBiM%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; csg=f8aceb36; skt=e95849fa038db48d; cq=ccp%3D0; pnm_cku822=098%23E1hvIvvUvbpvUpCkvvvvvjiPRLqUQjDvPFLhljrCPmPW6jDWP2cpgjYWRLFyQjnvRuwCvvpvvUmmkphvC99vvOHzB4yCvv9vvUm6EuavcbyCvm9vvvvvphvvvvvv9DCvpv1ZvvmmZhCv2CUvvUEpphvWDvvv9DCvpvQomphvLvs599vj7SLXS4ZAhjCwD7zOaXTAVA1l%2BExreTtYcgkQD70wd56JfaBl%2Bb8rwZHlYneYr2E9ZbmxfwoOd5ln%2B8c61EyXJZ%2FQ0f0DW3vCvpvVvvpvvhCv2QhvCvvvMMGtvpvhvvvvvv%3D%3D; isg=BKKiFjT8Cnk00xE-seKqKJII8y6o56wP-FtKO-w7z5XEv0M51IL_HV0t67vmrx6l",
        "referer": "https://list.tmall.com/search_product.htm?q=iiphone+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    # print(item)
    print(item['comment_href'])
    # driver.get()
    if item['comment_href'] != '空':
        # r = requests.get(url=url, headers=headers)
        # # time.sleep(5)
        # # print(r.text)
        # tree = etree.HTML(r.text)
        # 'class="rate-grid"'
        # tr_list = tree.xpath('//div[@class="rate-grid"]/table/tbody/tr')
        # # print(len(tr_list))
        # splash_render(item['comment_href'])
        dirver_get_page(item['comment_href'])
        # chrome 不好使
        # driver = get_chrome()
        # driver.get(item['comment_href'])
        # time.sleep(30)
        # print(driver.page_source)

def splash_render(url):
    splash_url = "http://localhost:8050/render.html"

    args = {
        "url": url,
        "timeout": 5,
        "image": 0
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "cna=gY5GE8vPMGACASvgLWesBpgg; l=bBgQUK1lvHlc2bE_BOCg5uI81fb9kIRPguPRwGoei_5Q-1T-JB_OlkIbwe96Vj5P9bYB4R3ZAF9teFmT8PsV.; sm4=110100; enc=xzqpgSiaHaMOi%2BHzY%2BcQ8xIJ6jeSOrGpaJQ3yJ2MJm22hbDyWWnk1saajEjzUU5PAmCn0Kvw4fr%2FIX%2F6FkAhoA%3D%3D; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; uss=""; _m_h5_tk=1c56b3d37cd4403e000ffc74cbf0e4c9_1552207508287; _m_h5_tk_enc=b596a3c994e77edd8777cd0bdb03dc57; hng=CN%7Czh-CN%7CCNY%7C156; t=a3e60ff03b942db42bf59b62b90443e5; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _tb_token_=ff5667554a5e5; cookie2=1773b3ac32e4331c11fb93ca5d48c43d; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpdiBh&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5icOEeoPwA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvz36PVYahQBiM%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; csg=f8aceb36; skt=e95849fa038db48d; cq=ccp%3D0; pnm_cku822=098%23E1hvIvvUvbpvUpCkvvvvvjiPRLqUQjDvPFLhljrCPmPW6jDWP2cpgjYWRLFyQjnvRuwCvvpvvUmmkphvC99vvOHzB4yCvv9vvUm6EuavcbyCvm9vvvvvphvvvvvv9DCvpv1ZvvmmZhCv2CUvvUEpphvWDvvv9DCvpvQomphvLvs599vj7SLXS4ZAhjCwD7zOaXTAVA1l%2BExreTtYcgkQD70wd56JfaBl%2Bb8rwZHlYneYr2E9ZbmxfwoOd5ln%2B8c61EyXJZ%2FQ0f0DW3vCvpvVvvpvvhCv2QhvCvvvMMGtvpvhvvvvvv%3D%3D; isg=BKKiFjT8Cnk00xE-seKqKJII8y6o56wP-FtKO-w7z5XEv0M51IL_HV0t67vmrx6l",
        "referer": "https://list.tmall.com/search_product.htm?q=iiphone+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }

    response = requests.get(splash_url, params=args, headers=headers)
    # return response.text
    print(response.text)




pcUA = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5']

mWidth = 1440
mHeight = 2000
PIXEL_RATIO = 3.0

mobileEmulation = {"deviceMetrics": {"width": mWidth, "height": mHeight, "pixelRatio": PIXEL_RATIO},
                   "UserAgent": random.choice(pcUA)}  # "userAgent": random.choice(pcUA)

def create_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option('mobileEmulation', mobileEmulation)
    ops.add_argument('--proxy-server=218.60.8.99:3129')
    # ops.add_argument('--headless')
    # ops.add_argument('--disable-gpu')

    web = webdriver.Chrome(chrome_options=ops)
    web.set_page_load_timeout(10)
    web.set_script_timeout(10)
    web.set_window_size(mWidth, mHeight)
    return web


driver = create_chrome()
def dirver_get_page(url):

    driver.maximize_window()

    # driver.get('https://detail.tmall.com/item.htm?id=584865383924&skuId=3951416717001&areaId=110100&user_id=902218705&cat_id=2&is_b=1&rn=289a6a85d6f5c3ca9cb4ea875d191f90&on_comment=1')
    driver.get(url)

    time.sleep(2)
    print(driver.get_cookies())
    time.sleep(20)
    print(driver.page_source)


if __name__ == '__main__':
    key = str(input('请输入关键字：'))
    ul = 'https://list.tmall.com/search_product.htm?q={}+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
    url = ul.format(key)
    first_page(url)
