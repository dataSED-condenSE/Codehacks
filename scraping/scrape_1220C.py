import scrapy
import json
#scrapy runspider scrape_1220C.py -o descriptions.json
#-o appends
#-O overwrites
class CodeforcesProblemItem(scrapy.Item):

    url                     = scrapy.Field()
    contestId               = scrapy.Field()
    index                   = scrapy.Field()
    title                   = scrapy.Field()
    timeLimit               = scrapy.Field()
    memoryLimit             = scrapy.Field()
    inputFile               = scrapy.Field()
    outputFile              = scrapy.Field()
    statement               = scrapy.Field()
    inputSpecification      = scrapy.Field()
    outputSpecification     = scrapy.Field()
    sampleTests             = scrapy.Field()
    note                    = scrapy.Field()


class ProblemSpider(scrapy.Spider):
    name = 'problem-spider'
    start_urls = ['https://codeforces.com/contest/1220/problem/C']
    custom_settings = {
        'DOWNLOAD_DELAY': 6 # 2 seconds of delay
        }
    def parse(self, response):
        item = CodeforcesProblemItem()
        item['url']                   = response.request.url
        item['contestId']               = response.request.url.split("/")[-3]
        item['index']                 = response.selector.xpath('//div/@problemindex').extract()[0]
        item['title']                 = response.selector.xpath('//div[@class="header"]/div[@class="title"]/text()')[0].extract()
        item['timeLimit']            = response.selector.xpath('//div[@class="header"]/div[@class="time-limit"]/text()')[0].extract()
        item['memoryLimit']          = response.selector.xpath('//div[@class="header"]/div[@class="memory-limit"]/text()')[0].extract()
        item['inputFile']            = "standard input"
        item['outputFile']           = "standard output"
        item['statement']             = response.selector.xpath('//div[@class="problem-statement"]/div')[1].extract()
        item['inputSpecification']   = response.selector.xpath('//div[@class="input-specification"]')[0].extract()
        item['outputSpecification']  = response.selector.xpath('//div[@class="output-specification"]')[0].extract()
        item['sampleTests']          = response.selector.xpath('//div[@class="sample-tests"]/div[@class="sample-test"]/div').extract()
        item['note']                  = response.selector.xpath('//div[@class="note"]/p').extract()
        yield item