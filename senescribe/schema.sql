DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS creneau;
DROP TABLE IF EXISTS grimpeur;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  label INTEGER NOT NULL,
  begin DATE NOT NULL,
  end DATE NOT NULL
);

CREATE TABLE creneau (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day INTEGER NOT NULL,
  begin TIME NOT NULL,
  end TIME NOT NULL,
  allowing INTEGER NOT NULL,
  subscribed INTEGER NOT NULL,
  category_id INTEGER NOT NULL,
  FOREIGN KEY (category_id) REFERENCES category (id)
);

CREATE TABLE grimpeur (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  firstname TEXT NOT NULL,
  birthdate DATE NOT NULL,
  contact_email TEXT,
  contact_tel TEXT,
  contact2_email TEXT,
  contact2_tel TEXT,
  creneau_id INTEGER,
  status TEXT,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (creneau_id) REFERENCES creneau (id)
);
