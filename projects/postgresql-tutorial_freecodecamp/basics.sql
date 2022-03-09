/*
CREATE TABLE table_name (
    {{ column_name }} {{ data type }} {{ optional_constraints }}
)
*/

-- CREATE TABLE example
CREATE TABLE person (
    id int
    ,first_name varchar(50)
    ,last_name varchar(50)
    ,gender varchar(6)
    ,date_of_birth TIMESTAMP
    ,email varchar(50)
)

-- Better CREATE TABLE version
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY
    ,first_name varchar(50) NOT NULL
    ,last_name varchar(50) NOT NULL
    ,gender varchar(6) NOT NULL
    ,date_of_birth TIMESTAMP NOT NULL
    ,email varchar(50)
)

-- INSERT INTO example
INSERT INTO person (
    first_name
    ,last_name
    ,gender
    ,date_of_birth
    ,email
)
VALUES ('Jake', 'Jones', 'MALE',DATE '1990-01-10', 'jake@gmail.com'),
    ('Anne','Smith','FEMALE',DATE '1988-01-09',NULL);
