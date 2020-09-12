from flask import render_template
from app import app

# Views
@app.route('/news/<news_title>')
def index():

    '''
    View news page function that returns the news details page and its data
    '''
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)