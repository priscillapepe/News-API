from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View news page function that returns the news details page and its data
    '''
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)

@app.route('/movie/<movie_id>')
def news(news_title):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_title}'
    return render_template('news.html',title = title)