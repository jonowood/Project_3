# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server recieved request for 'Home' page...") #prints to the console
    return "Welcome to my home page!" #returned to the client


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server recieved request for 'About' page...")
    return "Welcome to about page!"


if __name__ == "__main__": 
    app.run(debug=True) #runs the app on a local development server
    #makes dev. much easier, in production though best practices means debug must =False