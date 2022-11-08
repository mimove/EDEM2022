create database pagila;
drop database pagila;
-- Creación de tablas

create table if not exists employees(
	id int,
	name varchar,
	married boolean
);


-- ver datos de una tabla

select * from employees;

-- Agregar columnas a las tablas

-- Insertar datos

insert into employees (id, name, married) values (1, 'Paco', true);
insert into employees (id, name, married) values (2, 'Pepe', false);



-- Tipos de datos: CHAR, VARCHAR, TEXT

create table if not exists employees(
	id int,
	name varchar,
	married boolean,
	genre char(1)
);


insert into employees (id, name, married, genre) values (1, 'Paco', true, 'M');
insert into employees (id, name, married, genre) values (2, 'Pepe', false, 'M');



-- Tipo de datos: NUMERIC

create table if not exists employees(
	id int,
	name varchar,
	married boolean,
	genre char(1),
	salary numeric(9,2)
);


insert into employees (id, name, married, genre, salary) values (1, 'Paco', true, 'M', 29998.23);
insert into employees (id, name, married, genre, salary) values (2, 'Pepe', false, 'M', 998.23);



--  Tipo de dato: DATE

create table if not exists employees(
	id int,
	name varchar,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (id, name, married, genre, salary, birth_date) values (2, 'Pepe', false, 'M', 998.23, '1991-07-24');


--  Tipo de dato: TIME

create table if not exists employees(
	id int,
	name varchar,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (id, name, married, genre, salary, birth_date, start_at)
values (2, 'Pepe', false, 'M', 998.23, '1991-07-24', '08:30:00');



-- Identificador

create table if not exists employees(
	id serial,
	name varchar,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (name, married, genre, salary, birth_date, start_at)
values ('Pepe', false, 'M', 998.23, '1991-07-24', '08:30:00');

insert into employees (name, married, genre, salary) values ('Paco', true, 'M', 29998.23);


-- Primary key

create table if not exists employees(
	id serial primary key,
	name varchar,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (name, married, genre, salary, birth_date, start_at)
values ('Pepe', false, 'M', 998.23, '1991-07-24', '08:30:00');

insert into employees (name, married, genre, salary) values ('Paco', true, 'M', 29998.23);




-- Hacer que un campo sea obligatorio con NOT NULL

create table if not exists employees(
	id serial primary key,
	name varchar not null,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (name, married, genre, salary, birth_date, start_at)
values ('Pepe', false, 'M', 998.23, '1991-07-24', '08:30:00');

insert into employees (name, married, genre, salary) values ('Paco', true, 'M', 29998.23);



-- Hacer que un campo sea unico con UNIQUE



create table if not exists employees(
	id serial primary key,
	name varchar not null,
	email varchar(100) unique,
	married boolean,
	genre char(1),
	salary numeric(9,2),
	birth_date date,
	start_at TIME
);


insert into employees (name, email, married, genre, salary, birth_date, start_at)
values ('Pepe', 'pepe@gmail.com', false, 'M', 998.23, '1991-07-24', '08:30:00');

insert into employees (name, email, married, genre, salary) values ('Paco', 'paco@gmail.com', true, 'M', 29998.23);




-- Restricciones en rangos de datos

create table if not exists employees(
	id serial primary key,
	name varchar not null,
	email varchar(100) unique,
	married boolean,
	genre char(1),
	salary numeric(9,2) check (salary > 0),
	birth_date date check (birth_date > '1975-01-01'),
	start_at TIME
);


insert into employees (name, email, married, genre, salary, birth_date, start_at)
values ('Pepe', 'pepe@gmail.com', false, 'M', 998.23, '1991-07-24', '08:30:00');


-- Renombrar tabla
alter table if exists employees rename to employees_2022;


-- Agregar columnas a las tablas

alter table if exists employees add column email varchar(100);

select * from employees;

-- Borrar columnas de las tablas

alter table employees drop column if exists email;


-- Borrar tabla

drop table if exists employees;
