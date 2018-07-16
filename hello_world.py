from flask import Flask

app = Flask(__name__)


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
def exit():
    return "Thanks for looking around. Come back again soon!"

# app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
