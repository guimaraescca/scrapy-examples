import re
import scrapy
from news_crawler.items import NewsItem


class BrasilescolaSpider(scrapy.Spider):
    name = 'brasilescola'
    allowed_domains = ['brasilescola.uol.com.br']
    start_urls = ['http://brasilescola.uol.com.br/noticias/1']

    def parse(self, response):

        # For each publication date
        for news_date in response.xpath("//div[@class='data_noticia']"):

            # For each news published on that date
            for news in news_date.xpath("div[@class='data_noticia_item']"):

                # Obtain href reference to the news link
                news_link = news.xpath("div[@class='data_noticia_item_texto data_noticia_item_has_imagem']/div[@class='data_noticia_item_titulo data_noticia_item_has_imagem']/a/@href")

                # Extract news page link to be parsed
                news_link = news_link.extract_first()
                if news_link is not None:
                    yield response.follow(news_link, self.parse_news)

        # Proceed to the next page
        next_page_url = response.xpath("//div[@id='paginacao']/ul/li[8]/a/@href").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, self.parse)

    def parse_news(self, response):

        # Get news page main element
        news_div = response.xpath("//div[@class='conteudo-pagina']")

        # Parse page items content
        date_string = news_div.xpath("//span[@class='data']/text()").extract_first().strip()
        date = re.findall(r'(\d{2}/\d{2}/\d{4})', date_string)[0]

        title = news_div.xpath("//h1/text()").extract_first().strip()
        url = response.url
        text = ' '.join(string.strip() for string in news_div.xpath("//div[@class='conteudo-materia']//p//text()").getall())

        # Instantiate item with the parsed content
        news = NewsItem(date=date, title=title, url=url, text=text)

        yield news
