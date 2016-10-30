# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class PokemonItem(Item):
    eng_name = Field()
    jap_name = Field()
    national_no = Field()
    type1 = Field()
    type2 = Field()
    height = Field()
    weight = Field()
    classification = Field()
    ability = Field()
    flavor_text = Field()