from flask import Flask

# import matplotlib_inline


app = Flask(__name__)


# -------------- Register Homepage Blueprints ---------------
from Python_files.homepage import homepage_blueprint, home_function
from fellowship_py_files.fellowship import fellowship_blueprint, fellowship_function
from adiswayam_py_files.adiswayam import adiswayam_blueprint, adiswayam_function

home_function(app)
fellowship_function(app)
adiswayam_function(app)

app.register_blueprint(homepage_blueprint)
app.register_blueprint(fellowship_blueprint)
app.register_blueprint(adiswayam_blueprint)
# -----------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)