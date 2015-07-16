from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    message = 'Hello World'
    title = 'Our future soccer application'
    return render_template('index.html', title=title, message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash_message = 'login requested from OpenId="%s", remember_me=%s' % (form.openid.data, form.remember_me.data)
        flash(flash_message)
        return redirect('/index')
    return render_template('login.html',
        title='Please login',
        form=form)
