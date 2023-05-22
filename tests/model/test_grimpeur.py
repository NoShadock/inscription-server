from senescribe.db import get_db
from senescribe import model


def test_add_grimpeur(app):
    with app.app_context():
        db = get_db()
        gs = model.all_grimpeurs(db, 1)
        for g in gs:
            print(dict(g))
