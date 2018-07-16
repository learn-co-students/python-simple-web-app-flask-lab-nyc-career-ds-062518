from flask import Flask

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
def profile():
    return "This is my profile! It's not finished yet... :/"

@app.route('/exit')
def exit():
    return "Thanks for looking around. Come back again soon!"

if __name__ == '__main__':
    app.run(debug=True)
