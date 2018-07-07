from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joseph'}
    posts = [{
        'author':{'username':'liu'},
        'body': 'no1'
    },{
        'author':{'username':'dachuan'},
        'body': 'No2'
    }]
    return render_template('index.html', title='', user=user, posts=posts)
