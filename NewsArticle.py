from MediaOutletConfigReader import MediaOutletConfigReader
from WebScraper import WebScraper


class NewsArticle:
    def __init__(self, source, date, headline, category, url):
        self.source = source
        self.date = date
        self.headline = headline
        self.category = category
        self.url = url




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
