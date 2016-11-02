# -*- coding: utf-8 -*-
import scrapy
from pokedex_scraper.items import PokemonItem
import hashlib

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    # allowed_domains = ["serebii.net"]
    start_urls = (
        'http://www.serebii.net/pokedex-xy/001.shtml',
    )
    # allowed_domains = ['localhost']
    # start_urls = (
    # 	'http://localhost/serebii',
    # )

    def parse(self, response):
        pokemon = PokemonItem()
        pokemon['eng_name'] = response.css('table.dextab > tr > td > table > tr > td > font > b::text').extract()[0]
        pokemon['jap_name'] = response.css('table.dextable > tr > td.fooinfo > table > tr > td::text').extract()[1]
        pokemon['national_no'] = response.css('table.dextable > tr > td.fooinfo > table > tr > td::text').extract()[10]
        pokemon['type1'] = response.css('table.dextable > tr > td.cen > a::attr(href)').extract()[0]
        pokemon['type2'] = response.css('table.dextable > tr > td.cen > a::attr(href)').extract()[1]
        pokemon['height_feet'] = response.css('table.dextable > tr > td.fooinfo::text').extract()[2].split('\'')[0]
        pokemon['height_inches'] = response.css('table.dextable > tr > td.fooinfo::text').extract()[2].split('\'')[1]
        pokemon['weight_lbs'] = response.css('table.dextable > tr > td.fooinfo::text').extract()[4]
        pokemon['classification'] = response.css('table.dextable > tr > td.fooinfo::text').extract()[1]
        pokemon['ability'] = response.css('table.dextable > tr > td.fooinfo > a > b::text').extract()[0]
        pokemon['flavor_text'] = response.css('table.dextable > tr > td.fooinfo::text').extract()[24]

        pokemon['image_urls'] = ['http://www.serebii.net/' + response.css('table.art > tr > td > img::attr(src)').extract()[0], ]
        pokemon['url_sha1'] = hashlib.sha1(pokemon['image_urls'][0].encode('utf-8')).hexdigest()

        yield pokemon