from pathlib import Path

import scrapy


class MusicSpider(scrapy.Spider):
    name = "music"

    def start_requests(self):
        urls = [
            "https://www.melon.com/chart/",
            "https://www.melon.com/chart/hot100/",
            "https://www.melon.com/chart/day/",
            "https://www.melon.com/chart/week/",
            "https://www.melon.com/chart/month/",
        ]
        # 페이지 순회
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'site': url})

    def parse(self, response):
        music_rank_list = []
        site_name = response.meta.get('site', '').split('/')[-2]

        music_sels_50 = response.css('tbody > tr.lst50')
        music_sels_100 = response.css('tbody > tr.lst100')


        # 50위 곡 정보 저장
        for music_sel in music_sels_50:
            item = {}
            # item['site'] = site_name
            item['rank'] = music_sel.css('span.rank::text').get()
            item['title'] = music_sel.css('div.ellipsis.rank01 > span > a::text').get()
            item['artist'] = music_sel.css('div.ellipsis.rank02 > span > a::text').get()
            music_rank_list.append(item)
            yield item

        # 100위 곡 정보 저장
        for music_sel in music_sels_100:
            item = {}
            # item['site'] = site_name
            item['rank'] = music_sel.css('span.rank::text').get()
            item['title'] = music_sel.css('div.ellipsis.rank01 > span > a::text').get()
            item['artist'] = music_sel.css('div.ellipsis.rank02 > span > a::text').get()
            music_rank_list.append(item)
            yield item






