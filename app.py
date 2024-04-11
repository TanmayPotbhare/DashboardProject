from io import BytesIO
import pandas as pd
from flask import Flask, render_template, send_file, Blueprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as ply
# import matplotlib_inline

app = Flask(__name__)


# -------------- Register Homepage Blueprints ---------------
from homepage_Python_files.homepage import homepage_blueprint, home_function
home_function(app)
app.register_blueprint(homepage_blueprint)
# -----------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)