from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leroymerlin import settings
from leroymerlin.spiders.leroymerlin_parse import LeroymerlinParseSpider

if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(LeroymerlinParseSpider)
    crawl_proc.start()