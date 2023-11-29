import logging
from LoggingConfig import LoggingConfig
from MediaOutletConfigReader import MediaOutletConfigReader
from WebScraper import WebScraper
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
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


# # IMPLEMENTING THE WEBSCRAPER CLASS
# # Initialize WebScraper with media objects
scraper = WebScraper(media_list)
headlines = scraper.crawl_headlines()


# def print_headlines(arg):
#     for headline in headlines:
#         print(f"Source: {headline.source}, \nHeadline: {headline.headline}, "
#               f"\nDate: {headline.date}, \nLink: {headline.url}\n")
#
#
# print_headlines(headlines)


# IMPLEMENTING FLASK
app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def index(page=1):
    # per_page = 10
    # posts = headlines.query.order_by(headlines.time.desc()).paginate(page, per_page, error_out=False)
    return render_template('index.html',
                           news_headlines=headlines,
                           )


if __name__ == '__main__':
    app.run(debug=True)
