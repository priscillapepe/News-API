from newsapi import NewsApiClient
# from ..config import from news
class NewsRequests:
    API_KEY = '1c6caded5f054d598bf505ff7f0491a6'
    n = NewsApiClient(api_key=API_KEY)
    def get_top_headlines(self,**kwargs):
        return self.n.get_top_headlines(**kwargs)
    def get_everything(self,**kwargs):
        return self.n.get_everything(**kwargs)
    def get_sources(self,**kwargs):
        return self.n.get_sources(**kwargs)








# from newsapi import NewsApiClient
# from app import app
# from app.models import Article,Source

# class Requests:
#     News = NewsApiClient(api_key = app.config.get('API_KEY'))


#     def get_top_headlines(self,sources=None):
#         if Source is not None:
#             response = self.News.get_top_headlines()
#         else:
#             response = self.News.get_top_headlines(sources=sources)
#         articles = dict(articles = [])
#         if response['articles'] :
#             for article in response['articles']:
#                 articles['articles'].append(Article(**article).__dict__)
        
#         return articles

