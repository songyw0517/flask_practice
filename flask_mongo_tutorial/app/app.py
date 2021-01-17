from flask import Flask, request, render_template, url_for
from view import index, login
from DB import db


app = Flask(__name__)
app.register_blueprint(index.BP)
app.register_blueprint(login.BP)

if __name__== '__main__':
    app.run(debug=True)