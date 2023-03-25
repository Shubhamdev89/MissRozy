#Thank you Shubhamdev64 for helping me in this journey !
#Must Subscribe On YouTube @hackerbhai1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@Shubhamdev64'

if __name__ == "__main__":
    app.run()
