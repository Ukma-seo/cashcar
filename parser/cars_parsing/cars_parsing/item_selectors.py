CAR_PAGE_PATTERN = "//a[@class='m-link-ticket']//@href"
NEXT_PAGE_PATTERN = "//span[@class='page-item next text-r']/a/@href"

CARS_TAGS_VALUES_PATTERN = "//dd[contains(@class,'show-line')]/span[contains(@class,'argument')]/text()"
CARS_TAGS_NAMES_PATTERN = "//dd[contains(@class,'show-line')]/span[contains(@class,'label')]/text()"
CAR_DESCRIPTION_PATTERN = "//div[contains(@id,'full-description')]/text()"
CARS_IMAGE_PATTERN = '//div[@id="photosBlock"]//div[contains(@class,"photo-")]//img/@src'


CARS_JSON_PATTERN = 'application/ld.*>({.+})'
CARS_METADATA_PATTERN = 'defer src.*data.*">'
CARS_METADATA_SPLIT_PATTERN = '([^\s]+)=([^\s]+)'
CARS_MODEL_RATING_VALUE = '//span[@itemprop="ratingValue "]/text()'


ATTRIBUTES_FROM_JSON_METADATA = ('name',
                               'mileageFromOdometer/value',
                               'mileageFromOdometer/unitCode',
                               'brand/name',
                               'model',
                               'bodyType',
                               'productionDate',
                               'color',
                               'fuelType',
                               'vehicleTransmission',
                               'offers/price',
                               'offers/priceCurrency')

ATTRIBUTES_FROM_HTML_METADATA = ('data-marka-id',
                                 'data-mark-name',
                                 'data-model-id',
                                 'data-model-name',
                                 'data-modification',
                                 'data-year',
                                 'data-race',
                                 'data-body-id',
                                 'data-price',
                                 'data-repair',
                                 'data-confiscated',
                                 'data-damaged',
                                 'data-fuel',
                                 'data-color-id',
                                 'data-is-customed',
                                 'data-with-exchange',
                                 'data-with-auction',
                                 'data-engine-volume',
                                 'data-abroad',
                                 'data-advertisement-id'
                                 )


