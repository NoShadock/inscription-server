from flask import (
    Blueprint, render_template
)


bp = Blueprint('fun', __name__, url_prefix='/fun')


@bp.route('/')
def index():
    return render_template('fun/index.html')


@bp.route('/snake')
def snake():
    return render_template('fun/snake.html')

