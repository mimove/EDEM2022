-- MANUFACTURER

create table manufacturer (
id serial,
name varchar(50) not null,
num_employees int,
constraint pk_manufacturer primary key (id)
);

select * from manufacturer;

insert into manufacturer (name, num_employees) values ('Ford', 29000);


insert into manufacturer (name, num_employees) 
values ('Toyota', 550000);



-- MODEL

create table model(

    id serial,
    name varchar(50) not null,
    manufacturer_id int, 
    constraint pk_model primary key (id),
    constraint fk_model_manufacturer foreign key (manufacturer_id) references manufacturer(id)

);


select * from model;


insert into model (name, manufacturer_id)
values ('Mondeo', 1);

insert into model (name, manufacturer_id)
values ('Fiesta', 1);

insert into model (name, manufacturer_id)
values ('Prius', 2);



-- CAR VERSION


create table version (
    id serial,
    name varchar(50) not null,
    engine varchar(50),
    price numeric,
    cc numeric(2,1),
    id_model int,
    constraint pk_version primary key (id),
    constraint fk_version_model foreign key (id_model) references model (id) on update set null on delete set null
);


select * from version;

insert into version (name, engine, price, cc, id_model)
values ('basic', 'Diesel 4C', 30000, 1.9, 1);

insert into version (name, engine, price, cc, id_model)
values ('medium', 'Diesel 5C', 50000, 2.2, 1);

insert into version (name, engine, price, cc, id_model)
values ('advance', 'Diesel 6C V', 60000, 3.2, 1);



insert into version (name, engine, price, cc, id_model)
values ('sport', 'Gasolina 4C', 50000, 2.1, 2);

insert into version (name, engine, price, cc, id_model)
values ('sport advance', 'Gasolina 8C V', 90000, 3.2, 2);



-- EXTRA

create table extra (
    id serial,
    name varchar(50) not null
    description varchar(300),
    constraint pk_extra primary key (id)
);



create table extra_version (
    id_version int,
    id_extra int,
    price numeric not null check (price >= 0),

    constraint pk_extra_version primary key (id_version, id_extra),
    constraint fk_version_extra foreign key (id_version) references version(id) on update cascade on delete cascade,
    constraint fk_extra_version foreign key (id_extra) references extra(id) on update cascade on delete cascade

);


insert into extra (name, description)
values ('Techo solar', 'lorem ipsum ....');



insert into extra (name, description)
values ('Climatizador', 'lorem ipsum ....');


insert into extra (name, description)
values ('WiFi', 'lorem ipsum ....');


insert into extra (name, description)
values ('Frigorifico', 'lorem ipsum ....');

select * from extra;

-- Ford Mondeo basic Techo solar
insert into extra_version values (1, 1, 3000);

-- Ford Mondeo basic Climatizador
insert into extra_version values (1, 2, 1000);

-- Ford Mondeo basic WiFi
insert into extra_version values (1, 3, 500);


-- Ford Mondeo advance Techo solar
insert into extra_version values (2, 1, 3300);

-- Ford Mondeo advance Climatizador
insert into extra_version values (2, 2, 1200);

-- Ford Mondeo advance WiFi
insert into extra_version values (2, 3, 500);


-- EMPLOYEE

create table employee (
    id serial,
    name varchar(50),
    nif varchar(9) not null unique, 
    phone varchar(9),
    constraint pk_employee primary key (id)

);

insert into employee (name, nif, phone)
values ('Bob', '12345678', '111111111');

insert into employee (name, nif, phone)
values ('Mike', '12345679', '111111122');

select * from employee;


-- CUSTOMER


create table customer (
    id serial,
    name varchar(50),
    email varchar(50) not null unique,
    constraint pk_customer primary key (id)
);


insert into customer (name, email)
values ('Juan', 'juan@gmail.com');

insert into customer (name, email)
values ('Pepe', 'pepe@gmail.com');

select * from customer;


-- VEHICLE

create table vehicle (
    id serial,
    license_num varchar(7),
    creation_date date,
    price_gross numeric,
    price_net numeric,
    type_vehicle varchar(30),

    id_manufacturer int,
    id_model int,
    id_version int,
    id_extra int,

    constraint pk_vehicle primary key (id),
    constraint fk_vehicle_manufacturer foreign key (id_manufacturer) references manufacturer (id),
    constraint fk_vehicle_model foreign key (id_model) references model (id),
    constraint fk_vehicle_extra_version foreign key (id_version, id_extra) references extra_version (id_version, id_extra)


);

insert into vehicle (license_num, price_gross, id_manufacturer, id_model, id_version, id_extra)
values ('1111ABC', 40000, 1, 2, 1, 2);


insert into vehicle (license_num, price_gross, id_manufacturer, id_model, id_version, id_extra)
values ('3456CDV', 60000, 1, 3, 1, 3);

-- SALE

create table sale(
    id serial,
    sale_date date,
    channel varchar(300),

    id_vehicle int,
    id_employee int,
    id_customer int,

    constraint pk_sale primary key (id),
    constraint fk_sale_vehicle foreign key (id_vehicle) references vehicle (id),
    constraint fk_sale_employee foreign key (id_employee) references employee (id),
    constraint fk_sale_customer foreign key (id_customer) references customer (id)
);


insert into sale (sale_date, channel, id_vehicle, id_employee, id_customer)
values ('2022-01-01', 'Phone', 1,1,1);

select * from sale;