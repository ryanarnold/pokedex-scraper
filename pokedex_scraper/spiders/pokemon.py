# -*- coding: utf-8 -*-
import scrapy
from pokedex_scraper.items import PokemonItem


class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    # allowed_domains = ["serebii.net"]
    # start_urls = (
    #     'http://www.serebii.net/pokedex-xy/001.shtml',
    # )
    allowed_domains = ['localhost']
    start_urls = (
    	'http://localhost/serebii',
    )

    def parse(self, response):
        pokemon = PokemonItem()
        pokemon['eng_name'] = response.css('table.dextab > tbody > tr > td > table > tbody > tr > td > font > b::text').extract()[0]
        pokemon['jap_name'] = response.css('table.dextable > tbody > tr > td.fooinfo > table > tbody > tr > td::text').extract()[1]
        pokemon['national_no'] = response.css('table.dextable > tbody > tr > td.fooinfo > table > tbody > tr > td::text').extract()[10]
        pokemon['type1'] = response.css('table.dextable > tbody > tr > td.cen > a::attr(href)').extract()[0]
        pokemon['type2'] = response.css('table.dextable > tbody > tr > td.cen > a::attr(href)').extract()[1]
        pokemon['height'] = response.css('table.dextable > tbody > tr > td.fooinfo::text').extract()[2]
        pokemon['weight'] = response.css('table.dextable > tbody > tr > td.fooinfo::text').extract()[4]
        pokemon['classification'] = response.css('table.dextable > tbody > tr > td.fooinfo::text').extract()[1]
        pokemon['ability'] = response.css('table.dextable > tbody > tr > td.fooinfo > a > b::text').extract()[0]
        pokemon['flavor_text'] = response.css('table.dextable > tbody > tr > td.fooinfo::text').extract()[24]

        return pokemon