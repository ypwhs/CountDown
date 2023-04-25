from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='.', static_folder='dist')


@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=12345, debug=True)
