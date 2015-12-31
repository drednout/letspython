DROP TABLE IF EXISTS player;
CREATE TABLE player (
    id INT AUTO_INCREMENT,
    name varchar(30) UNIQUE,
    email varchar(30) UNIQUE,
    password varchar(40),
    PRIMARY KEY (id)
);

INSERT INTO player (name, email, password) VALUES ('Vasya', 'vasya@tut.by', '123');
INSERT INTO player (name, email, password) VALUES ('Ilya', 'ilya@gmail.com', '123');
INSERT INTO player (name, email, password) VALUES ('Petya', 'petya@mail.ru', '123');
/*INSERT INTO player (name, email, password) VALUES ('Petya2', 'petya@mail.ru', '123');*/

SELECT id, name, email FROM player;

/*
id      name    email
1       Vasya   vasya@tut.by
2       Ilya    ilya@gmail.com
3       Petya   petya@mail.ru
*/

UPDATE player SET email='petya@petya.com' WHERE name='Petya';
UPDATE player SET email='vasya@vasya.com' WHERE id=1;

SELECT id, name, email FROM player;

/*
id      name    email
1       Vasya   vasya@vasya.com
2       Ilya    ilya@gmail.com
3       Petya   petya@petya.com

*/


SELECT * FROM player ORDER BY id DESC LIMIT 1;
/*
id      name    email   password
3       Petya   petya@petya.com 123
*/ 

DELETE FROM player WHERE id=1;

SELECT id, name, email FROM player;
/*
id      name    email
2       Ilya    ilya@gmail.com
3       Petya   petya@petya.com
*/

DROP TABLE player;
SELECT id, name, email FROM player;
