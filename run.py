from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Kekambas'

@app.route('/definition')
def test():
    return 'Kamba or Kikamba is a Bantu language spoken by millions of people primariy in Kenya'

