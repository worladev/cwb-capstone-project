from flask import Flask

from WebScraper import WebScraper

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello CWB Members</h1>'


#if __name__ == '__main__':
#    app.run(debug=True)

#Daakyehen
from MediaOutlet import printMediaOutlet
from MediaOutletConfigReader import MediaOutletConfigReader

# Create an instance of MediaOutletConfigReader
# Call the read method to parse the file and get a list of media objects
# Print the names, URLs, and locations of the media items
def run_news_scraper():
    media_objects = MediaOutletConfigReader("confiq.ini")
    media_list = media_objects.read()

    # Initialize WebScraper with media objects
    scraper = WebScraper(media_list)

    headlines = scraper.crawl_headlines()
    for headline in headlines:
        print(f"Source: {headline.source}, \nHeadline: {headline.headline}, \nDate: {headline.date}, \nLink: {headline.url}\n")

if __name__ == "__main__":
    run_news_scraper()
