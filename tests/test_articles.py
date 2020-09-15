import unittest
import sys
sys.path.append(".")
from app.models import Article
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # self,,,,,source,,,urlToImage
        self.new_news = Article(
            url='https://image.tmdb.org/t/p/w500/khsjha27hbs',
            author='Kingkrusha',
            content='Python Must Be Crazy',
            description='A thrilling new Python Series',
            publishedAt=129993,
            source='fox',
            title='Python Must Be Crazy',
            urlToImage='https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,Article))

    def test_author(self):
        author_var = self.new_news.author
        self.assertTrue(author_var == "Kingkrusha")

    def test_content(self):
        content_var = self.new_news.content
        self.assertTrue(content_var == "Python Must Be Crazy")

    def test_description(self):
        description_var = self.new_news.description
        self.assertTrue(description_var == "A thrilling new Python Series")

    def test_publishedAt(self):
        publishedAt_int = self.new_news.publishedAt
        self.assertTrue(publishedAt_int == 129993)

    def test_url(self):
        url_var = self.new_news.url
        self.assertTrue(url_var == "https://image.tmdb.org/t/p/w500/khsjha27hbs")

    def test_title(self):
        title_var = self.new_news.title
        self.assertTrue(title_var == "Python Must Be Crazy")

    def test_source(self):
        source_var = self.new_news.source
        self.assertTrue(source_var == "fox")

    def test_urlToImage(self):
        urlToImage_var = self.new_news.urlToImage
        self.assertTrue(urlToImage_var == "https://image.tmdb.org/t/p/w500/khsjha27hbs")


if __name__ == '__main__':
    unittest.main()