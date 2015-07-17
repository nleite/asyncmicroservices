from flask import render_template, flash, redirect, g, url_for
from app import app
from app.forms import LoginForm, SearchForm
from app.models import FTSModel

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

@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect( url_for('index'))
    return redirect( url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
def search_results(query):
    fts = FTSModel()
    results = list(fts.search(query))
    title = 'The results for search "{0}"'.format(query)

    return render_template('list.html',
        title=title,
        list=results,
        query= '"{0}"'.format(query)
    )

@app.route('/recommended/')
@app.route('/recommended/<topic>')
def recommended(topic='all'):
    pass

@app.before_request
def before_request():
    g.search_form = SearchForm()
