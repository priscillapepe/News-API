from flask import render_template
from app import app

# Views
@app.route('/news/<news_title>')
def news(news_title):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',title = news_title)
