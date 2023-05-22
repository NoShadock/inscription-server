from senescribe import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    msg = 'Hello !<br/>\nSi tu souhaites aider à maintenir ce site, fais nous signe : info@senescalade.bzh'
    assert response.data == bytes(msg, 'utf-8')
