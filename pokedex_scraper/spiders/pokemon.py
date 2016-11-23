# -*- coding: utf-8 -*-
import scrapy
from pokedex_scraper.items import PokemonItem
import hashlib
import re

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    allowed_domains = ["serebii.net"]
    start_urls = ['http://serebii.net/pokedex-rs/' + ('0' * (3 - len(str(x)))) + str(x) + '.shtml' for x in range(1, 152)]
    # allowed_domains = ['localhost']
    # start_urls = (
    # 	'http://localhost/serebii',
    # )

    def parse(self, response):
        pokemon = PokemonItem()
        pokemon['eng_name'] = response.css('table.dextab > tr > td > table > tr > td > font > b::text').extract_first()

        yield pokemon