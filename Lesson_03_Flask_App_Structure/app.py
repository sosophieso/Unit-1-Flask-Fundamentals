from flask import Flask
app = Flask(__name__)

@app.route('/') # / front door (homepage)
def home(): # function name (can be anything)
    return "Homepage!" # what users see

@app.route('/about')
def about():
    # return "About Page!"
    return """<h1> Welcome - About Me <h1>
              <p> This is my first website </p>
"""

@app.route('/contact')
def contact():
    return "Contact Page!"

app.run(debug = True)