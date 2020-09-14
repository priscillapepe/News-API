from app import app
from flask import render_template
from app.requests import Requests

request = Requests()

@app.route('/')
def index():
    topheadlines = request.get_top_headlines(sources='bbc-news')
    # return topheadlines

    return render_template('index.html', data = topheadlines['articles'])       


@app.route('/fox')
def fox():
    topheadlines = request.get_top_headlines(sources='fox-news')  
    # return topheadlines

    return render_template('fox.html', data = topheadlines['articles']) 
    
@app.route('/abc')
def abc():
    topheadlines = request.get_top_headlines(sources='abc-news')  
    # return topheadlines
    # return topheadlines

    return render_template('abc.html', data = topheadlines['articles']) 
