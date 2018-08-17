from flask import Flask, render_template, flash, request, url_for, redirect, session
import gc

app = Flask(__name__)
app.secret_key = 'bestintheworld'

@app.route('/')
def homepage():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == '__main__':
	app.run(debug = True)
