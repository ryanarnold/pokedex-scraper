# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class PokemonPipeline(object):
    def process_item(self, item, spider):
        item['eng_name'] = re.sub(r'.* ', '', item['eng_name'])
        item['jap_name'] = item['jap_name'].strip()
        item['national_no'] = int(item['national_no'].strip())
        # item['height_feet'] = int(item['height_feet'])
        # item['height_inches'] = int(item['height_inches'].replace('"', ''))
        # item['weight_lbs'] = float(re.sub(r'lbs', '', item['weight_lbs']))
        # item['type1'] = item['type1'].replace('/pokedex-xy/', '').replace('.shtml', '')
        # item['type2'] = item['type2'].replace('/pokedex-xy/', '').replace('.shtml', '')

        return item