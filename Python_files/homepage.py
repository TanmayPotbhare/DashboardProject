from flask import Flask, render_template, send_file, Blueprint


homepage_blueprint = Blueprint('homepage', __name__)


def home_function(app):

    @homepage_blueprint.route('/')
    def homepage():
        return render_template('homepage/homepage.html')

    @homepage_blueprint.route('/aadiswayam')
    def aadiswayam():
        return render_template('homepage/aadiswayam.html')

