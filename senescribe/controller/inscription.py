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
    grimpeurs = model.all_grimpeurs(get_db(), g.user['id'])
    return render_template('inscription/index.html', grimpeurs=grimpeurs)


@bp.route('/create', methods=('GET', 'POST'))
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


def get_grimpeur(id, check_user=True):
    grimpeur = model.get_grimpeur(get_db(), grimpeur_id=id)

    if grimpeur is None:
        abort(404, f"Grimpeur id {id} n'existe pas.")
    if check_user and grimpeur['user_id'] != g.user['id']:
        abort(403)

    return grimpeur


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    grimpeur = get_grimpeur(id)

    if request.method == 'POST':
        fields = {
            'name': Text,
            'firstname': Text,
            'birthdate': Birthdate,
        }
        error = False
        grimpeur = dict(grimpeur)
        for f, checker in fields.items():
            try:
                grimpeur[f] = checker().validate(request.form[f])
            except ValueError as e:
                grimpeur[f] = request.form[f]
                flash(' '.join([f, e]))
                error = True

        if not error:
            model.update_grimpeur(get_db(), id, grimpeur)
            return redirect(url_for('inscription.index'))

    return render_template('inscription/update.html', grimpeur=grimpeur)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    model.delete_grimpeur(get_db(), user_id=g.user['id'], grimpeur_id=id)
    return redirect(url_for('inscription.index'))


@bp.route('/checkout', methods=('GET',))
@login_required
def checkout():
    # get_post(id)
    # db = get_db()
    # model.delete_post(db, id)
    return redirect(url_for('inscription.index'))
