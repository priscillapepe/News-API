from newsapi import NewsApiClient
from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key = "be4e93f873ac485f96369b58d4413c7d")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')  
    # return topheadlines

    return render_template('index.html', data = topheadlines['articles'])       


@app.route('/fox')
def fox():
    newsapi = NewsApiClient(api_key = "be4e93f873ac485f96369b58d4413c7d")
    topheadlines = newsapi.get_top_headlines(sources='fox-news')  
    # return topheadlines

    return render_template('fox.html', data = topheadlines['articles']) 
    
@app.route('/abc')
def abc():
    newsapi = NewsApiClient(api_key = "be4e93f873ac485f96369b58d4413c7d")
    topheadlines = newsapi.get_top_headlines(sources='abc-news')  
    # return topheadlines

    return render_template('abc.html', data = topheadlines['articles']) 


if __name__ == "__main__":
    app.run(debug=True)
    
