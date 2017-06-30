from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'David'}
	
	comments = [
		{
			'text': 'Please select one of the charts above.'
		}
	]
	return render_template('index.html',
				title='Home',
				user=user,
				comments=comments)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	
	return render_template('login.html',
				title='Sign In',
				form=form)
				

@app.route('/chart1')
def chart1():
	return render_template('chart1.html', title='Chart 1')
	
	
@app.route('/chart2')
def chart2():
	return render_template('chart2.html', title='Chart 2')
	
	
@app.route('/chart3')
def chart3():
	return render_template('chart3.html', title='Chart 3')
	
	
@app.route('/chart4')
def chart4():
	return render_template('chart4.html', title='Chart 4')
	
	
@app.route('/chart5')
def chart5():
	return render_template('chart5.html', title='Chart 5')

