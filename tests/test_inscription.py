import pytest
from senescribe.db import get_db


def assert_in(tokens, response):
    for token in tokens:
        assert bytes(token, 'utf-8') in response.data


def test_index(client, auth):
    response = client.get('/')
    assert response.headers["Location"] == "/auth/login"

    response = client.get('/', follow_redirects=True)
    assert_in(["Se connecter", "Créer un compte"], response)

    auth.login()
    response = client.get('/')
    assert_in(['Se déconnecter', 'Inscriptions',
               'Nom', 'Prénom', 'Naissance', 'Catégorie', 'Créneau', 'Statut',
               'Ajouter un·e grimpeur·euse'], response)


@pytest.mark.parametrize('path', (
    '/create',
    # '/1/update',
    # '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_add_grimpeur(client, auth, app):
    with app.app_context():
        db = get_db()
        old_count = db.execute('SELECT COUNT(id) FROM grimpeur').fetchone()[0]
        # add one grimpeur
        auth.login()
        assert client.get('/create').status_code == 200
        client.post('/create', data={'name': 'grant', 'firstname': 'hugh', 'birthdate': '2010-05-02'})
        # recount
        count = db.execute('SELECT COUNT(id) FROM grimpeur').fetchone()[0]
        assert count == old_count + 1


# def test_author_required(app, client, auth):
#     # change the post author to another user
#     with app.app_context():
#         db = get_db()
#         db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
#         db.commit()

#     auth.login()
#     # current user can't modify other user's post
#     assert client.post('/1/update').status_code == 403
#     assert client.post('/1/delete').status_code == 403
#     # current user doesn't see edit link
#     assert b'href="/1/update"' not in client.get('/').data


# @pytest.mark.parametrize('path', (
#     '/2/update',
#     '/2/delete',
# ))
# def test_exists_required(client, auth, path):
#     auth.login()
#     assert client.post(path).status_code == 404


# def test_update(client, auth, app):
#     auth.login()
#     assert client.get('/1/update').status_code == 200
#     client.post('/1/update', data={'title': 'updated', 'body': ''})

#     with app.app_context():
#         db = get_db()
#         post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
#         assert post['title'] == 'updated'


# @pytest.mark.parametrize('path', (
#     '/create',
#     '/1/update',
# ))
# def test_create_update_validate(client, auth, path):
#     auth.login()
#     response = client.post(path, data={'title': '', 'body': ''})
#     assert b'Title is required.' in response.data


# def test_delete(client, auth, app):
#     auth.login()
#     response = client.post('/1/delete')
#     assert response.headers["Location"] == "/"

#     with app.app_context():
#         db = get_db()
#         post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
#         assert post is None
