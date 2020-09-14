from newsapi import NewsApiClient
from app import app
from app.models import Article,Source

class Requests:
    News = NewsApiClient(api_key = app.config.get('API_KEY'))


    def get_top_headlines(self,sources=None):
        if Source is not None:
            response = self.News.get_top_headlines(country = 'us')
        else:
            response = self.News.get_top_headlines(sources=sources)
        articles = dict(articles = [])
        if response['articles'] :
            for article in response['articles']:
                articles['articles'].append(Article(**article).__dict__)
        
        return articles

