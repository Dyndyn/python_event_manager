from flask import render_template, Blueprint
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():
    events = current_user.events
    return render_template('home.html', events=events)
