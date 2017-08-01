# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib import parse
from jobbole.items import JobboleItem
from jobbole.utils.common import get_md5


class JobboleSpiderSpider(scrapy.Spider):
    name = 'jobbole_spider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # 1.获取当前页面所有文章url，并进行处理
        post_nodes = response.css('.post .post-thumb a')
        for post_node in post_nodes:
            post_url = post_node.css('::attr(href)').extract_first("")  # 括号内部是默认值
            face_url = post_node.css('img::attr(src)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_post,
                          meta={"face_url": face_url})  # 通过meta可以传递额外的源信息, 在reponse中拿到
            # urljoin方解决url绝对路径和相对路径的问题
            # URLjoin函数中，后者如果有域名则前面的参数对后面的值就不会有影响

            # 2. 获取下一页url进行处理
            # next_url = response.xpath('//div[contains(@class, "navigation")]/a[contains(@class,"next page-numbers")]['
            #                           '1]//@href')[0].extract()
            # if next_url:
            #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_post(self, response):
        title = response.xpath('//div[@class="entry-header"]/h1/text()')[0].extract()
        post_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')[0].extract().strip()
        tags = [item.extract() for item in response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()')]
        source_url = response.xpath('//div[@class="copyright-area"]/a[1]/@href')[0].extract()
        upvote_count = response.xpath('//i[@class="fa  fa-thumbs-o-up"]/following-sibling::h10[1]/text()')
        upvote_count = upvote_count[0].extract() if len(upvote_count) > 0 else '0'
        comment_count = response.xpath('//i[@class="fa fa-comments-o"]/following-sibling::h10[1]/text()')
        comment_count = comment_count[0].extract() if len(comment_count) > 0 else '0'
        face_url = response.meta.get('face_url', "")  # meta是response的属性，通过get来获取值
        id = response.url

        item = JobboleItem()
        item['title'] = title
        item['post_time'] = post_time
        item['tags'] = tags
        item['source_url'] = source_url
        item['upvote_count'] = upvote_count
        item['comment_count'] = comment_count
        item['face_url'] = [face_url]  # 通过pipline下载，url必须是一个列表形式！！
        item['id'] = get_md5(response.url)
        yield item  # 使用yield而不是return，将item传递到pipline中进行处理
