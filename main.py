
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World From Algo!"


app.run(port=5001)