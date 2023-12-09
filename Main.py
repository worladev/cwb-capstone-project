# import logging
# import requests
import os
import math

from LoggingConfig import LoggingConfig
from MediaOutletConfigReader import MediaOutletConfigReader
from WebScraper import WebScraper
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

# from flask import Blueprint


# Set up logging
logging_config = LoggingConfig()


# IMPLEMENTING FLASK
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Reading from config.ini file
# Create an instance of MediaOutletConfigReader
filename = 'config.ini'
reader = MediaOutletConfigReader(filename)
media_list = reader.read()

# IMPLEMENTING THE WEBSCRAPER CLASS
# Initialize WebScraper with media objects
scraper = WebScraper(media_list)
headlines = scraper.crawl_headlines()


def print_headlines(arg):
    for category, headline in headlines.items():
        for item in headline:
            print(category, item.source)
        # print(f"Source: {headline.source}, \nHeadline: {headline.headline}, "
        #       f"\nDate: {headline.date}, \nLink: {headline.url},\nCategory: {headline.category}\n")


print_headlines(headlines)


# def paginate_items(page, per_page):
#     start_index = (page - 1) * per_page
#     end_index = start_index + per_page
#     return set(list(headlines)[start_index:end_index])
#
#
# def get_total_pages(items, per_page):
#     total_items = len(items)
#     return int(math.ceil(total_items / per_page))
#
#
# @app.route('/')
# def index():
#     # Paginating and rendering Flask object
#     per_page = 10
#     page = request.args.get('page', default=1, type=int)
#     news_items = paginate_items(page, per_page)
#
#     total_pages = get_total_pages(headlines, per_page)
#
#     return render_template('index.html',
#                            news_headlines=news_items,
#                            # news_headlines=headlines,
#                            page=page,
#                            total_pages=total_pages,
#                            )
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
