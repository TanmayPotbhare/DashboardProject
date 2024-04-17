from flask import Flask, render_template, send_file, Blueprint
from adiswayam_py_files.adiswayam_definition import *


adiswayam_blueprint = Blueprint('adiswayam', __name__)


def adiswayam_function(app):
    @adiswayam_blueprint.route('/aadiswayam', methods=['GET', 'POST'])
    def adiswayam():
        total_count = test()
        return render_template('homepage/aadiswayam.html', total_count=total_count)