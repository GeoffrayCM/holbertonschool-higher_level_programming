CREATE TABLE IF NOT EXISTS states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO states (name) VALUES ('California');
INSERT INTO states (name) VALUES ('Arizona');
INSERT INTO states (name) VALUES ('Texas');
INSERT INTO states (name) VALUES ('New York');
INSERT INTO states (name) VALUES ('Nevada');

