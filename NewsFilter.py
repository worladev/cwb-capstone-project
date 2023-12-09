class NewsFilter:
    @staticmethod
    def filter_headlines(headlines, categories):
        filtered_headlines = []

        for headline in headlines:
            if headline.category.lower() in categories:
                filtered_headlines.append(headline)

        return filtered_headlines
