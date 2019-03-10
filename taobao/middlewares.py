# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import time

from scrapy import signals


class TaobaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TaobaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomIPMiddleware(object):
    def __init__(self):
        self.ip_pool = self.getip()


    def getip(self):
        return [
            '218.60.8.99:3129',
            '113.200.56.13:8010',
            '140.143.96.216:80',
        ]

    def process_request(self, request, spider):
        # 随机一个ip
        self.ip = random.choice(self.ip_pool)
        print('*' * 100)
        print('当前使用的ip为--%s--' % self.ip)
        print('*' * 100)
        request.meta['proxy'] = 'http://' + self.ip
        request.meta['download_timeout'] = 5

    def process_exception(self, request, exception, spider):
        print('#' * 100)
        print(exception)
        print('#' * 100)
        # 删除不可用代理
        self.ip_pool.remove(self.ip)
        if len(self.ip_pool) < 5:
            self.ip_pool = self.getip()
        # 让request重新发送
        return request


class RandomUAMiddleware(object):
    def __init__(self):
        self.ua_list = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
        ]

    # 每次发请求都会调用这个函数
    def process_request(self, request, spider):
        # 从上面的列表中随机抽取一个ua
        ua = random.choice(self.ua_list)
        # print('*' * 100)
        # print('当前使用的ua为--%s--' % ua)
        # print('*' * 100)

        # 给请求添加这个头部
        request.headers.setdefault('User-Agent', ua)




# from lxml import etree
from pyvirtualdisplay import Display

from scrapy import signals
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from logging import getLogger
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# from qq.ua import uas_dict
# from qq.utils import Mysql
chrome_n=no_se_n=0

class Selenium_Chrome_Middleware():
    # display = Display(visible=0, size=(800, 800))
    # display.start()
    chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # path = r'/home/kou/soft/chromedriver'
    path = r'/usr/bin/chromedriver'
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

    def __init__(self):
        self.logger = getLogger(__name__)
        # self.mysql = Mysql()


    def __del__(self):
        self.driver.close()

    def process_request(self,request,spider):
        """
        用PhantomJS抓取页面
        :param request:
        :param spider:
        :return: HtmlResponse
        """

        # if not request.meta.get('index'):

        global chrome_n
        chrome_n += 1

        self.logger.info('chrome_headless浏览器 正在启动...%d' % chrome_n)
        try:
            self.driver.get(request.url)
            # login = self.driver.find_element_by_class_name('forget-pwd').click()
            # login = self.driver.find_element_by_id('J_Static2Quick')
            # login.click()
            time.sleep(3)
            self.driver.save_screenshot('b0.png')
            login = self.driver.find_element_by_id('J_Quick2Static')
            # login = driver.find_element_by_class_name('forget-pwd J_Quick2Static')
            login.click()
            print('kjgkjgk')
            time.sleep(3)
            self.driver.save_screenshot('ta11212.png')
            time.sleep(3)
            # myinput = self.driver.find_element_by_id('kw')
            # 往框里面写内容
            # myinput.send_keys('气质美女')
            # time.sleep(3)
            # self.driver.save_screenshot('baidu1.png')

            # 点击百度一下
            # mybutton = self.driver.find_element_by_id('su')
            # time.sleep(3)
            # mybutton.click()
            # time.sleep(3)
            # self.driver.implicily_wait(10)
            # self.driver.save_screenshot('baidu2.png')
            js = 'document.body.scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(5)
            self.driver.save_screenshot('douban2.png')
            # time.sleep(4)
            # print('6767'*100)

            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',status=200)

        except TimeoutException:
            print('6767'*100)
            return HtmlResponse(url=request.url, status=500, request=request)
        # else:
        #
        #     global no_se_n
        #     no_se_n += 1
        #
        #     self.logger.info('不走selenium中间件...%d' % no_se_n)
        #     return None


