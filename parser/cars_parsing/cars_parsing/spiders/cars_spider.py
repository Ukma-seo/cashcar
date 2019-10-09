import scrapy
import json

from operator import itemgetter
from collections import defaultdict
from flatten_dict import flatten
import re

import cars_parsing.item_selectors as item_selectors
from cars_parsing.items import CarItem


class CarsSpider(scrapy.Spider):

    name = "cars"

    start_urls = [
        'https://auto.ria.com/car/used/?page=2164',
    ]

    def extract_image_urls(self, response):

        image_urls = response.xpath(item_selectors.CARS_IMAGE_PATTERN).extract()
        filtered_images = filter(lambda url: 'support' not in url, image_urls)
        extension_replacer = lambda x: re.sub('(\w)?.jpg', 'fx.jpg', x)
        return list(map(extension_replacer, filtered_images))

    def parse_json_state(self, response):

        cars_metadata = json.loads(response.xpath("//script")
                                 .re(item_selectors.CARS_JSON_PATTERN)[0])

        cars_metadata = defaultdict(lambda: None, flatten(cars_metadata, reducer='path'))

        attribute_getter = itemgetter(*item_selectors.ATTRIBUTES_FROM_JSON_METADATA)
        attributes_extracted = attribute_getter(cars_metadata)

        return attributes_extracted

    def parse_html_metadata(self, response):

        cars_metadata = response.xpath("//script").re(item_selectors.CARS_METADATA_PATTERN)[0]
        cars_metadata = defaultdict(lambda :None, re.findall(item_selectors.CARS_METADATA_SPLIT_PATTERN, cars_metadata))
        attribute_getter = itemgetter (*item_selectors.ATTRIBUTES_FROM_HTML_METADATA)
        attributes_extracted = attribute_getter(cars_metadata)
        # print(attributes_extracted)
        # print(len(attributes_extracted))
        return attributes_extracted


    def parse_page(self, response):

        preprocess_item = lambda string: '' if not string else string.strip ()
        preprocess_items = lambda iterable: '' if not iterable else list(map(preprocess_item, iterable))

        search_patterns = [item_selectors.CAR_DESCRIPTION_PATTERN,
                           item_selectors.CARS_MODEL_RATING_VALUE,
                           ]

        parsed_values = [preprocess_item(response.xpath(pattern).get())
                         for pattern in search_patterns]

        parsed_tags = preprocess_items(response.xpath(item_selectors.CARS_TAGS_VALUES_PATTERN).extract())
        parsed_tag_names = preprocess_items(response.xpath(item_selectors.CARS_TAGS_NAMES_PATTERN).extract())

        parsed_values.extend([parsed_tags, parsed_tag_names])

        return parsed_values


    def parse(self, response):

        # finding all apartments on a page
        for href in response.xpath(item_selectors.CAR_PAGE_PATTERN):
            yield response.follow(href, self.parse_car)

        # next_page_link = response.xpath(item_selectors.NEXT_PAGE_PATTERN)[0]
        page_link_namespace, page_link_number = str(response.url).split('=')
        page_link_number = int(page_link_number)+1
        next_page_link = str(page_link_namespace)+'='+str(page_link_number)

        print(f"Next page link {next_page_link}")
        yield response.follow(next_page_link, self.parse)

    def parse_car(self, response):

        name, mileage_value, mileage_unitcode, brand_name, \
            model, body_type, prod_date, color, fuel_type, \
            transmission, price, price_cur = self.parse_json_state(response)

        image_urls = self.extract_image_urls(response)

        brand_id, brand_name_html, model_id, model_name, modification, year, race,\
        body_id, price_html, is_repaired, is_confiscated, is_damaged, fuel_html, color_html, is_customed,\
        with_exchange, with_auction, engine_volume, is_abroad, car_id = self.parse_html_metadata(response)

        description, rating, tags, tag_names = self.parse_page(response)

        apartment_item = CarItem(
                                id=car_id,
                                name = name,
                                mileage_value = mileage_value,
                                mileage_unitcode = mileage_unitcode,
                                brand_name = brand_name,
                                model = model,
                                body_type = body_type,
                                prod_date = prod_date,
                                color = color,
                                fuel_type = fuel_type,
                                transmission = transmission,
                                price = price,
                                price_cur = price_cur,
                                brand_id = brand_id,
                                brand_name_html = brand_name_html,
                                model_id = model_id,
                                model_name = model_name,
                                modification = modification,
                                year = year,
                                race = race,
                                body_id = body_id,
                                price_html = price_html,
                                is_repaired = is_repaired,
                                is_confiscated = is_confiscated,
                                is_damaged = is_damaged,
                                fuel_html = fuel_html,
                                color_html = color_html,
                                is_customed = is_customed,
                                with_exchange = with_exchange,
                                with_auction = with_auction,
                                engine_volume = engine_volume,
                                is_abroad = is_abroad,
                                description = description,
                                tags = tags,
                                tag_names = tag_names,
                                image_urls = image_urls,
                                absolute_url = response.url)

        yield apartment_item

