from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from douban_actress_pics.items import DoubanActressPicsItem


class KeikoSpider(CrawlSpider):
    # Spider's name
    name = "keiko_spider"

    # Downloader should wait before 1m until next hitting
    # Incase the website block the visit
    download_delay = 0.5

    # Only allow "douban" domain to be crawled
    # allowed_domains = ['www.douban.com']

    # Crawler will start from this URL
    start_urls = ['https://movie.douban.com/celebrity/1023064/photo/1658140954/']

    # As per this rule, crawl all relevant URLs
    rules = (Rule(LinkExtractor(
            # Crawl all URLs match this regex
            allow=(r'https://movie.douban.com/celebrity/1023064/photo/\d+/.+')),
        # Parse above with the method 'parse_item'
        callback='parse_item',
        follow=True),
    )

    def parse_item(self, response):
        print response

        # Built-in selector to select certain parts of the content
        sel = Selector(response)

        # Extract items based on xpath and assign values to item of KikiSpider's instance
        item = DoubanActressPicsItem()
        item['image_urls'] = sel.xpath('//div[@class="photo-show"]/div/a/img/@src').extract()

        # Yield item
        yield item
