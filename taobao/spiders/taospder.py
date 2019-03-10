# -*- coding: utf-8 -*-
import scrapy


class TaospderSpider(scrapy.Spider):
    name = 'taospder'
    # allowed_domains = ['www.baidu.com/']
    allowed_domains = ['www.tmall.com/']
    # start_urls = ['https://list.tmall.com/search_product.htm?q=%CA%B3%C6%B7&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton']
    # start_urls = ['https://www.baidu.com/']
    start_urls = ['https://login.tmall.com/?spm=a220m.1000858.a2226mz.2.13ef7adcc7KkXn&redirectURL=https%3A%2F%2Flist.tmall.com%2Fsearch_product.htm%3Fq%3D%25CA%25B3%25C6%25B7%26type%3Dp%26spm%3Da220m.1000858.a2227oh.d100%26from%3D.list.pc_1_searchbutton']

    # def start_requests(self):
    #     post_url = 'https://cn.bing.com/ttranslationlookup?&IG=8F83182E45744ED6A39A628938C5E6E2&IID=translator.5036.1'
    #     # 表单数据
    #     formdata = {
    #         'from': 'zh-CHS',
    #         'to': 'en',
    #         'text': '土豆',
    #     }
    #     # 发送post请求
    #     yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        print('['*100)
        print(response.text)

        print('[' * 100)