from flask import Blueprint, render_template
from app.login import login_required
bp = Blueprint('library', __name__, url_prefix='/library', template_folder='../templates', static_folder='../static')

"""
render library
"""
@bp.route('/')
@login_required
def index():
    return render_template('library.html')