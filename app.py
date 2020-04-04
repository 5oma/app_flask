from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	user = {'username': 'Ariel'}
	return render_template('index.html', title='Home', user=user)