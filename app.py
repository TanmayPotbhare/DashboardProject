from io import BytesIO
import pandas as pd
from flask import Flask, render_template, send_file, Blueprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as ply
# import matplotlib_inline
from classes.connections import ConnectParam


app = Flask(__name__)

conn_param = ConnectParam()


# -------------- Register Homepage Blueprints ---------------
from Python_files.homepage import homepage_blueprint, home_function
from Python_files.fellowship import fellowship_blueprint, fellowship_function

home_function(app)
fellowship_function(app)

app.register_blueprint(homepage_blueprint)
app.register_blueprint(fellowship_blueprint)
# -----------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)