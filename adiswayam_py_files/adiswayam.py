from flask import Flask, render_template, send_file, Blueprint
from adiswayam_py_files.adiswayam_definition import *


adiswayam_blueprint = Blueprint('adiswayam', __name__)


def adiswayam_function(app):
    @adiswayam_blueprint.route('/aadiswayam', methods=['GET', 'POST'])
    def aadiswayam():
        total_count = total_candidates()
        total_train_center = total_training_center()
        total_train_partner = total_training_partner()
        placed_data = placement_count()
        return render_template('masterDash/projects/aadiswayam.html', total_count=total_count, total_train_center=total_train_center,
                               total_train_partner=total_train_partner, placed_data=placed_data)
