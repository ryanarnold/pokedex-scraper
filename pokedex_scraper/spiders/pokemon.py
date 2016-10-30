# -*- coding: utf-8 -*-
import scrapy


class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    allowed_domains = ["serebii.net"]
    start_urls = (
        'http://www.serebii.net/',
    )

    def parse(self, response):
        pass
