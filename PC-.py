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


# def writelog(msg, log):
#     nt = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#     text = "[%s] %s " % (nt, msg)
#     os.system("echo %s >> %s" % (text.encode('utf8'), log))


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
# print(driver.get_cookies())
# cook = 'cookie'
# value = 'cna=Tj0GFfQd7WoCAX0jSx7nusPu; enc=oRKYDCU5y1m1VFVbIWUMn2QyXwEqt7CA9BI5KpjgZeRE90sX%2FwrUsIKhOECrqEBmKlG%2B1ZTiHV%2BGjobUqVhjTw%3D%3D; _med=dw:375&dh:667&pw:750&ph:1334&ist:0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; hng=CN%7Czh-CN%7CCNY%7C156; t=b07e9de440f1fb0e3ab2b66e17f7b37a; _tb_token_=53fb9ef3e81ee; cookie2=111d252490c66778480de2076c9fc47b; _uab_collina=155193672433852538332314; swfstore=92842; x5sec=7b22746d616c6c7365617263683b32223a226437353135306166616162383530643634326366326565323761303333366338434a4b72672b5146454a6938753671693538535247786f504d6a49774d44637a4d7a51784f4467344e547335227d; tt=login.tmall.com; cq=ccp%3D0; _m_h5_tk=49a86b858caee07c8da2f5b320428fd1_1551958233749; _m_h5_tk_enc=3472a233e78156946253b38bd2380ad3; res=scroll%3A1585*6302-client%3A1585*410-offset%3A1585*6302-screen%3A1600*900; pnm_cku822=098%23E1hv3vvUvbpvUvCkvvvvvjiPRLzy6j1HRF5h6jnEPmPOljnVPLMUAjlnPszZ1jYWRphvCvvvvvvPvpvhvv2MMQyCvhQpdCQvCsN6YPoxdB9aW4c6D704d5YVtnFZTEIOwZkQ0f0DW3CQog0HsXZpejD2AXcBlLyzOvxrtjc6%2BultE8AUDfyTh7QHYWLh0C%2B4Kphv8vvvvvtvpvvvvvv2UhCvCVIvvvW9phvWh9vvvACvpvQXvvv2UhCv2CeivpvUvvmvrCaXk5JEvpvVmvvCvcaVvphvC9v9vvCvp8wCvvpvvUmm; whl=-1%260%260%260; l=bBxv7lDcvBd4CvYzBOfNKdyzzWbOoIRb4sPP7GHipICP_25p7eR5WZ1YC_T9C3GVw1oDR3yzWgmLBeYBY1f..; isg=BPLyKFIq-o2B_8ZOqUcSY3XyQzG5ffDCA6l-SrzLn6WNT5JJpBDcLGHlP6vWP261; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=Vq8l%2BKCLiYYu&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5boqII3%2F1A%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvxcemrgAbQKyI%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; uss=""; csg=85c7d2ee; skt=30020c8f212a64b9'

# driver.get('https://list.tmall.com')
driver.get(
    'https://detail.tmall.com/item.htm?id=584865383924&skuId=3951416717001&areaId=110100&user_id=902218705&cat_id=2&is_b=1&rn=289a6a85d6f5c3ca9cb4ea875d191f90&on_comment=1')
# cookies = {
#     'access-control-allow-origin': '*',
#     'age': '32161',
#     'ali-swift-global-savetime': '1551888350',
#     'cache-control': 'max-age=31104000,s-maxage=31104000',
#     'content-encoding': 'gzip',
#     'content-length': '49246',
#     'content-md5': '6A/IvftxPNYVdO4F8j0X9A==',
#     'content-type': 'application/javascript',
#     'date': 'Wed, 06 Mar 2019 16:05:50 GMT',
#     'eagleid': '77f9359615519205117826673e',
#     'server': 'Tengine',
#     'status': '200',
#     'timing-allow-origin': '*',
#     'vary': 'Accept-Encoding',
#     'via': 'cache15.l2cn859[0,200-0,H], cache39.l2cn859[0,0], cache8.cn213[0,200-0,H], cache2.cn213[1,0]',
#     'x-cache': 'HIT TCP_MEM_HIT dirn:12:366660859',
#     'x-oss-hash-crc64ecma': '7642643058677396894',
#     'x-oss-object-type': 'Normal',
#     'x-oss-request-id': '5C7FEFDE1233EC5EC05D75D9',
#     'x-oss-server-time': '1',
#     'x-oss-storage-class': 'Standard',
#     'x-source-scheme': 'https',
#     'x-swift-cachetime': '31103968',
#     'x-swift-savetime': 'Wed, 06 Mar 2019 16:06:22 GMT',
#
#     'Origin': 'https://list.tmall.com',
#     'Referer': 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.af6e5cb21bM0ce&brand=30111&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&type=pc',
#     'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#
# }

# driver.add_cookie(cookie_dict=cookies)
# url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.af6e5cb21bM0ce&brand=30111&q=iphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&type=pc'
# url = 'https://detail.tmall.com/item.htm?id=560905201223&skuId=3510680937618&pic=//img.alicdn.com/bao/uploaded/i3/TB1zK1TDOrpK1RjSZFhUNhSdXXa_043502.jpg_560x840Q50s50.jpg_.webp&itemTitle=Apple/%E8%8B%B9%E6%9E%9C%20iPhone%20X&price=6299.00&from=h5'
# driver.get(url=url)
time.sleep(2)
print(driver.get_cookies())
time.sleep(20)
print(driver.page_source)

