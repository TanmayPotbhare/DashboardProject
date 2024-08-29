from flask import Flask, render_template, flash
import logging

# import matplotlib_inline


app = Flask(__name__)
app.secret_key = '123456Dashboard'  # Replace with a strong, unique key

app.config['LOG_LEVEL'] = logging.DEBUG


# -------------- Register Homepage Blueprints ---------------
from Python_files.homepage import homepage_blueprint, home_function
from fellowship_py_files.fellowship import fellowship_blueprint, fellowship_function
from adiswayam_py_files.adiswayam import adiswayam_blueprint, adiswayam_function
from masterDashboard_py_files.masterDash import master_blueprint, master_function

home_function(app)
fellowship_function(app)
adiswayam_function(app)
master_function(app)

app.register_blueprint(homepage_blueprint)
app.register_blueprint(fellowship_blueprint)
app.register_blueprint(adiswayam_blueprint)
app.register_blueprint(master_blueprint)
# -----------------------------------------------------------


@app.route('/logout')
def logout():
    flash('Logged Out Successfully', 'success')
    return render_template('homepage/login.html')


if __name__ == '__main__':
    app.run(debug=True)