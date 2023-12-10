# class NewsFilter:
#     @staticmethod
#     def filter_headlines(headlines_dict, categories):
#         filtered_headlines = []
#
#         for category, headline in headlines_dict.items():
#             if headline.category.lower() in categories:
#                 filtered_headlines.append(headline)
#
#         return filtered_headlines


class NewsFilter:
    def __init__(self):
        self.category_headlines = list()

    def filter_category(self, headlines_dict, headline_category):
        for category, headline in headlines_dict.items():
            category = category.lower()
            if category in headline_category and category in self.category_headlines:
                self.category_headlines.append(headline)
            else:
                continue
        return self.category_headlines
