# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class PokemonPipeline(object):
    def process_item(self, item, spider):
        item['eng_name'] = re.sub(r'.* ', '', item['eng_name'])
        item['height_feet'] = int(item['height_feet'])
        item['height_inches'] = int(item['height_inches'].replace('"', ''))
        item['national_no'] = int(re.sub(r'\#0*', '', item['national_no']))
        item['weight_lbs'] = float(re.sub(r'lbs', '', item['weight_lbs']))

        return item