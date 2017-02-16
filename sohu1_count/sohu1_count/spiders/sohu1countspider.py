# -*- coding: utf-8 -*-

import scrapy
import json
import logging
from ..items import Sohu1CountItem

logger = logging.getLogger(__name__)

class Sohu1CountSpider(scrapy.Spider):
    name = 'sohu1'
    start_urls = ('http://mp.sohu.com/openapi/profile/getRichInfo?cb=jQuery17108447113800793886_1487135388511&mpId=319379&newsId=480262090&_=1487135389093',
                  'http://changyan.sohu.com/api/2/topic/comments?callback=jQuery17044654883979819715_1487135389660&client_id=cyqemw6s1&page_size=10&topic_id=2532697157&page_no=1&_=1487135390420'
                  )

    def parse(self, response):
        #logger.info(response.body)
        result = response.body
        start_index = result.find('(')
        logger.info('起始下标为：'+str(start_index))
        end_index = result.find(')')
        logger.info('截止下标为：'+str(end_index))
        tmp_jdict = result[start_index+1:end_index]
        logger.info(tmp_jdict)
        #jdict = eval(tmp_jdict)
        jdict = json.loads(tmp_jdict)
        logger.info(jdict)
        jdata = {}
        if jdict.get('data',False):
            jdata = jdict['data']
        #logger.info(jdata)
        item = Sohu1CountItem()
        if jdata.get('newspv',False):
            item['comments_num'] = jdata['newspv']
            logger.info(u"评论数为：" + str(jdata['newspv']))
            fp = open('123.html','w')
            fp.write(response.body)
            yield item
            logger.info(item)
        elif jdict.get('cmt_sum',False):
            item['read_num'] = jdict['cmt_sum']
            logger.info(u"阅读数为：" + str(item['read_num']))
            yield item
