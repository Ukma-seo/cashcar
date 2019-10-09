# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    mileage_value = scrapy.Field()
    mileage_unitcode = scrapy.Field()
    brand_name = scrapy.Field()
    model = scrapy.Field()
    body_type = scrapy.Field()
    prod_date = scrapy.Field()
    color = scrapy.Field()
    fuel_type = scrapy.Field()
    transmission = scrapy.Field()
    price = scrapy.Field()
    price_cur = scrapy.Field()
    brand_id = scrapy.Field()
    brand_name_html = scrapy.Field()
    model_id = scrapy.Field()
    model_name = scrapy.Field()
    modification = scrapy.Field()
    year = scrapy.Field()
    race = scrapy.Field()
    body_id = scrapy.Field()
    price_html = scrapy.Field()
    is_repaired = scrapy.Field()
    color_html = scrapy.Field()
    is_confiscated = scrapy.Field()
    is_damaged = scrapy.Field()
    fuel_html = scrapy.Field()
    is_customed = scrapy.Field()
    with_exchange = scrapy.Field()
    with_auction = scrapy.Field()
    engine_volume = scrapy.Field()
    is_abroad = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    tag_names = scrapy.Field()
    image_urls = scrapy.Field()
    absolute_url = scrapy.Field()
