# app.py
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/welcome")
def hai():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
