from pathlib import Path

import scrapy


class MusicSpider(scrapy.Spider):
    name = "music"

    def start_requests(self):
        urls = [
            "https://www.melon.com/chart/",
        ]
        # 페이지 순회
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        music_sels_50 = response.css('tbody > tr.lst50')
        music_sels_100 = response.css('tbody > tr.lst100')
        item = {}
        for music_sel in music_sels_50:
            item['title'] = music_sel.css('div.ellipsis.rank01 > span > a::text').get()
            # print('title : ', title)
        for music_sel in music_sels_100:
            item['title'] = music_sel.css('div.ellipsis.rank01 > span > a::text').get()
            # print('title : ', title)
            yield item