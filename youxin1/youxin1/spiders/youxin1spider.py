# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request

from youxin1.items import Youxin1Item


class Youxin1spiderSpider(scrapy.Spider):
    name = 'youxin1spider'
    allowed_domains = ['www.xin.com']

    start_url = 'https://www.xin.com'
    def start_requests(self):
        yield Request(url=self.start_url, callback=self.city_url)

    def city_url(self, response):
        '''
        获取每个城市的url后缀
        :param response: start_url
        :return: 城市后缀的url
        '''
        sel = Selector(response)
        city_list = sel.xpath('/html/body/div[21]/div[2]/table/tbody/tr/td/dl/dd/a')
        for city in city_list:
            city_url = city.xpath('./@href').extract()[0].split('/')[1]
            yield Request(url=self.start_url + city_url, callback=self.car_type)

    def car_type(self, response):
        '''
        爬取每个类型车的url
        :param response:
        :return: 每个url的后缀
        '''
        sel = Selector(response)
        type_list = sel.xpath('/html/body/div[2]/div[3]/div[1]/div/a')
        for lis in type_list:
            type_url = lis.xpath('./@href').extract()[0].split('/')[2]
            real_type_urls = self.city_url + type_url

            yield Request(url=real_type_urls, callback=self.page_url)

    def page_url(self, reponse):
        '''
        拿取每个车辆下的详情页面
        :param reponse: 上面的响应
        :return: 详情页面的后缀
        '''

        rep = Selector(reponse)
        urls = rep.xpath('//*[@id="search_container"]/div[1]/ul/li/div[2]/a')
        for url in urls:
            real_url = url.xpath('./@href').extract()[0]
            real_urls = 'https:' + str(real_url)
            yield Request(url=real_urls, callback=self.parse_detail)

        # 判断是否有下一页
        next_url = rep.xpath(
            '//div[@class="con-page search_page_link"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url:
            url = 'https://www.xin.com' + next_url
            # print(url)
            yield Request(url=url, callback=self.page_url)

    def parse_detail(self, response):
        '''
        爬取车辆详情页面信息
        :param response:
        :return:
        '''
        sel = Selector(response)
        car_detail = sel.xpath('/html/body/div[2]/div[2]')
        item = Youxin1Item()
        if car_detail:
            # 标题
            title = sel.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/span/text()').extract_first()
            # 价格
            price = sel.xpath('/html/body/div[2]/div[2]/div[2]/p/span[2]/b/text()').extract_first()
            # 原价
            current_price = sel.xpath('/html/body/div[2]/div[2]/div[2]/p/span[3]/span[2]/b/text()').extract_first()
            # 首付
            payment = sel.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[2]/text()').extract_first()
            # 月供
            month_payment = sel.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[3]/text()').extract_first()
            # 哪一年上牌
            time = sel.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[1]/span[2]/text()').extract_first()
            # 公里数
            kilometer = sel.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[2]/a/text()').extract_first().strip()
            # 排量
            displacement = sel.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[4]/span/text()').extract_first().replace(
                '\n', '')
            item['title'] = title
            item['price'] = price
            item['current_price'] = current_price
            item['payment'] = payment
            item['month_payment'] = month_payment
            item['time'] = time
            item['kilometer'] = kilometer
            item['displacement'] = displacement
        # 图片
        image = sel.xpath('/html/body/div[2]/div[2]/div[1]/img/@src').extract_first()
        # 颜色
        color = sel.xpath('//*[@id="cd_m_clxx"]/div[3]/dl[2]/dd[3]/span[2]/a/text()').extract_first()
        # 车辆类型
        car_type = sel.xpath('//*[@id="cd_m_clxx"]/div[3]/dl[2]/dd[2]/span[2]/a/text()').extract_first()
        # 发动机
        motor = sel.xpath('//*[@id="cd_m_clxx"]/div[3]/dl[3]/dd[1]/span[2]/text()').extract_first()
        # 变速箱 .strip().replace('\n', '')
        gearbox = sel.xpath('//*[@id="cd_m_clxx"]/div[3]/dl[3]/dd[2]/span[2]/a/text()').extract_first()
        # 每个车的唯一id
        car_id = sel.xpath('/html/body/div[2]/div[1]/@data-carid').extract_first()
        area = 'chengdu'

        item['image'] = image
        item['color'] = color
        item['type'] = car_type
        item['motor'] = motor
        item['gearbox'] = gearbox
        item['car_id'] = car_id
        item['area'] = area

        yield item
