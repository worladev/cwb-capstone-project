import logging
from bs4 import BeautifulSoup
from NewsArticle import NewsArticle
import requests

from dateutil import parser as date_parser
from dateutil.parser import ParserError
from datetime import datetime

import re
from StatusCode import StatusCode


# WebScraper class has self and media_list as its parameters.
# this function is to get the url of news platform from a list of media objects and scrap information
# an empty list is created to store the headlines obtained from the news platforms


class WebScraper:
    def __init__(self, media_list):
        self.media_list = media_list
        self.logger = logging.getLogger(__name__)

    def get_media(self):
        return self.media_list



    # def date_formats(self, date_format):
    #     date_formats = ["%d %B, %Y", "%d-%b-%Y", "%B %d, %Y", "%b-%d-%Y"]
    #     for date_format in date_formats:
    #         if format == date_format:
    #             return date_format
    #     return datetime.now().date()

    # Method to obtain headlines from news platforms based on various urls in a config file
    # It uses the request module to gain permission to scrap data from news platforms
    # It uses Beautiful soup to get all the headlines from the news outlet

    def crawl_headlines(self, num_of_headline_text=30):
        all_headlines = dict()
        self.logger.info("Scraping headlines from news platforms.")

        def get_category_from_text(text):
            text = text.lower()
            if 'entertainment' in text:
                return 'entertainment'
            elif 'sports' in text:
                return 'sports'
            elif 'business' in text:
                return 'business'
            else:
                return 'news'

        for media_object in self.media_list:
            try:
                response = requests.get(media_object.url)
                # regex
                # date_pattern = re.compile(
                #     r'(\d{2})[-/]?(\d{2})[-/]?(\d{4})|(\d{1,2})(?:st|nd|rd|th)? (\w+),? (\d{4})')

                date_pattern = re.compile(
                    r'(\d{2})[-/]?(\d{2})[-/]?(\d{4})|'
                    r'(\d{1,2})(?:st|nd|rd|th)? (\w+),? (\d{4})|'
                    r'(\d{1,2})(\w+), (\d{4})|'
                    r'(\d{2})-(\w{3})-(\d{4})|'
                    r'(\w+)(\d{1,2}), (\d{4})|'
                    r'(\w{3})-(\d{1,2})-(\d{4})'
                )

                # Check for successful response
                if response.status_code == 200:
                    logging.info(f"Successfully connected to {media_object.url}")
                    soup = BeautifulSoup(response.content, 'html.parser')
                    news_items = soup.find_all('a', href=True)

                    logging.info(f"Successfully obtained data from {media_object.url}")

                    for news_item in news_items:
                        logging.info(f"Obtaining headlines from {media_object.url}")
                        url = news_item['href']
                        headline_text = news_item.text.strip()

                        # date_items = soup.find_all('span', class_='date')
                        date_match = date_pattern.search(headline_text)  # date-code
                        # date_match = date_pattern.search(url)

                        if date_match:
                            # date = date_items.text.strip()
                            year = date_match.group(3) or date_match.group(6)
                            month = date_match.group(1) or date_match.group(4)
                            day = date_match.group(2) or date_match.group(5)

                            try:
                                date = date_parser.parse(f'{month}-{day}-{year}').date()
                            except ParserError:
                                date = "Invalid Format"
                        else:
                            # If no date match, use current date
                            date = datetime.now().date()
                            # date = "##### - Could not pick"

                        if url == "" or "video" in url or len(headline_text) < num_of_headline_text:
                            # log

                            logging.info(f"A media item that isn't a headline has been removed.")

                            continue
                        else:
                            category = get_category_from_text(headline_text)
                            article = NewsArticle(
                                source=media_object.name,
                                date=date,
                                headline=headline_text,
                                category=category,
                                url=url
                            )
                            logging.info(f"A media item successfully obtained.")

                            if category in all_headlines:
                                article_category = all_headlines[category]
                                article_category.add(article)
                                all_headlines[category] = article_category
                            else:
                                new_set = set()
                                new_set.add(article)
                                all_headlines[category] = new_set

                    logging.info(f"All media headlines successfully obtained from {media_object.name}.")

                else:
                    for code in StatusCode:
                        if response.status_code == int(code.value):
                            logging.warning(
                              f"Failed to fetch data from {media_object.url}. "
                              f"Status code after attempting to connect to {media_object.name}: {code.name}")
            except requests.RequestException as exception_error:
                logging.error(f"Error connecting to {media_object.url}: {exception_error}")



        return all_headlines
        # a method that takes an integer. could use enums
        # returns meaning of status code received

