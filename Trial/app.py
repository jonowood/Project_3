# Import dependencies 
from flask import Flask, render_template, url_for
# Create an app

app = Flask(__name__)

#  Define static routes

# index

@app.route("/")
def index():
    print("Server received request for 'index' page...")
    return render_template('index2.html')

#  construction


@app.route("/construction")
def construction():
    print("Server received request for 'construction' page...")
    return render_template('construction.html')

# engineering


@app.route("/engineering")
def engineering():
    print("Server received request for 'engineering' page...")
    return render_template('engineering.html')

# healthcare


@app.route("/healthcare")
def healthcare():
    print("Server received request for 'healthcare' page...")
    return render_template('healthcare.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
    