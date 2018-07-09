from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Username:{}, remember_me:{}'.format(
            form.username.data, 
            form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
