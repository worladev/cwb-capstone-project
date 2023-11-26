import logging
import sys

from NewsArticle import NewsArticle
from bs4 import BeautifulSoup
import requests
from datetime import datetime

logging.basicConfig(
    # filename='web_scrapers.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('web_scrapers.log'), logging.StreamHandler(sys.stdout)]
)

# WebScraper class has self and media_list as its parameters.
# this function is to get the url of news platform from a list of media objects and scrap information
# an empty list is created to store the headlines obtained from the news platforms


class WebScraper:
    def __init__(self, media_list):
        self.media_list = media_list

    def get_media(self):
        return self.media_list

    # Method to obtain headlines from news platforms based on various urls in a config file
    # It uses the request module to gain permission to scrap data from news platforms
    # It uses Beautiful soup to get all the headlines from the news outlet
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime

    def crawl_headlines(self):
        all_headlines = []

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

                        if url == "" or "video" in url or len(headline_text) < 25:
                            continue
                        else:
                            current_date = datetime.now().strftime("%Y-%m-%d")

                            article = NewsArticle(
                                source=media_object.name,
                                date=current_date,
                                headline=headline_text,
                                category="some_category",
                                url=url
                            )
                            all_headlines.append(article)
                else:
                    logging.warning(
                        f"Failed to fetch data from {media_object.url}. Status code: {response.status_code}")
            except requests.RequestException as exception_error:
                logging.error(f"Error connecting to {media_object.url}: {exception_error}")

        return all_headlines
