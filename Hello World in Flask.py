# -*- coding: utf-8 -*-
"""Created by Paul A. Gureghian in Jan 2019."""

"""Hello World in Flask."""

from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True) 
 