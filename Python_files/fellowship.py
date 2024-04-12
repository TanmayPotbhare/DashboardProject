from flask import Flask, render_template, send_file, Blueprint
from classes.connections import ConnectParam

fellowship_blueprint = Blueprint('fellowship', __name__)


def fellowship_function(app):
    def applications_today():
        # Create an instance of ConnectParam with the host parameter
        connect_param = ConnectParam(FellowshipHost.hostserver, 'root', 'A9CALcsd7lc%7ac', 'ICSApplication')
        cursor = connect_param.connect()
        cursor.execute("SELECT COUNT(*) FROM application_page")
        result = cursor.fetchone()
        print(result)
        return result[0]

    @fellowship_blueprint.route('/fellowship', methods=['GET', 'POST'])
    def fellowship():
        total_count = applications_today()
        return render_template('homepage/fellowship.html', total_count=total_count)