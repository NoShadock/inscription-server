def all_posts(db):
    return db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()


def add_post(db, title, body, user_id):
    db.execute(
        'INSERT INTO post (title, body, author_id)'
        ' VALUES (?, ?, ?)',
        (title, body, user_id)
    )
    db.commit()


def get_post(db, post_id):
    return db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (post_id,)
    ).fetchone()


def update_post(db, post_id, title, body):
    db.execute(
        'UPDATE post SET title = ?, body = ?'
        ' WHERE id = ?',
        (title, body, post_id)
    )
    db.commit()


def delete_post(db, post_id):
    db.execute('DELETE FROM post WHERE id = ?', (post_id,))
    db.commit()
