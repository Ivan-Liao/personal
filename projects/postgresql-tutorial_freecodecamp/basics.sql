/*
CREATE TABLE table_name (
    {{ column_name }} {{ data type }} {{ optional_constraints }}
)
*/

-- CREATE TABLE example
CREATE TABLE person (
    id int,
    first_name varchar(50),
    last_name varchar(50),
    gender varchar(6),
    date_of_birth TIMESTAMP,
    email varchar(50)
)
;

-- Better CREATE TABLE version
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    gender varchar(6) NOT NULL,
    date_of_birth TIMESTAMP NOT NULL,
    email varchar(50)
)
;

-- INSERT INTO example
INSERT INTO
    person (
        first_name,
        last_name,
        gender,
        date_of_birth,
        email
    )
VALUES
    (
        'Jake',
        'Jones',
        'MALE',
        DATE '1990-01-10',
        'jake@gmail.com'
    ),
    (
        'Anne',
        'Smith',
        'FEMALE',
        DATE '1988-01-09',
        NULL
    )
;

-- Math Operators example
SELECT
    id,
    make,
    model,
    price,
    round(price *.10, 2) AS discount,
    round(price - (price *.10), 2) AS price_after_discount
FROM
    car
;

-- Dates and Time
SELECT NOW();
SELECT NOW()::DATE;
SELECT NOW()::TIME;

-- Demonstration of upsert
SELECT *
FROM person
LIMIT 20;

UPDATE person
SET first_name = 'Jackie'
WHERE id = 1;


INSERT INTO person (id, first_name, last_name, gender, date_of_birth, email)
VALUES(1, 'Jackie', 'Jones', 'FEMALE', '1990-01-10', 'jackie@gmail.com')
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;
-- Notice that only email is changed due to the EXCLUDED keyword

-- useful extensions
-- key,value table
-- uuid