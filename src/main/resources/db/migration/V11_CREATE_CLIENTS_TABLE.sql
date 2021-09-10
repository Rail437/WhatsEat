create table hibernate_sequence
(
    next_val bigint
);

CREATE TABLE clients
(
    id       uuid,
    name     varchar(64) not null,
    login    varchar(64) not null,
    password varchar(64) not null,
    PRIMARY KEY (id)
);