# from MediaOutletConfigReader import MediaOutletConfigReader
# from WebScraper import WebScraper


# This Class defines a NewsArticle with the following attributes:
# source : the name of the media
# date: the date news article was posted
# headline: the headline of the news article
# category: the type of news article
# url: the link to the full news article
class NewsArticle:
    def __init__(self, source, date, headline, category, url):
        self.source = source
        self.date = date
        self.headline = headline
        self.category = category
        self.url = url


# This creates a method to print the headline of news articles.
# This function prints out the source, headline, date and url of the NewsArticle
