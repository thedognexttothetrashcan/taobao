import requests
from lxml import etree

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
url = 'https://list.tmall.com/search_product.htm?q=iiphone+x&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
def first_page():
    r = requests.get(url=url, headers=headers)
    # print(r.text)
    tree = etree.HTML(r.text)
    div = tree.xpath('//div[@class="product-iWrap"]')
    item = {}

    for li in div:

        # 价格
        price = li.xpath('./p/em/text()')[0]
        # 产品id
        # property_id = li.xpath('./@data-id')[0]
        # # 店名
        # shop_name = str(li.xpath('.//div[@class="productShop"]/a/text()')[0]).strip('\n')
        # # 商品详情链接
        # product_href = 'http:' + li.xpath('.//div[@class="productImg-wrap"]/a/@href')[0]
        # # 商品名字
        # product_name = li.xpath('.//p[@class="productTitle"]/a/@title')[0]
        # # 月成交
        # try:
        #     mon_sales = li.xpath('.//p[@class="productStatus"]/span[1]/em/text()')[0]
        # except Exception as e:
        #     mon_sales = '空'
        # # 评价链接
        # try:
        #     common_href = 'http:' + str(li.xpath('.//p[@class="productStatus"]/span[2]/a/@href')[0])
        # except Exception as e:
        #     common_href = '空'
        # # 商品次数
        # try:
        #     common_count = str(li.xpath('.//p[@class="productStatus"]/span[2]/a/text()')[0])
        # except Exception as e:
        #     common_count = '空'
        # # print(item)
        item['price'] = price
        # item['property_id'] = property_id
        # item['shop_name'] = shop_name
        # item['product_href'] = product_href
        # item['product_name'] = product_name
        # item['mon_sales'] = mon_sales
        # item['common_href'] = common_href
        # item['common_count'] = common_count
        # print(item)
        print('sdsd')

        yield item

def detaail_page():
    item = first_page()
    print(item)



if __name__ == '__main__':
    first_page()