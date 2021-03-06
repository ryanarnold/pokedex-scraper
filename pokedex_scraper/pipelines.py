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
        item['height_inches'] = int(item['height_feet'].strip().split('\'')[1].replace('\"', ''))
        item['height_feet'] = int(item['height_feet'].strip().split('\'')[0])
        item['weight_lbs'] = float(re.sub(r'lbs', '', item['weight_lbs'].strip()))
        item['type1'] = item['type1'].replace('/pokedex-rs/', '').replace('.shtml', '')
        item['type2'] = item['type2'].replace('/pokedex-rs/', '').replace('.shtml', '')
        item['classification'] = item['classification'].strip()

        abilities = item['ability'].replace('Ability: ', '')
        item['ability'] = [a.strip() for a in abilities.split('&')]

        item['flavor_text'] = item['flavor_text'].strip()

        return item