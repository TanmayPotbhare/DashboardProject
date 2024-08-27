from flask import Flask, render_template, send_file, Blueprint, request, redirect, url_for, flash
from classes.connections import *

homepage_blueprint = Blueprint('homepage', __name__)


def home_function(app):

    @homepage_blueprint.route('/')
    def homepage():
        return render_template('homepage/homepage.html')

    @homepage_blueprint.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('homepage/login.html')

    @homepage_blueprint.route('/submit_login', methods=['GET', 'POST'])
    def submit_login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            print(email)
            print(password)
            host = FellowshipHost().hostserver
            query = "SELECT * FROM dashboard_login"

            with DatabaseConnection(host, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication') as conn:
                result = conn.execute_query(query)
                print(result)
                username = result[0]['email']
                password = result[0]['password']

                if email != username:
                    flash('Username is Invalid. Please enter Valid Username', 'error')
                    return redirect(url_for('homepage.login'))

                if password != password:
                    flash('Password is Invalid. Please enter Valid Password', 'error')
                    return redirect(url_for('homepage.login'))

                if email == username and password == password:
                    flash('Logged in Successfully.', 'success')
                    return redirect(url_for('fellowship.fellowship'))

        flash('Invalid Username and Password', 'error')
        return render_template('homepage/login.html')