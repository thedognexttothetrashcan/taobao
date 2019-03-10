import random
import re

import requests
# from fake_useragent import UserAgent
from lxml import etree
# from pymongo import MongoClient
# ua = UserAgent()
# headers = {'User-Agent': ua.random}
# print(headers)

# from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# driver = webdriver.Chrome(chrome_options=chrome_options)

headers = {
    'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie': 'cna=TMqrFGn+mhcCAd3ZtT4aXbSc; UM_distinctid=167f02b9979202-036eed607db659-10306653-fa000-167f02b997abc9; ali_beacon_id=123.120.105.61.1546929761255.560026.5; ali_ab=221.217.180.12.1547562015612.9; hng=CN%7Czh-CN%7CCNY%7C156; lid=getpricedrop; ali_apache_track=c_mid=b2b-401975615933341|c_lid=getpricedrop|c_ms=1|c_mt=3; l=bBjpGLzRvxNa253iBOfNquI8Ls_O0hRfWsPzw4OMsIB197CiHE_BYHwKS3oMK3Q_E_5h33-rbJTb2dek-m4LSo5..; ad_prefer="2019/02/22 17:30:33"; h_keys="%u957f%u8896t%u6064%u7537#%u536b%u8863%u7537#%u886c%u886b%u7537"; __last_loginid__=getpricedrop; _csrf_token=1551930095355; cookie2=19c4a623bcc6928f99e49a9423d920de; t=8a3c206de6c4e8e30e3113d617ae91e7; _tb_token_=51e33e7f0ba37; __cn_logon_id__=getpricedrop; __cn_logon__=true; csg=8aae9f36; ali_apache_tracktmp=c_w_signed=Y; alicnweb=touch_tb_at%3D1552013315429%7Clastlogonid%3Dgetpricedrop%7ChomeIdttS%3D14920814308255411914194223381290731628%7ChomeIdttSAction%3Dtrue%7Cshow_inter_tips%3Dfalse; isg=BPDwO3uEWHJ70wTTcjeufeh2wbiCkdWAFq8lMupBzstUpZFPkkrmE51U_c1gNYxb',
    # 'referer': 'https://valensina.1688.com/page/offerlist.htm?spm=a261y.7663282.autotrace-topNav.3.32eb38dbikiRHo',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}

ul = 'https://beinuoneiyi.1688.com/page/offerlist.htm?tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=tradenumdown&pageNum={}#search-bar'
# print(url)

proxies = [
    '218.60.8.99:3129',
    # '101.27.23.165:1246'
]

def scrool(url):
    driver.get(url)
    time.sleep(2)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(1)

    content = driver.page_source
    return content

def parse(con):
    # print(con.text)
    time.sleep(10)
    tree = etree.HTML(con.text)
    ol_list = tree.xpath('//ul[@class="offer-list-row"]/li')
    # print(ol_list)
    for o_list in ol_list:
        # 价格
        # price = o_list.xpath('div[3]/div/em/text()')[0]

        # 详情页链接
        url = o_list.xpath('div[4]/a/@href')[0]
        # print(url)

        detail_1(url)


def detail_1(url):
    print(url)
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': 'cna=TMqrFGn+mhcCAd3ZtT4aXbSc; UM_distinctid=167f02b9979202-036eed607db659-10306653-fa000-167f02b997abc9; ali_beacon_id=123.120.105.61.1546929761255.560026.5; ali_ab=221.217.180.12.1547562015612.9; hng=CN%7Czh-CN%7CCNY%7C156; lid=getpricedrop; ali_apache_track=c_mid=b2b-401975615933341|c_lid=getpricedrop|c_ms=1|c_mt=3; l=bBjpGLzRvxNa253iBOfNquI8Ls_O0hRfWsPzw4OMsIB197CiHE_BYHwKS3oMK3Q_E_5h33-rbJTb2dek-m4LSo5..; ad_prefer="2019/02/22 17:30:33"; h_keys="%u957f%u8896t%u6064%u7537#%u536b%u8863%u7537#%u886c%u886b%u7537"; __last_loginid__=getpricedrop; _csrf_token=1551930095355; cookie2=19c4a623bcc6928f99e49a9423d920de; t=8a3c206de6c4e8e30e3113d617ae91e7; _tb_token_=51e33e7f0ba37; __cn_logon_id__=getpricedrop; __cn_logon__=true; csg=8aae9f36; ali_apache_tracktmp=c_w_signed=Y; CNZZDATA1261052687=28746827-1550646506-https%253A%252F%252Fdetail.1688.com%252F%7C1551929608; alicnweb=touch_tb_at%3D1552013315429%7Clastlogonid%3Dgetpricedrop%7ChomeIdttS%3D14920814308255411914194223381290731628%7ChomeIdttSAction%3Dtrue%7Cshow_inter_tips%3Dfalse; CNZZDATA1253659577=207967806-1545921827-https%253A%252F%252Fshangchenbaby.1688.com%252F%7C1552011764; isg=BDk5zZnUQalZRh2YIxjn1mlxSKPT7iz794hcOVtutmDd4lh0o5REycqwYKax2sUw',
        'referer': 'https://detail.1688.com/offer/571127588412.html?spm=a2615.7691456.autotrace-offerGeneral.13.10b4420aRAGLWn',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    con = requests.get(url=url, headers=headers)
    # print(con.text)
    tree = etree.HTML(con.text)
    try:
        try:
            url_2 = tree.xpath('//li[@class="trade-type-has-tip trade-tab-long-text"]/a/@href')[0]
        except:
            url_2 = url
        # print(url_2)
        con = requests.get(url=url_2, headers=headers)
        # print(con2.text)
        tree = etree.HTML(con.text)
        try:
            cost_01 = float(tree.xpath('//td[text()="价格"]/following::*[4]/text()')[0])
        except:
            cost_01 = 0
        try:
            cost_02 = float(tree.xpath('//td[text()="价格"]/following::*[7]/text()')[0])
        except:
            cost_02 = 0
        try:
            cost_03 = float(tree.xpath('//span[text()="价格"]/following::*[2]/text()')[0])
        except:
            cost_03 = 0
        try:
            cost_04 = float(tree.xpath('//span[text()="价格"]/following::*[5]/text()')[0])
        except:
            cost_04 = 0
        try:
            cost_05 = float(tree.xpath('//td[text()="价格"]/following::*[4]/text()')[0])
        except:
            cost_05 = 0
        try:
            cost_06 = float(tree.xpath('//span[text()="2.08"]/following::*[3]/text()')[0])
        except:
            cost_06 = 0

        if cost_02 != 0:
            cost_11 = str(cost_01) + "-" + str(cost_02)
        else:
            cost_11 = str(cost_03) + "-" + str(cost_04)
        list_price_11 = tree.xpath('//div[@class="obj-content"]//td[@class="price"]/span/em[1]/text()')
    except:
        cost_11 = cost_04
        list_price_11 = 0
    detail_2(url, cost_11, list_price_11)


def detail_2(url, cost_11, list_price_11):
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': 'cna=TMqrFGn+mhcCAd3ZtT4aXbSc; UM_distinctid=167f02b9979202-036eed607db659-10306653-fa000-167f02b997abc9; ali_beacon_id=123.120.105.61.1546929761255.560026.5; ali_ab=221.217.180.12.1547562015612.9; hng=CN%7Czh-CN%7CCNY%7C156; lid=getpricedrop; ali_apache_track=c_mid=b2b-401975615933341|c_lid=getpricedrop|c_ms=1|c_mt=3; l=bBjpGLzRvxNa253iBOfNquI8Ls_O0hRfWsPzw4OMsIB197CiHE_BYHwKS3oMK3Q_E_5h33-rbJTb2dek-m4LSo5..; ad_prefer="2019/02/22 17:30:33"; h_keys="%u957f%u8896t%u6064%u7537#%u536b%u8863%u7537#%u886c%u886b%u7537"; __last_loginid__=getpricedrop; _csrf_token=1551930095355; cookie2=19c4a623bcc6928f99e49a9423d920de; t=8a3c206de6c4e8e30e3113d617ae91e7; _tb_token_=51e33e7f0ba37; __cn_logon_id__=getpricedrop; __cn_logon__=true; csg=8aae9f36; ali_apache_tracktmp=c_w_signed=Y; CNZZDATA1261052687=28746827-1550646506-https%253A%252F%252Fdetail.1688.com%252F%7C1551929608; alicnweb=touch_tb_at%3D1552013315429%7Clastlogonid%3Dgetpricedrop%7ChomeIdttS%3D14920814308255411914194223381290731628%7ChomeIdttSAction%3Dtrue%7Cshow_inter_tips%3Dfalse; CNZZDATA1253659577=207967806-1545921827-https%253A%252F%252Fshangchenbaby.1688.com%252F%7C1552011764; isg=BNDQlWNsuNJZMmRzkpeO3YgWoRjiMbXgNs8FUsqhKCvYBXKvcag9c_D33Y1A1Wy7',
        'referer': 'https://detail.1688.com/offer/571127588412.html?spm=a261y.7663282.autotrace-offerDetailContext1.20.293219fepOJfi4&sk=consign',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    list_price_11 = list_price_11
    cost_11 = cost_11
    con_3 = requests.get(url=url, headers=headers)
    # print(con.text)
    tree = etree.HTML(con_3.text)

    # 净重
    try:
        # j_weight = tree.xpath('//div[@class="mod mod-detail-other-attr"]/div/dl/dd/span[1]/em/text()')[0]
        j_weight_pro = tree.xpath('//b[text()="单位重量"]/following::*[1]/text()')[0]
        if j_weight_pro:
            j_weight = j_weight_pro.split(" ")[0]
        else:
            j_weight = 0.1
    except:
        j_weight = 0.1

    # 毛重
    try:
        m_weight_pro = tree.xpath('//b[text()="跨境包裹重量"]/following::*[1]/text()')[0]
        if m_weight_pro:
            m_weight = m_weight_pro.split(" ")[0]
        else:
            m_weight = 0.1
    except:
        m_weight = 0.1


    # 颜色名称
    try:
        color_list_pro_pro_1 = tree.xpath('//td[text()="颜色"]/following::*[1]/text()')[0]
        if color_list_pro_pro_1:
            color_name_pro_1 = ''.join(color_list_pro_pro_1)
            color_name_1 = color_name_pro_1.split(',')
        else:
            color_name_1 = ""
    except:
        color_name_1 = ""

    color_name = color_name_1


    # 颜色链接
    try:
        try:
            time.sleep(5)
            color_src1_pro_1 = tree.xpath('//span[@class="vertical-img"]/span[@class="box-img"]/img/@data-lazy-src')
            print(color_src1_pro_1)
            if color_src1_pro_1 and (len(color_name) == len(color_src1_pro_1)):
                color_src1_list_1 = color_src1_pro_1
                color_src1_list_max_1 = []
                for j in color_src1_list_1:
                    j = str(j)
                    b = j.split(".")
                    q = b[0] + "." + b[1] + "." + b[2] + "." + "160x160" + "." + b[4]
                    color_src1_list_max_1.append(q)


            else:
                color_pro_pro_1 = []
                for i in range(len(color_name)):
                    color_pro_pro_1.append("")
                color_src1_list_max_1 = color_pro_pro_1

        except:
            color_src1_list_max_1 = []
            for i in range(len(color_name)):
                color_src1_list_max_1.append("")
    except:
        print("有问题1")

    try:
        try:
            color_src1_pro_2 = tree.xpath('//div[@class="box-img"]/img/@data-lazy-src')
            if color_src1_pro_2 and (len(color_name) == len(color_src1_pro_2)):
                color_src1_list_2 = color_src1_pro_2
                color_src1_list_max_2 = []
                for j in color_src1_list_2:
                    j = str(j)
                    b = j.split(".")
                    q = b[0] + "." + b[1] + "." + b[2] + "." + "160x160" + "." + b[4]
                    color_src1_list_max_2.append(q)
            else:
                color_pro_pro_2 = []
                for i in range(len(color_name)):
                    color_pro_pro_2.append("")
                color_src1_list_max_2 = color_pro_pro_2

        except:
            color_src1_list_max_2 = []
            for i in range(len(color_name)):
                color_src1_list_max_2.append("")
    except:
        print("有问题2")



    color_src1_list_max_pro_pro = color_src1_list_max_1 + color_src1_list_max_2
    # color_src1_list_max_pro = set(color_src1_list_max_pro_pro)
    # color_src1_list_max = list(color_src1_list_max_pro)
    color_src1_list_max_max = []
    for i in color_src1_list_max_pro_pro:
        if i != '':
            color_src1_list_max_max.append(i)

    if len(color_src1_list_max_max) < 1:
        for i in range(len(color_name)):
            color_src1_list_max_max.append("")



    # 轮播图
    img_list_pro = []
    img_src_pro = tree.xpath('//div[@class="tab-content-container"]/ul/li/div/a/img/@src')
    img_src = list(img_src_pro)
    for i in img_src:
        if i != 'https://cbu01.alicdn.com/cms/upload/other/lazyload.png':
            img_list_pro.append(i)

    img_list = []
    for j in img_list_pro:
        j = str(j)
        a = j.split(".")
        s = a[0]+'.'+a[1]+'.'+a[2]+"."+a[4]
        img_list.append(s)

    cost = cost_11




    # 每款颜色价格
    if list_price_11 != 0:
        list_price = list_price_11
    else:
        list_price = tree.xpath('//div[@class="obj-content"]//td[@class="price"]/span/em[1]/text()')
        if not list_price:
            list_price = "空"

        list_price_pro = []
        if list_price == "空":
            list_price_pro.append(cost)
            list_price = list_price_pro

    # size_list = []
    # size = 'one size'
    # size_list.append(size)

    try:
        size_list_pro_pro_1 = tree.xpath('//td[text()="适合身高"]/following::*[1]/text()')
        if size_list_pro_pro_1:
            size_list_pro_1 = ''.join(size_list_pro_pro_1)
            size_list_1 = size_list_pro_1.split(',')
        else:
            size_list_1 = "One Size"
    except:
        size_list_1 = "One Size"


    size_list_max = []
    if size_list_1:
        size_list_max = size_list_1


    aa = con_3.text
    aa = re.sub(r'&gt;', " ", aa)
    result = re.findall(r'},"(.*?)":{"specId":"(.*?)","skuStorageInfos":"', aa)
    result1 = re.findall(r'"skuMap":{"(.*?)":{"specId":"(.*?)","skuStorageInfos":"', aa)
    try:
        result2 = re.findall(r'"skuMap":{"(.*?)":{"specId":"(.*?)","saleCount"', a)
    except:
        result2 = []
    # num = re.sub(r'&gt;', "", result)
    # print(result)
    # print(result1)
    result = result + result1 +result2
    if result != []:
        # print(result)
        # print(len(result))
        dic1 = dict(result)
        print(dic1)
        specid_list= []
        if size_list_max != "One Size":
            for i in color_name:
                for j in size_list_max:
                    specid_list.append(dic1.get('{} {}'.format(i, j)))
        else:
            for i in color_name:
                specid_list.append(dic1.get(i))

    if result == []:
        result = re.findall(r'"(.*?)":{"canBookCount":(.*?),"discountPrice":"(.*?)","saleCount":(.*?),"skuId":(.*?),"specId":"(.*?)","storageInfos"', aa)
        dic_ll = {}
        for i in result:
            dic_ll[i[0].replace('skuMap":{"', "")] = i[-1]
        specid_list = []
        if size_list_max != "One Size":
            for i in color_name:
                for j in size_list_max:
                    specid_list.append(dic_ll.get('{} {}'.format(i, j)))
        else:
            for i in color_name:
                specid_list.append(dic_ll.get(i))
    try:
        items = {
            'log_url': url,
            'title': title,
            'cost': cost,             # 第一个价格
            'list_price': list_price,   # 每款对应价格
            'net_weight': j_weight,
            'gross_weight': m_weight,
            'color': color_name,
            'color_image': color_src1_list_max_max,
            'images': img_list,
            'size': size_list_max,
            'specid': specid_list

        }
        # save_mongo(items)
        print(items)
    except:
        print("haha")

def save_mongo(items):
    client = MongoClient('localhost', 27017)
    db = client.beinuo_38_1688
    conn = db.beinuo_38_1688
    conn.insert(items)


def main():
    for page in range(1, 3):
        url = ul.format(page)
        print('开始第%s页爬取。。。。。' % page)
        con = requests.get(url=url, headers=headers, proxies={'https': random.choice(proxies)}, timeout=10)
        parse(con)
        print('结束第%s页爬取。。。。。' % page, '\n')
        time.sleep(1)



if __name__ == '__main__':
    main()

# 25
