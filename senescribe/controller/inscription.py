from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from senescribe.controller.auth import login_required
from senescribe.db import get_db
from senescribe import model
from senescribe.validators import Text, Birthdate


bp = Blueprint('inscription', __name__)


@bp.route('/')
@login_required
def index():
    return render_template('inscription/index.html', grimpeurs=[])


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        fields = {
            'name': Text,
            'firstname': Text,
            'birthdate': Birthdate,
        }
        error = False
        grimpeur = {}
        for f, checker in fields.items():
            try:
                grimpeur[f] = checker().validate(request.form[f])
            except ValueError as e:
                grimpeur[f] = request.form[f]
                flash(' '.join([f, e]))
                error = True

        if not error:
            model.add_grimpeur(get_db(), g.user['id'], grimpeur)
            return redirect(url_for('inscription.index'))

    return render_template('inscription/create.html')


# def get_post(id, check_author=True):
#     post = model.get_post(get_db(), id)

#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")

#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)

#     return post


# @bp.route('/<int:id>/update', methods=('GET', 'POST'))
# @login_required
# def update(id):
#     post = get_post(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None

#         if not title:
#             error = 'Title is required.'

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             model.update_post(db, id, title, body)
#             return redirect(url_for('inscription.index'))

#     return render_template('inscription/update.html', post=post)


# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     get_post(id)
#     db = get_db()
#     model.delete_post(db, id)
#     return redirect(url_for('inscription.index'))
