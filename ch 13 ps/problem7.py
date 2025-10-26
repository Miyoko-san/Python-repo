# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run()
