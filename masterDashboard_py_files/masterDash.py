from flask import Flask, render_template, send_file, Blueprint
from fellowship_py_files.fellowship_definitions import *


master_blueprint = Blueprint('master', __name__)


def master_function(app):

    @master_blueprint.route('/master_dashboard', methods=['GET', 'POST'])
    def master_dashboard():
        return render_template('masterDash/master_dashboard.html')

    @master_blueprint.route('/suggestions', methods=['GET', 'POST'])
    def suggestions():
        return render_template('masterDash/suggestions.html')