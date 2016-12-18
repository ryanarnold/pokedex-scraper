# -*- coding: utf-8 -*-
import scrapy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, update


class AbilitySpider(scrapy.Spider):
    name = "ability"
    allowed_domains = ["serebii.net"]

    engine = create_engine('mysql+pymysql://root:@localhost/pokedex', pool_recycle=3600)
    conn = engine.connect()
    metadata = MetaData()
    ability = Table('ability', metadata, autoload=True, autoload_with=engine)

    def start_requests(self):
        query = select([self.ability])
        results = self.conn.execute(query)

        urls = [
            'http://serebii.net/abilitydex/' + a.name.lower().replace(' ', '') + '.shtml' for a in results
        ]
        return [scrapy.Request(url, callback=self.parse) for url in urls]

    def parse(self, response):
        name = response.xpath('//table[@class="dextable"]/tr/td/font/b/text()').extract_first().upper()
        desc = response.xpath('//table[@class="dextable"]/tr[4]/td[1]/text()').extract_first()

        print(name)
        print(desc)
        query = update(self.ability).where(self.ability.c.name == name).values(description=desc)
        self.conn.execute(query)