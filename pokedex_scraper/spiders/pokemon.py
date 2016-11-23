# -*- coding: utf-8 -*-
import scrapy
from pokedex_scraper.items import PokemonItem
import hashlib
import re

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    allowed_domains = ["serebii.net"]
    start_urls = ['http://serebii.net/pokedex-rs/' + ('0' * (3 - len(str(x)))) + str(x) + '.shtml' for x in range(1, 387)]
    # allowed_domains = ['localhost']
    # start_urls = (
    # 	'http://localhost/serebii',
    # )

    def parse(self, response):
        pokemon = PokemonItem()
        pokemon['eng_name'] = response.css('table.dextab > tr > td > table > tr > td > font > b::text').extract_first()
        pokemon['jap_name'] = response.xpath('//table[@width="98%"][1]/tr[2]/td[5]/text()').extract()[1]
        pokemon['national_no'] = response.xpath('//table[@width="98%"][1]/tr[2]/td[2]/text()').extract_first()
        pokemon['type1'] = response.xpath('//table[@width="98%"][1]/tr[8]/td[2]/div/a/@href').extract_first()
        pokemon['type2'] = response.xpath('//table[@width="98%"][1]/tr[8]/td[3]/div/a/@href').extract_first()
        pokemon['height_feet'] = response.xpath('//table[@width="98%"][1]/tr[8]/td[4]/text()').extract_first()
        pokemon['weight_lbs'] = response.xpath('//table[@width="98%"][1]/tr[8]/td[5]/text()').extract_first()
        pokemon['classification'] = response.xpath('//table[@width="98%"][1]/tr[8]/td[1]/text()').extract_first()
        pokemon['ability'] = response.xpath('//table[@width="98%"][1]/tr[3]/td[2]/b/text()').extract_first()
        pokemon['flavor_text'] = response.xpath('//table[@width="98%"][3]/tr[2]/td[2]/text()').extract_first()

        pokemon['image_urls'] = ['http://serebii.net' + response.xpath('//table[@width="98%"][1]/tr[3]/td[1]/div/table/tr/td/img/@src').extract_first(),]
        pokemon['url_sha1'] = hashlib.sha1(pokemon['image_urls'][0].encode('utf-8')).hexdigest() 

        yield pokemon