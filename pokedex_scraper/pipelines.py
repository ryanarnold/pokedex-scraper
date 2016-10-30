# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class PokemonPipeline(object):
    def process_item(self, item, spider):
        item['eng_name'] = re.sub(r'.* ', '', item['eng_name'])
        

        return item