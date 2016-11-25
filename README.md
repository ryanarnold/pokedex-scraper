Pokedex Scraper
=============

This is a web crawler for scraping the pokedex data found in serebii.net, a fan-made website for the immensely popular Pokemon media franchise.

## Installing

To install, simply clone the repo on your system,

`$ git clone https://github.com/ryanarnold/pokedex_scraper.git`

Make sure that you have scrapy installed on your python environment.

## Usage

To begin crawling, open your terminal on the root project directory (`pokedex_scraper/`) and enter,

`$ scrapy crawl pokemon`

Scraped items will be written on a JSON file, located at `pokedex_scraper/feed_exports/`.

To change which pokemon will be scraped, modify the `start_urls` property from `PokemonSpider` in `pokemon.py`.

**Example:** The following code snippet will make the crawler scrape Pokemon#001 up to Pokemon#386 (i.e., all Gen III pokemon).

~~~
start_urls = [
	'http://serebii.net/pokedex-rs/' + ('0' * (3 - len(str(x)))) + str(x) + '.shtml' 
	for x in range(1, 387)
]
~~~