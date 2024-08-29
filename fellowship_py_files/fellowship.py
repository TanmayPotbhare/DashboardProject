from flask import Flask, render_template, send_file, Blueprint
from fellowship_py_files.fellowship_definitions import *


fellowship_blueprint = Blueprint('fellowship', __name__)


def fellowship_function(app):
    @fellowship_blueprint.route('/fellowship', methods=['GET', 'POST'])
    def fellowship():
        total_count = applications_today()
        visitor_counts = visitor_count()
        current_count = current_year_count()
        accepted_count = accepted_year_count()
        return render_template('masterDash/projects/fellowship.html', total_count=total_count, visitor_counts=visitor_counts,
                               current_count=current_count, accepted_count=accepted_count)