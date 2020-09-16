# from app import app
from . import main
from flask import render_template
from ..requests import NewsRequests
# from run import app
# from app import create_app

# app = create_app('development')
request = NewsRequests()

@main.route('/')
def index():
    topheadlines = request.get_top_headlines(sources='bbc-news')
    # return topheadlines

    return render_template('index.html', data = topheadlines['articles'])       


@main.route('/fox')
def fox():
    topheadlines = request.get_top_headlines(sources='fox-news')  
    # return topheadlines

    return render_template('fox.html', data = topheadlines['articles']) 
    
@main.route('/abc')
def abc():
    topheadlines = request.get_top_headlines(sources='abc-news')  
    print(topheadlines)
    # return topheadlines
    # return topheadlines

    return render_template('abc.html', data = topheadlines['articles']) 
