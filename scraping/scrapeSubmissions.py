import scrapy
import json
#scrapy runspider scrapeSubmissions.py -o submissions.json
#-o appends
#-O overwrites
class CodeforcesSubmissionItem(scrapy.Item):
    submissionID             = scrapy.Field()
    programmingLanguage      = scrapy.Field()
    code                     = scrapy.Field()


#https://stackoverflow.com/questions/18920930/scrapy-python-set-up-user-agent
    #https://www.whatismybrowser.com/guides/the-latest-user-agent/
    #https://www.simplified.guide/scrapy/change-user-agent#:~:text=Open%20the%20configuration%20file%20of,using%20your%20preferred%20text%20editor.&text=Search%20for%20the%20USER_AGENT%20option.&text=Uncomment%20the%20line%20and%20set,agent%20for%20your%20Scrapy%20spider.
    


class SubmissionSpider(scrapy.Spider):
    name = 'submission-spider'
    urls = [l for l in open("../crawlCluster/urls_to_crawl.txt", 'r').read().splitlines()]
    start_urls = ['https://codeforces.com' + u for u in urls[:50]]
    #start_urls = ["https://codeforces.com/contest/538/submission/10878400"]
    custom_settings = {
        'DOWNLOAD_DELAY': 5 # Seconds of delay
        }
    def parse(self, response):
        submission_code = response.xpath('//pre[@id="program-source-text"]/text()').extract()
        item = CodeforcesSubmissionItem()
        #test = response.selector.xpath('//div[@class="datatable"]')
        # test = response.xpath('//table[@class=""]//tr//td/text()').extract()
        # print (test)
        # test2 = response.xpath('//table[@class=""]//tr//td').extract()
        # print (test2)
        tds = response.xpath('//table[@class=""]//tr//td')
        data = [td.xpath('.//text()').extract_first().strip() for td in tds]
        data = [x for x in data if x]
        item['submissionID'] = data[0]
        item['programmingLanguage'] = data[2]
        item['code']                   = submission_code
        yield item