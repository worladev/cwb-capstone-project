# import logging
# import requests
import os

from LoggingConfig import LoggingConfig
from MediaOutletConfigReader import MediaOutletConfigReader
from WebScraper import WebScraper
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from NewsFilter import NewsFilter

# from flask_sqlalchemy import SQLAlchemy
# from flask import Blueprint


# Set up logging
logging_config = LoggingConfig()

# IMPLEMENTING CONFIG READER CLASS
# Create an instance of MediaOutletConfigReader
# Call the read method to parse the file and get a list of media objects
# Print the names, URLs, and locations of the media items

filename = 'config.ini'
reader = MediaOutletConfigReader(filename)
media_list = reader.read()
#
#
# IMPLEMENTING THE WEBSCRAPER CLASS
# Initialize WebScraper with media objects
scraper = WebScraper(media_list)
headlines = scraper.crawl_headlines()


# def print_headlines(arg):
#     for headline in headlines:
#         print(f"Source: {headline.source}, \nHeadline: {headline.headline}, "
#               f"\nDate: {headline.date}, \nLink: {headline.url},\nCategory: {headline.category}\n")
#

# def print_headlines(headlines_dict):
#     for category, articles in headlines_dict.items():
#         print(f"Category: {category}")
#         for article in articles:
#             print(f"Source: {article.source}")
#             print(f"Headline: {article.headline}")
#             print(f"Date: {article.date}")
#             print(f"Link: {article.url}")
#             print(f"Category: {article.category}")
#             print()
#
#
# print_headlines(headlines)


filter1 = NewsFilter()


# IMPLEMENTING FLASK
app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Reading from config.ini file
    # filename = 'config.ini'
    # reader = MediaOutletConfigReader(filename)
    # media_list = reader.read()

    # IMPLEMENTING THE WEBSCRAPER CLASS
    # Initialize WebScraper with media objects
    # scraper = WebScraper(media_list)
    # headlines = scraper.crawl_headlines()

    # Paginating and rendering Flask object
    # page = request.args.get('page', 1, type=int)
    # per_page = 10
    # start_index = (page - 1) * per_page
    # end_index = start_index + per_page
    # page_items = headlines[start_index:end_index]
    # total_pages = len(headlines) // per_page + (len(headlines) // per_page > 0)

    return render_template('index.html',
                           # news_headlines=page_items,
                           news_headlines=headlines
                           # page=page,
                           # total_pages=total_pages,
                           )


@app.route('/category', methods=['GET', 'POST'])
def news_category():
    selected_categories = list()
    if request.method == 'POST':
        selected_categories = request.form.getlist('check')
        selected_categories = [category.lower() for category in selected_categories]

    filtered_headlines = filter1.filter_category(headlines, selected_categories)
    return render_template('category.html',
                           filtered_headlines=filtered_headlines,
                           )


if __name__ == '__main__':
    app.run(debug=True)
