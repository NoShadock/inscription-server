from werkzeug.security import generate_password_hash


def add_user(db, username, password):
    db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (username, generate_password_hash(password)),
    )
    db.commit()


def fetch_user(db, username):
    return db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()


def get_user(db, user_id):
    return db.execute(
        'SELECT * FROM user WHERE id = ?', (user_id,)
    ).fetchone()
