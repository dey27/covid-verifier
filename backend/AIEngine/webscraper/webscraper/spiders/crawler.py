from datetime import datetime
from dateutil import parser

import pandas as pd
import scrapy
from scrapy.utils.project import get_project_settings


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.google.com']
    rss_url_format = "https://news.google.com/rss/search?q="
    query_list = [
        'environmental initiatives india',
        'environmental initiatives beach cleaning india mumbai',
    ]

    settings = get_project_settings()
    base_dir = settings.get('PROJECT_ROOT')
    output_file = base_dir + '/scrapedData/' + name + '.csv'
    headers = ['title', 'url', 'article_text', 'date_crawled', 'date_published', 'is_processed']
    dataDf = pd.DataFrame(columns=headers)

    def start_requests(self):
        for query in self.query_list:
            url = self.rss_url_format + "{" + query + "}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = response.xpath('//channel/item')

        for item in items:
            scraped_info = {
                'title': item.xpath('title/text()').extract_first(),
                'url': item.xpath('link//text()').extract_first(),
                'article_text': '',
                'date_crawled': datetime.now(),
                'date_published': self.parse_date(item.xpath('pubDate//text()').extract_first()),
                'is_processed': False,
            }
            self.dataDf = self.dataDf.append(scraped_info, ignore_index=True)
            self.dataDf.to_csv(self.output_file, sep=',', encoding='utf-8')
            yield scraped_info

    def parse_date(self, date):
        if date:
            return parser.parse(date)
        return None
