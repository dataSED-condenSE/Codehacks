import scrapy
import json
#scrapy runspider scrape.py -o descriptions2.json
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
    name = 'problems'
    p = [tuple(l.split()) for l in open("../Problems.txt", 'r').read().splitlines()]
    p2 = [tuple(l.split()) for l in open("../Problems2.txt", 'r').read().splitlines()]
    print (len(p),len(p2))
    prel = []
    for x in p2:
        if x not in p:
            prel.append(x)
    #prel = [x for x in p2 if x not in p]
    start_urls = [f'https://codeforces.com/contest/{nr}/problem/{letter}' for nr,letter in prel]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'DOWNLOAD_DELAY': 10 # Seconds of delay
        }
    def parse(self, response):
        item = CodeforcesProblemItem()
        item['url']                   = response.request.url
        item['contestId']               = response.request.url.split("/")[-3]
        item['index']                 = response.selector.xpath('//div/@problemindex').extract()[0]
        item['title']                 = response.selector.xpath('//div[@class="header"]/div[@class="title"]/text()')[0].extract()
        item['timeLimit']            = response.selector.xpath('//div[@class="header"]/div[@class="time-limit"]/text()')[0].extract()
        item['memoryLimit']          = response.selector.xpath('//div[@class="header"]/div[@class="memory-limit"]/text()')[0].extract()
        item['inputFile']            = response.selector.xpath('//div[@class="header"]/div[@class="input-file"]/text()')[0].extract()
        item['outputFile']           = response.selector.xpath('//div[@class="header"]/div[@class="output-file"]/text()')[0].extract()
        item['statement']             = response.selector.xpath('//div[@class="problem-statement"]/div')[1].extract()
        item['inputSpecification']   = response.selector.xpath('//div[@class="input-specification"]')[0].extract()
        item['outputSpecification']  = response.selector.xpath('//div[@class="output-specification"]')[0].extract()
        item['sampleTests']          = response.selector.xpath('//div[@class="sample-tests"]/div[@class="sample-test"]/div').extract()
        item['note']                  = response.selector.xpath('//div[@class="note"]/p').extract()
        yield item