from logging_config import LoggingConfig

# Set up logging
logging_config = LoggingConfig()

from MediaOutlet import MediaOutlet
from MediaOutletConfigReader import MediaOutletConfigReader
from WebScraper import WebScraper
from flask import Flask, render_template
#from flask_bootstrap import Bootstrap5
# from flask_sqlalchemy import SQLAlchemy
# from Main import headlines
import logging


# IMPLEMENTING CONFIG READER CLASS
# Create an instance of MediaOutletConfigReader
# Call the read method to parse the file and get a list of media objects
# Print the names, URLs, and locations of the media items

filename = 'config.ini'
reader = MediaOutletConfigReader(filename)
media_list = reader.read()

# for media in media_list:
#     printMediaOutlet(media)


# IMPLEMENTING THE WEBSCRAPER CLASS
# Initialize WebScraper with media objects
scraper = WebScraper(media_list)
headlines = scraper.crawl_headlines()

for headline in headlines:
     print(f"Source: {headline.source}, \nHeadline: {headline.headline},"
           f"\nDate: {headline.date}, \nLink: {headline.url}\n")


# IMPLEMENTING FLASK
#app = Flask(__name__)
#bootstrap = Bootstrap5(app)


#@app.route('/')
#def index():
  #  return render_template('index.html', news_headlines=headlines)


#if __name__ == '__main__':
#    app.run(debug=True)
