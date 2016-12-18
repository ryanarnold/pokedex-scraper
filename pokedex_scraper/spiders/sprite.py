# -*- coding: utf-8 -*-
import scrapy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, update
from pokedex_scraper.items import SpriteItem
import hashlib


class SpriteSpider(scrapy.Spider):
    name = "sprite"
    allowed_domains = ["serebii.net"]

    engine = create_engine('mysql+pymysql://root:@localhost/pokedex', pool_recycle=3600)
    conn = engine.connect()
    metadata = MetaData()
    pokemon = Table('pokemon', metadata, autoload=True, autoload_with=engine)

    def start_requests(self):
        query = select([self.pokemon])
        results = self.conn.execute(query)

        urls = [
            # 'http://www.serebii.net/pokedex-xy/' + ('0' * (3 - len(str(a.national_number)))) + str(a.national_number) + '.shtml' for a in results
            'http://www.serebii.net/pokedex-xy/001.shtml'
        ]
        return [scrapy.Request(url, callback=self.parse) for url in urls]

    def parse(self, response):
        sprite = SpriteItem()

        for i in range(1, 387):
            sprite['file_urls'] = ['http://www.serebii.net/art/th/' + str(i) + '.png',]
            sprite['url_sha1'] = hashlib.sha1(sprite['file_urls'][0].encode('utf-8')).hexdigest() 

            query = update(self.pokemon).where(self.pokemon.c.national_number == i).values(image_sha1=sprite['url_sha1'])
            self.conn.execute(query)

            yield sprite