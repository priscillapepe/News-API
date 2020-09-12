from flask import render_template
from app import app

# Views
@app.route('/news/<news_id>')
def movie(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)
