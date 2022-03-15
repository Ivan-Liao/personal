create table car (
    id BIGSERIAL NOT NULL PRIMARY KEY
    ,make VARCHAR(100) NOT NULL
    ,model VARCHAR(100) NOT NULL
    ,price NUMERIC(19, 2)
)