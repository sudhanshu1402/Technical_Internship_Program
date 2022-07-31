from marketair.MarketairItem import MarketairItem
import scrapy


class MarketairspiderSpider(scrapy.Spider):
    name = 'marketairspider'
    start_urls = [
                   'https://www.marketair.com/shop/acustiflex.html', 'https://www.marketair.com/shop/deflectair.html',
                  'https://www.marketair.com/shop/drainhide.html', 'https://www.marketair.com/shop/drainmate.html',
                  'https://www.marketair.com/shop/dripshield.html', 'https://www.marketair.com/shop/dss-switch.html',
                  'https://www.marketair.com/shop/easybend.html', 'https://www.marketair.com/shop/lineport.html',
                  'https://www.marketair.com/shop/perfect-pitch.html', 'https://www.marketair.com/shop/pipe-prop-pipe-support.html',
                  'https://www.marketair.com/shop/reversaline.html', 'https://www.marketair.com/shop/roughinbox.html',
                  'https://www.marketair.com/shop/snapfix.html', 'https://www.marketair.com/shop/snowshield.html',
                  'https://www.marketair.com/shop/supersleeve.html', 'https://www.marketair.com/shop/valveshield.html'
                  ]

    def parse(self, response, **kwargs):
        for href in response.css("div.vm-product-media-container a::attr(href)").extract():
            view_url = "https://www.marketair.com" + str(href)
            url = view_url
            yield scrapy.Request(url, callback=self.parse_items, errback=self.parse_items, dont_filter=True)

    def parse_items(self, response):

        items = MarketairItem()

        ####################
        ####################

        try:
            title = response.xpath('//*[@id="sidecontent"]/div[2]/h1/text()').extract_first()
        except Exception as e:
            title = ''
            print('Exception while getting product title --> ', e)
            pass
        print('title --> ', title)
        items['title'] = title

        ####################
        ####################

        try:
            price = response.css('span.PricebasePrice::text').extract_first().replace('$', '')
        except Exception as e:
            price = ''
            print('Exception while getting product price --> ', e)
            pass
        print('price --> ', price)
        items['price'] = price

        ####################
        ####################

        try:
            url = response.request.url
        except Exception as e:
            url = ''
            print('Exception while getting product url --> ', e)
            pass
        print('url --> ', url)
        items['url'] = url

        ####################
        ####################

        try:
            desc = response.css('div.product-description').extract_first()
        except Exception as e:
            desc = ''
            print('Exception while getting product desc --> ', e)
            pass
        print('desc --> ', desc)
        items['desc'] = str(desc).replace('\\r', '').replace('\\n', '').replace('\\t', '').replace('[', '').replace(']', '').replace("'", "")

        ####################
        ####################

        try:
            images = {}
            main_image = response.css('div.main-image a::attr(href)').extract()
            extra_image = response.css('div.additional-images a::attr(href)').extract()
            product_imgurls = main_image + extra_image
            for img_urls in range(len(product_imgurls)):
                images.update({"image_url_" + str(img_urls + 1): product_imgurls[img_urls]})
        except Exception as e:
            images = ''
            print('Exception while getting product images --> ', e)
            pass
        print('images --> ', images)
        items['images'] = images

        ####################
        ####################

        yield items