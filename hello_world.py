# import flask here
from flask import Flask

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app

# tell your flask app to run with debug mode on

@app.route('/')
def index():
    return "Hello, world!"


@app.route('/home')
def home():
    return "Welcome to an amazing Flask App!"

@app.route('/myprofile')
def myprofile():
    return "This is my profile! It's not finished yet... :/"

@app.route('/exit')
def ecit():
    return "Thanks for looking around. Come back again soon!"

if __name__ == '__main__':
    app.run(debug = True)
