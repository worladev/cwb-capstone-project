import logging
from bs4 import BeautifulSoup
from NewsArticle import NewsArticle
import requests
from datetime import datetime
import re

class WebScraper:
    def __init__(self, media_list):
        self.media_list = media_list
        self.logger = logging.getLogger(__name__)

    def get_media(self):
        return self.media_list



    def crawl_headlines(self, num_of_headline_text=30):
        all_headlines = []
        self.logger.info("Scraping headlines from news platforms.")

        for media_object in self.media_list:
            try:
                response = requests.get(media_object.url)
                # Check for successful response
                if response.status_code == 200:
                    logging.info(f"Successfully connected to {media_object.url}")
                    soup = BeautifulSoup(response.content, 'html.parser')
                    news_items = soup.find_all('a', href=True)

                    for news_item in news_items:
                        url = news_item['href']
                        headline_text = news_item.text.strip()

                        if url == "" or "video" in url or len(headline_text) < num_of_headline_text:
                            continue

                        try:
                            # Extract date using the new method
                            parsed_date = self.extract_date_from_headline(headline_text)

                            article = NewsArticle(
                                source=media_object.name,
                                date=parsed_date.strftime("%Y-%m-%d"),
                                headline=headline_text,
                                category="some_category",
                                url=url
                            )
                            all_headlines.append(article)
                        except Exception as e:
                            self.logger.error(f"Error processing headline: {headline_text}. Error: {e}")

                else:
                    logging.warning(
                        f"Failed to fetch data from {media_object.url}. Status code: {response.status_code}")
            except requests.RequestException as exception_error:
                logging.error(f"Error connecting to {media_object.url}: {exception_error}")

        return all_headlines
