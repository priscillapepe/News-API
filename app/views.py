from flask import render_template
from app import app

# Views
@app.route('/news/<news_title>')
def movie(news_title):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',title = news_title)
