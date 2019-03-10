import random
import time

import requests
from lxml import etree

proxies = [
    # '218.60.8.99:3129',
    # '101.27.23.165:1246'
    "49.70.212.234:4207",
    "153.101.245.181:2589",
    "49.70.217.167:4207",
    "114.229.62.201:4203",
    "114.229.240.169:4203",
    "58.217.52.52:4207",
    "117.90.217.51:4207",
    "114.229.58.86:4207",
    "49.70.213.208:4207",
    "153.101.240.121:2589",

]

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "cache-control": "max-age=0",
#     "cookie": "cna=gY5GE8vPMGACASvgLWesBpgg; _med=dw:1440&dh:900&pw:1440&ph:900&ist:0; l=bBgQUK1lvHlc2bE_BOCg5uI81fb9kIRPguPRwGoei_5Q-1T-JB_OlkIbwe96Vj5P9bYB4R3ZAF9teFmT8PsV.; sm4=110100; enc=xzqpgSiaHaMOi%2BHzY%2BcQ8xIJ6jeSOrGpaJQ3yJ2MJm22hbDyWWnk1saajEjzUU5PAmCn0Kvw4fr%2FIX%2F6FkAhoA%3D%3D; _uab_collina=155187561517221955690883; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; hng=CN%7Czh-CN%7CCNY%7C156; tk_trace=1; t=a3e60ff03b942db42bf59b62b90443e5; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _tb_token_=31be3e73997e5; cookie2=1b8f21a5c9e506e84e656d60295a13a5; _m_h5_tk=cfb444dcbb06a43d4a577b24234b80b0_1552150173904; _m_h5_tk_enc=ce73ae367db4d19a16f655f333eaa140; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UtASsssmfufd&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5iTLQ9MXPA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvz1X9YYE1xpaY%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; uss=""; csg=f378d88d; skt=5f3a54dd35a3edd2; tt=38.tmall.com; cq=ccp%3D0; res=scroll%3A1440*6307-client%3A1440*789-offset%3A1440*6307-screen%3A1440*900; pnm_cku822=098%23E1hv6pvUvbpvUvCkvvvvvjiPRLqh6jiPn2F91jljPmPwzjYPPLMvtjYbP2Sp6jrPiQhvChCvCCpEvpCWpaxtv8Wqb6OyCWmQ%2Bul1pC69D76fdeQEVAdwaXgffvyf8KBl53D%2BmB%2Bulj7Jh7EREcqhs8TJwHQiHWLWei307FXXiXhpVj%2BOUx8x9UyCvvXmp99We1eivpvUphvhiLj%2BoNKtvpvIphvvvvvvphCvpComvvC2xyCvHUUvvhPjphvZ99vvp0CvpComvvC21QhCvvXvppvvvvvPvpvhvv2MMsyCvvBvpvvv; isg=BHNzIMlqK5l8euBRuAnrb9tzAnFdABg9YZCblCUQwxLJJJPGrXqrugO22hRvhF9i",
#     "referer": "https://list.tmall.com/search_product.htm?q=%C8%FD%D0%C7&type=p&vmarket=&spm=a211oj.12556964.a2227oh.d100&xl=sanxing_1&from=..pc_1_suggest",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
# }

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=gY5GE8vPMGACASvgLWesBpgg; _med=dw:1440&dh:900&pw:1440&ph:900&ist:0; l=bBgQUK1lvHlc2bE_BOCg5uI81fb9kIRPguPRwGoei_5Q-1T-JB_OlkIbwe96Vj5P9bYB4R3ZAF9teFmT8PsV.; sm4=110100; enc=xzqpgSiaHaMOi%2BHzY%2BcQ8xIJ6jeSOrGpaJQ3yJ2MJm22hbDyWWnk1saajEjzUU5PAmCn0Kvw4fr%2FIX%2F6FkAhoA%3D%3D; _uab_collina=155187561517221955690883; lid=%E6%8F%90%E6%96%AF%E6%8B%89%E7%88%B8%E7%88%B8; hng=CN%7Czh-CN%7CCNY%7C156; tk_trace=1; t=a3e60ff03b942db42bf59b62b90443e5; tracknick=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; lgc=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; _tb_token_=31be3e73997e5; cookie2=1b8f21a5c9e506e84e656d60295a13a5; _m_h5_tk=cfb444dcbb06a43d4a577b24234b80b0_1552150173904; _m_h5_tk_enc=ce73ae367db4d19a16f655f333eaa140; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UtASsssmfufd&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5iTLQ9MXPA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvz1X9YYE1xpaY%3D&id2=UUphyu7opSokkbNd8Q%3D%3D&nk2=r7Qc2M7TAvy3RA%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2200733418885; cookie1=W80vOuO9AY8m2yPvjGw2CQE%2B%2Bjh7a7z5PnzPvOgtEs0%3D; login=true; cookie17=UUphyu7opSokkbNd8Q%3D%3D; _nk_=%5Cu63D0%5Cu65AF%5Cu62C9%5Cu7238%5Cu7238; uss=""; csg=f378d88d; skt=5f3a54dd35a3edd2; cq=ccp%3D0; res=scroll%3A1440*6137-client%3A1440*789-offset%3A1440*6137-screen%3A1440*900; x5sec=7b22746d616c6c7365617263683b32223a226364383366363066656166666539306137323030323566356433633766653433434f6d316a2b5146454a486b754c717677664f3164426f504d6a49774d44637a4d7a51784f4467344e547378227d; pnm_cku822=098%23E1hv6vvUvbpvUpCkvvvvvjiPRLqh6jt8R2MWtjD2PmPWzjtUPLM9tjEbnLsv1jrmR8wCvvpvvUmmRphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphvEvpCW2Hl1vva6DO29T2eAnhjEKOmD5dUf8r1lGE7rV16s%2BX7t5LI6N6S9tRLIVBizBb2XS4ZAhjCbFOcnDBmwJ9kx6acEn1vDNr1lYE7refyCvm9vvvvvphvvvvvv9DCvpv1ZvvmmZhCv2CUvvUEpphvWFvvv9DCvpvQouphvmvvv9bpFW8%2BEkphvC99vvOHzBp%3D%3D; isg=BAkJbT1NsTs2VEpTtmehjf2FGDOj_uLf0LUXFKt-h_Av8isE9KbeWKcgMBBhqpXA',
    'referer': 'https://s.m.tmall.com/m/searchbar.htm?searchType=default',
    'upgrade-insecure-requests': '1',
    # 'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'User-Agent': 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
}
# ul = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.ffe373a4trPu0A&brand=81156&s={}&q=%C8%FD%D0%C7s9&sort=s&style=g&from=.list.pc_1_suggest&suggest=0_4&smAreaId=110100&type=pc#J_Filter'
ul='http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016¤tPage=1'


# def parse(con):
#     time.sleep(10)
#     print(con.text)
    # tree = etree.HTML(con.text)
    # print(tree)
    # ol_list = tree.xpath('//div[@id="J_ItemList"]')
    # ol_list = tree.xpath('//*[@id="J_ItemList"]/div/div//p/em/text()')
    # ol_list = tree.xpath('//*[@id="J_ItemList"]/div//div/p[4]/span/em/text()')
    # print(ol_list)
    # for o_list in ol_list:
    #     print(o_list)
    #     # 价格
    #     price = o_list.xpath('./p[@class="productPrice"]/@title')[0]
    #     print(price)
    #
    #     # 详情页链接
    #     url = o_list.xpath('div[4]/a/@href')[0]
    #     # print(url)
    #
    #     detail_1(url)


def main():
    # for page in range(300, 1000, 60):
    #     url = ul.format(page)
    #     print('开始第%s页爬取。。。。。' % (page / 60))
    con = requests.get(url=ul, headers=headers, timeout=10)
    print(con.text)
        # time.sleep(5)
        # parse(con)
        # print('结束第%s页爬取。。。。。' % (page / 60), '\n')
        # time.sleep(1)


if __name__ == '__main__':
    main()
