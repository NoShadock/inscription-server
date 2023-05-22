INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

-- INSERT INTO post (title, body, author_id, created)
-- VALUES
--   ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
  
INSERT INTO category (label, begin, end)
VALUES
  ('U10', '2012-01-01', '2013-12-31');

INSERT INTO creneau (day, begin, end, allowing, subscribed, category_id)
VALUES
  (7, '17:30', '19:00', 12, 1, 1);

INSERT INTO grimpeur (user_id, name, firstname, birthdate, contact_email, contact_tel, contact2_email, contact2_tel, creneau_id, status)
VALUES
  (1, 'doll', 'bambi', '2018-01-05', 'b@g.fr', '0654231545', NULL, NULL, 1, 'inscrit'),
  (2, 'furry', 'wolf', '2014-02-16', 'x@o.fr', '0753321777', NULL, NULL, NULL, 'en attente de paiement');
