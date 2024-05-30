from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/list-page')
def list_page():
    return render_template('list-page.html')