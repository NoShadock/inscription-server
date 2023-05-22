grimpeur_fields = ['name', 'firstname', 'birthdate', 'contact_email', 'contact_tel', 'contact2_email',
                   'contact2_tel', 'creneau_id', 'status']


def all_grimpeurs(db, user_id):
    return db.execute(
        f'SELECT id, {", ".join(grimpeur_fields)}'
        ' FROM grimpeur c'
        ' WHERE c.user_id = ?'
        ' ORDER BY name, firstname, created DESC',
        (user_id, )
    ).fetchall()


def add_grimpeur(db, user_id, grimpeur):
    db.execute(
        f'INSERT INTO grimpeur (user_id, {", ".join(grimpeur_fields)})'
        f' VALUES (?, {", ".join("?" for f in grimpeur_fields)})',
        (user_id, *(grimpeur.get(f, None) for f in grimpeur_fields))
    )
    db.commit()


def get_grimpeur(db, grimpeur_id):
    return db.execute(
        f'SELECT id, user_id, {", ".join(grimpeur_fields)}'
        ' FROM grimpeur c'
        ' WHERE c.id = ?',
        (grimpeur_id, )
    ).fetchone()


def update_grimpeur(db, id, grimpeur):
    db.execute(
        'UPDATE grimpeur'
        f' SET {", ".join(f"{col}=?" for col in grimpeur)}'
        ' WHERE id = ?',
        (*(grimpeur[col] for col in grimpeur), id, )
    )
    db.commit()


def delete_grimpeur(db, user_id, grimpeur_id):
    db.execute(
        'DELETE FROM grimpeur'
        ' WHERE user_id = ? AND id = ?',
        (user_id, grimpeur_id, )
    )
    db.commit()
