from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from vacancy_parse import settings
from vacancy_parse.spiders.hh_parse import HhParseSpider
from vacancy_parse.spiders.superjob_parse import SuperjobParseSpider

if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(HhParseSpider)
    crawl_proc.crawl(SuperjobParseSpider)
    crawl_proc.start()