from bs4 import BeautifulSoup
import requests
from datetime import datetime


class WebScraper:
    def __init__(self, media_list):
        self.media_list = media_list

    def get_media(self):
        return self.media_list

    def crawl_headlines(self):
        from NewsArticle import NewsArticle  # Importing here to avoid circular dependency

        all_headlines = []

        for media_object in self.media_list:
            response = requests.get(media_object.url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all 'a' tags with corresponding headlines and links
            news_items = soup.find_all('a', href=True)

            for news_item in news_items:
                url = news_item['href']
                headline_text = news_item.text.strip()

                if url == "" or "video" in url or len(headline_text) < 25:
                    continue
                else:
                    # Assuming today's date for each article scraped ??
                    current_date = datetime.now().strftime("%Y-%m-%d")

                    article = NewsArticle(
                        source=media_object.name,
                        date=current_date,
                        headline=headline_text,
                        category="some_category",
                        url=url
                    )
                    all_headlines.append(article)

        return all_headlines
