from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    print(request.args)
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    print(request.args)
    return "welcome home"


@app.route('/welcome/back')
def welcome_back():
    print(request.args)
    return "welcome back"